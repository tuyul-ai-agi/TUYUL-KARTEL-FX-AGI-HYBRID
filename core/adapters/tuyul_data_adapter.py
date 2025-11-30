"""
Tuyul Data Adapter
------------------
Mengubah data mentah (CSV/API) menjadi format siap olah untuk AGI Hybrid.
"""

import pandas as pd


class TuyulDataAdapter:
    def __init__(self, source=None):
        self.source = source

    def load_csv(self, file_path: str) -> pd.DataFrame:
        """Load data CSV pasar"""
        df = pd.read_csv(file_path)
        df.columns = [c.strip().lower() for c in df.columns]
        return df

    def normalize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalisasi kolom OHLC & volume"""
        for col in ["open", "high", "low", "close", "volume"]:
            if col not in df.columns:
                raise KeyError(f"Missing {col} in dataset")
        df["mid"] = (df["high"] + df["low"]) / 2
        df["range"] = df["high"] - df["low"]
        return df

    def get_latest_snapshot(self, df: pd.DataFrame):
        """Ambil data candle terakhir"""
        return df.tail(1).to_dict("records")[0]
