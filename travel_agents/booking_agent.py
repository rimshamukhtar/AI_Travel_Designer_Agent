from agents import Agent
from model_loader import model
from tools import get_flights, suggest_hotels

BookingAgent = Agent(
    name="Booking Assistant",
    instructions="Use get_flights and suggest_hotels to provide booking details.",
    tools=[get_flights, suggest_hotels],
    model=model
)