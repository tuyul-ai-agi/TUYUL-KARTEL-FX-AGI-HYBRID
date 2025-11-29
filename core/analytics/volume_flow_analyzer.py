"""
Volume Flow Analyzer
--------------------
Analisa hubungan volume–price dan distribusi institusional antar sesi.
"""

import pandas as pd


class VolumeFlowAnalyzer:
    def analyze(self, df: pd.DataFrame):
        df["vpi"] = df["volume"] * (df["close"] - df["open"])
        total = df["vpi"].sum()
        flow_bias = "BUY" if total > 0 else "SELL"
        strength = abs(total) / len(df)
        return {"bias": flow_bias, "strength": round(strength, 3)}
