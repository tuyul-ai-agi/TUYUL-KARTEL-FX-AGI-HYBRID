import random


def estimate_volatility(pair: str, timeframe: str):
    base_volatility = random.uniform(0.5, 1.5)
    timeframe_adjustment = 0.8 if timeframe.lower().startswith("h") else 1.0
    return round(base_volatility * timeframe_adjustment, 3)
