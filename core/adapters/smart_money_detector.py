"""
Smart Money Detector
--------------------
Deteksi aktivitas smart money melalui analisa volume dan candle delta.
"""

import pandas as pd

class SmartMoneyDetector:
    def __init__(self, threshold=1.5):
        self.threshold = threshold

    def detect_flow(self, df: pd.DataFrame):
        df["delta"] = df["close"] - df["open"]
        df["flow_strength"] = (df["delta"].abs() / df["range"]) * df["volume"]
        df["smart_flow"] = df["flow_strength"] > (df["flow_strength"].mean() * self.threshold)
        return df

    def summarize_bias(self, df: pd.DataFrame):
        active_flows = df[df["smart_flow"]]
        direction = "BUY" if active_flows["delta"].sum() > 0 else "SELL"
        return {"bias": direction, "intensity": round(active_flows["flow_strength"].mean(), 3)}
