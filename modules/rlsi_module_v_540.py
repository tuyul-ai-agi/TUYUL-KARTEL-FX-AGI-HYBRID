"""
RLSI Module v5.4.0 (Modular)
----------------------------
Reflex Layer Smart Index — perhitungan momentum jangka pendek.
"""

import pandas as pd

class RLSIModuleStandalone:
    def calculate(self, df: pd.DataFrame, period: int = 14):
        delta = df["close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rlsi = 100 - (100 / (1 + rs))
        return {"RLSI": round(rlsi.iloc[-1], 2)}
