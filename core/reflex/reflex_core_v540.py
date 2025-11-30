"""
Reflex Core v5.4.0
------------------
Reflex Layer — sistem reaksi cepat terhadap dinamika harga & momentum pasar.
"""

import pandas as pd
from core.fushion.rlsi_module_v540 import RLSIModule


class ReflexCore:
    def __init__(self):
        self.rlsi = RLSIModule()

    def analyze(self, df: pd.DataFrame):
        """Analisa reaksi cepat berdasarkan RLSI & candle pattern"""
        rlsi_val = self.rlsi.calculate(df)
        candle = df.tail(1).iloc[0]
        signal = "BUY" if rlsi_val < 40 else "SELL" if rlsi_val > 60 else "WAIT"

        return {
            "RLSI": rlsi_val,
            "CandleClose": candle["close"],
            "Signal": signal,
            "Strength": round(abs(rlsi_val - 50) / 50, 3),
            "Strength": round(abs(rlsi_val - 50) / 50, 3)
        }
