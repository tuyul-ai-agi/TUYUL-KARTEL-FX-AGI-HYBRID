"""
Reflex Fastlane
---------------
Mode reflex cepat tanpa melewati Fusion Layer.
Ideal untuk high-frequency reflex (scalping logic).
"""

import pandas as pd
from core.reflex.reflex_core_v540 import ReflexCore


class ReflexFastlane:
    def __init__(self):
        self.reflex = ReflexCore()

    def quick_scan(self, df: pd.DataFrame):
        """Scan cepat arah harga"""
        result = self.reflex.analyze(df)
        signal = result["Signal"]
        if signal == "BUY":
            direction = "UP"
        elif signal == "SELL":
            direction = "DOWN"
        else:
            direction = "FLAT"
        return {
            "direction": direction,
            "momentum_strength": result["Strength"],
            "rlsi": result["RLSI"],
        direction = "UP" if result["Signal"] == "BUY" else "DOWN" if result["Signal"] == "SELL" else "FLAT"
        return {
            "direction": direction,
            "momentum_strength": result["Strength"],
            "rlsi": result["RLSI"]
        }
