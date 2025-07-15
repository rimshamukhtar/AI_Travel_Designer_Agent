from agents import Agent
from model_loader import model
from tools import suggest_attractions, suggest_food

ExploreAgent = Agent(
    name="Explore Guide",
    instructions="Use suggest_attractions and suggest_food to recommend fun things.",
    tools=[suggest_attractions, suggest_food],
    model=model
)