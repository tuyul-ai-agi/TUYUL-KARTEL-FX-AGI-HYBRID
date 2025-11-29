"""
RLSI Module v5.4.0
------------------
Reflex Layer Smart Index — deteksi momentum mikro jangka pendek.
"""

import pandas as pd

class RLSIModule:
    def calculate(self, df: pd.DataFrame, period: int = 14):
        delta = df["close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rlsi = 100 - (100 / (1 + rs))
        return round(rlsi.iloc[-1], 2)
