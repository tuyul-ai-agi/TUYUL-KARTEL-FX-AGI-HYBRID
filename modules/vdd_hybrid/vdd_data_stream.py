import pandas as pd
import numpy as np
import requests
from datetime import datetime

class VDDDataStream:
    """
    TUYUL FX ULTRA WOLF v5.4.0
    Modul: VDD Data Stream (Volatility-Dollar Feed)
    Fungsi: Streamer real-time untuk indeks VIX, DXY, VIX3M
    """

    def __init__(self, api_key: str, source: str = "twelvedata"):
        self.api_key = api_key
        self.source = source
        self.symbols = ["VIX", "DXY", "VIX3M"]

    def fetch_data(self):
        """Ambil data live"""
        url = f"https://api.twelvedata.com/time_series"
        result = {}
        for sym in self.symbols:
            params = {"symbol": sym, "interval": "1min", "apikey": self.api_key, "outputsize": 10}
            r = requests.get(url, params=params)
            if r.status_code == 200:
                df = pd.DataFrame(r.json()['values'])
                df['datetime'] = pd.to_datetime(df['datetime'])
                df = df.sort_values('datetime')
                result[sym] = df
        return result
