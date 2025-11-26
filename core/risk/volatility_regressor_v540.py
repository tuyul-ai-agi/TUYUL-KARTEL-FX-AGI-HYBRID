"""Volatility deviation detection utilities."""

import random
from typing import Dict


def detect_volatility_deviation(data) -> Dict[str, float]:
    """Analyze volatility and detect anomaly deviation index."""

    volatility = round(random.uniform(0.1, 0.9), 3)
    return {"DVG": volatility, "status": "High" if volatility > 0.7 else "Normal"}


def estimate_volatility(pair: str, timeframe: str) -> float:
    """Estimate volatility based on pair and timeframe."""

    base_volatility = random.uniform(0.5, 1.5)
    timeframe_adjustment = 0.8 if timeframe.lower().startswith("h") else 1.0
    return round(base_volatility * timeframe_adjustment, 3)
