"""Reflex coherence and confidence metric utilities."""

from __future__ import annotations

from math import cos
from random import random, uniform
from time import time


def compute_confidence_factors(pair: str, timeframe: str):
    """Generate pseudo-random fusion factors (EMA, VWAP, RC, DVG)."""

    ema = round(uniform(0.6, 0.95), 3)
    vwap = round(uniform(0.7, 1.0), 3)
    rc = round(uniform(0.65, 0.9), 3)
    dvg = round(uniform(0.1, 0.35), 3)
    return {"ema": ema, "vwap": vwap, "rc": rc, "dvg": dvg}


def compute_reflex_coherence() -> float:
    """Compute a pseudo-realistic reflex coherence score between 0 and 1."""

    periodic = cos(time() / 180.0) * 0.05
    stochastic = (random() - 0.5) * 0.04
    drift = 0.07 if periodic + stochastic + 0.78 > 0.9 else 0.0
    value = 0.78 + periodic + stochastic - drift
    return round(max(0.0, min(1.0, value)), 4)
