#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐺 Reflective Lorentzian Adapter – TUYUL FX AGI v5.8r+
------------------------------------------------------
Fungsi: Mengkonversi output Lorentzian ML menjadi parameter Layer–12
        (FusionConf₁₂, WLWCI, RCAdj, Integrity Index, Bias)
"""

from __future__ import annotations

import datetime
import json
from pathlib import Path
from typing import Dict, List

import numpy as np

LOG_PATH = Path("logs/lorentzian_metrics_log.json")
LOG_PATH.parent.mkdir(exist_ok=True)


def compute_lorentzian_distance(features: np.ndarray, reference: np.ndarray) -> float:
    """Menghitung jarak reflektif Lorentzian antar vektor fitur."""
    return float(np.sum(np.log1p(np.abs(features - reference))))


def tuyul_lorentzian_adapter(
    prediction: float, distances: List[float], kernel_estimate: List[float]
) -> Dict[str, object]:
    """Adaptasi hasil Lorentzian Classification ke format TUYUL Layer–12."""
    fusion_conf12 = min(1.0, abs(prediction) / (abs(prediction) + 10))
    rcadj = 1 - (np.std(distances) / (np.mean(distances) + 1e-9))
    wlwci = (
        1 - np.mean(np.abs(np.diff(kernel_estimate[-5:])))
        if len(kernel_estimate) > 5
        else 0.9
    )
    bias = (
        "Bullish"
        if prediction > 0
        else "Bearish"
        if prediction < 0
        else "Neutral"
    )
    integrity_index = np.mean([fusion_conf12, wlwci, rcadj])

    result = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "fusion_conf12": round(fusion_conf12, 3),
        "wlwci": round(wlwci, 3),
        "rcadj": round(rcadj, 3),
        "integrity_index": round(integrity_index, 3),
        "bias": bias,
    }

    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(result, indent=2) + ",\n")

    return result
