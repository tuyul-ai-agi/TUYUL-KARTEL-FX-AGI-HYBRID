"""
VDD Feature Engine
------------------
Membangun fitur dari data pasar untuk deteksi rezim hybrid.
"""

import numpy as np
import pandas as pd


class VDDFeatureEngine:
    def extract_features(self, df: pd.DataFrame):
        vol = df["range"].mean()
        bias_strength = np.sign(df["close"].iloc[-1] - df["open"].iloc[0])
        coherence = round(abs(df["close"].corr(df["volume"])), 3)
        return {
            "volatility": round(vol, 4),
            "bias_strength": float(bias_strength),
            "coherence_index": coherence,
        }
