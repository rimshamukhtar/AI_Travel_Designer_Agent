
def tool(func):
    return func

@tool
def get_flights(destination: str, dates: str) -> str:
    return f"✈️ Flights to {destination} on {dates} start from $499 (mock)."

@tool
def suggest_hotels(destination: str) -> str:
    return f"🏨 Hotels in {destination}: Grand Resort, Cozy Inn, Budget Stay."

@tool
def suggest_attractions(destination: str) -> str:
    return f"📍 Visit in {destination}: Sunset Beach, Art Museum, Old Market."

@tool
def suggest_food(destination: str) -> str:
    return f"🍽️ Try in {destination}: Shawarma, Dumplings, Chai Latte."
