"""Fusion Reflective Confidence helper (v5.7.3r++).

Calculates CONF12, RCAdj, integrity index, and reflective regime state based on
reflective energy, adaptive weights, and macro factors.
"""

from __future__ import annotations

from typing import Dict, Iterable

import numpy as np


def fusion_confidence(
    trq_mean: float,
    weights: Iterable[float],
    macro_factor: float,
    coherence_index: float = 0.9,
) -> Dict[str, float | str]:
    """Compute reflective fusion confidence metrics.

    Args:
        trq_mean: Average reflective TRQ 3D energy.
        weights: Reflective weights (alpha, beta, gamma).
        macro_factor: Global macro factor (for example, RVI).
        coherence_index: Reflective coherence index in the range [0, 1].

    Returns:
        A mapping with CONF12, RCAdj, integrity index, and reflective regime state.
    """

    weight_list = list(weights)
    if len(weight_list) != 3:
        raise ValueError(
            "weights must contain exactly three elements (alpha, beta, gamma)"
        )

    alpha, beta, gamma = (float(value) for value in weight_list)

    conf12 = (
        (alpha * trq_mean)
        + (beta * (trq_mean * coherence_index))
        + (gamma * macro_factor)
    )
    rcadj = float(np.tanh(conf12 * 1.15))
    integrity_index = float(
        np.clip(1 - abs(trq_mean - macro_factor) * (1 - coherence_index), 0, 1)
    )

    if integrity_index >= 0.9 and conf12 > 0.9:
        regime = "Expansion"
    elif integrity_index >= 0.75:
        regime = "Neutral"
    else:
        regime = "Stressed"

    return {
        "conf12": round(float(conf12), 3),
        "rcadj": round(rcadj, 3),
        "integrity_index": round(integrity_index, 3),
        "regime": regime,
    }
