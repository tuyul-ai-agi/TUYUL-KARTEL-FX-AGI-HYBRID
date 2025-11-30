"""
VDD Data Stream
---------------
Membaca dan menyiapkan feed data dari FX/Kartel Vault untuk deteksi rezim hybrid.
"""

import pandas as pd
import json

class VDDDataStream:
    def load_from_vault(self, path: str):
        """Load data JSON dari Vault"""
        with open(path) as f:
            data = json.load(f)
        return pd.DataFrame(data.get("candles", []))

    def preprocess(self, df: pd.DataFrame):
        """Normalisasi data feed"""
        df["range"] = df["high"] - df["low"]
        df["mid"] = (df["high"] + df["low"]) / 2
        df = df.dropna()
        return df
