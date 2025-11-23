import random


def compute_confidence_factors(pair, timeframe):
    """Menghitung variabel dasar fusion (EMA, VWAP, RC, DVG)."""
    ema = round(random.uniform(0.6, 0.95), 3)
    vwap = round(random.uniform(0.7, 1.0), 3)
    rc = round(random.uniform(0.65, 0.9), 3)
    dvg = round(random.uniform(0.1, 0.35), 3)
    return {"ema": ema, "vwap": vwap, "rc": rc, "dvg": dvg}
"""Reflex coherence metric utilities."""

from __future__ import annotations

from math import cos
from random import random
from time import time

_DEF_BASE_REFLEX = 0.78
_DEF_DRIFT_SCALE = 0.07
_STABILITY_THRESHOLD = 0.9


def compute_reflex_coherence() -> float:
    """Compute a pseudo-realistic reflex coherence score between 0 and 1."""

    periodic = cos(time() / 180.0) * 0.05
    stochastic = (random() - 0.5) * 0.04
    drift = _DEF_DRIFT_SCALE if periodic + stochastic + _DEF_BASE_REFLEX > _STABILITY_THRESHOLD else 0.0
    value = _DEF_BASE_REFLEX + periodic + stochastic - drift
    return round(max(0.0, min(1.0, value)), 4)
