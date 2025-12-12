"""
Reflex Core v5.7.3r++
--------------------
Reflex Layer — sistem reaksi cepat terhadap dinamika harga & momentum pasar.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class ReflexCore:
    def __init__(self):
        self.default_period = 14

    def _calculate_rlsi(self, df: pd.DataFrame) -> float:
        closes = df.get("close")
        if closes is None or len(closes) < 2:
            return 50.0

        delta = closes.diff().dropna()
        gain = delta.clip(lower=0).rolling(window=self.default_period, min_periods=1).mean()
        loss = (-delta.clip(upper=0)).rolling(window=self.default_period, min_periods=1).mean()
        rs = gain / loss.replace(0, np.nan).fillna(0.0001)
        rlsi = 100 - (100 / (1 + rs))
        return float(rlsi.iloc[-1])

    def _rcadj(self, closes: pd.Series) -> float:
        if len(closes) < 2:
            return 0.0
        index_array = np.arange(len(closes))
        correlation = np.corrcoef(index_array, closes.fillna(method="ffill"))[0, 1]
        return float(round(correlation, 3))

    def analyze(self, df: pd.DataFrame):
        """Analisa reaksi cepat berdasarkan RLSI & candle pattern."""

        rlsi_val = self._calculate_rlsi(df)
        candle = df.tail(1).iloc[0]
        signal = "BUY" if rlsi_val < 40 else "SELL" if rlsi_val > 60 else "WAIT"
        coherence = round(max(0.0, 1 - abs(rlsi_val - 50) / 50), 3)
        rcadj = self._rcadj(df.get("close", pd.Series(dtype=float)))

        return {
            "RLSI": rlsi_val,
            "CandleClose": candle["close"],
            "Signal": signal,
            "Strength": round(abs(rlsi_val - 50) / 50, 3),
            "conf_reflex": coherence,
            "rcadj": rcadj,
        }
