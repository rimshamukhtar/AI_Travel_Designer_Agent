from agents import Agent, Runner, set_tracing_disabled
import chainlit as cl
from agents.extensions.models.litellm_model import LitellmModel
import os, asyncio, re
from dotenv import load_dotenv

from travel_agents.destination_agent import DestinationAgent
from travel_agents.booking_agent import BookingAgent
from travel_agents.explore_agent import ExploreAgent

from tools import get_flights, suggest_hotels, suggest_food, suggest_attractions

load_dotenv()
set_tracing_disabled(True)

model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

user_state = {}

@cl.on_chat_start
async def chat_start():
    await cl.Message(content="👋 Hello! I'm your AI Travel Designer. Ready to plan your next adventure?").send()
    await cl.Message(content="🌤️ What's your travel mood?\nPlease choose one:\n1. Relaxing 🌴\n2. Adventure 🧗\n3. Romantic 💖\n4. Cultural 🕌\n(Type the number or mood)").send()

@cl.on_message
async def main(msg: cl.Message):
    uid = msg.author
    if uid not in user_state:
        user_state[uid] = {"step": 1}

    state = user_state[uid]

    # --- Step 1: Mood ---
    if state["step"] == 1:
        state["mood"] = msg.content.strip()
        state["step"] = 2
        await cl.Message(content="💸 How would you describe your travel budget?\nPlease type: `friendly`, `normal`, or `luxury`.").send()
        return

    # --- Step 2: Budget & Generate Plan ---
    if state["step"] == 2:
        state["budget"] = msg.content.strip().lower()
        mood = state["mood"]
        budget = state["budget"]

        # Call DestinationAgent
        dest_run = await Runner.run(DestinationAgent, input=mood)
        dest_output = dest_run.final_output

        # Extract all bold destinations from Gemini response
        destinations = re.findall(r'\*\*([^*\n]+)\*\*', dest_output)

        plan = f"""
📍 **Top Destinations for *{mood}* mood**
{dest_output}

---
"""

        for dest in destinations[:3]:
            flight_info = get_flights(dest, "next month")
            hotel_info = suggest_hotels(dest)
            attractions = suggest_attractions(dest)
            food = suggest_food(dest)

            plan += f"""
🌍 **Destination:** {dest}
✈️ {flight_info}
🏨 {hotel_info}
📍 {attractions}
🍽️ {food}

---
"""

        plan += f"""
💸 **Your Budget Preference:** {budget.capitalize()}

Type `restart` to plan another trip.
"""

        await cl.Message(content=plan).send()
        user_state[uid] = {"step": 1}
        return

    # --- Restart command ---
    if msg.content.strip().lower() == "restart":
        user_state[uid] = {"step": 1}
        await cl.Message(content="🌤️ Let's begin again! What's your travel mood?").send()
        return

    # Fallback
    await cl.Message(content="Please follow the prompts to plan your trip ✈️").send()
