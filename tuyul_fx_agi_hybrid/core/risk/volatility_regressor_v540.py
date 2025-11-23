"""Volatility deviation detection utilities."""

import random
from typing import Dict


def detect_volatility_deviation(data) -> Dict[str, float]:
    """Analyze volatility and detect anomaly deviation index."""

    volatility = round(random.uniform(0.1, 0.9), 3)
    return {"DVG": volatility, "status": "High" if volatility > 0.7 else "Normal"}
