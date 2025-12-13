"""
TUYUL FX AGI v5.7.8 - VDD Feature Engine (Reflective)
Builds volatility-driven features for Kartel macro awareness.
"""

from datetime import datetime
from typing import Dict

import numpy as np
import pandas as pd


class VDDFeatureEngine:
    def extract_features(self, df: pd.DataFrame) -> Dict[str, float]:
        if df.empty:
            return {
                "volatility": 0.0,
                "bias_strength": 0.0,
                "coherence_index": 0.0,
                "timestamp": self._ts(),
            }

        vol = float(df["range"].mean()) if "range" in df else 0.0
        open_close = float(df["close"].iloc[-1] - df["open"].iloc[0]) if {"close", "open"}.issubset(df.columns) else 0.0
        bias_strength = float(np.sign(open_close))

        coherence = 0.0
        if {"close", "volume"}.issubset(df.columns) and df["close"].std(ddof=0) != 0 and df["volume"].std(ddof=0) != 0:
            coherence = round(abs(df["close"].corr(df["volume"])), 3)

        return {
            "volatility": round(vol, 4),
            "bias_strength": bias_strength,
            "coherence_index": coherence,
            "timestamp": self._ts(),
        }

    @staticmethod
    def _ts() -> str:
        return datetime.utcnow().isoformat() + "Z"
