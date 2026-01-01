"""
TUYUL Data Bridge v6.0
-----------------------------------------
Connects TwelveData / FX feeds to reflective learning.
"""

import requests, json
from datetime import datetime
from clients.reflective_logger import ReflectiveLogger

class TuyulDataBridge:
    def __init__(self, api_key=None):
        self.endpoint = "https://api.twelvedata.com/time_series"
        self.api_key = api_key
        self.logger = ReflectiveLogger()

    def fetch(self, symbol="GBP/USD", interval="1h"):
        params = {"symbol": symbol, "interval": interval, "apikey": self.api_key}
        res = requests.get(self.endpoint, params=params)
        data = res.json()
        self.logger.log(f"Fetched {symbol} data @ {datetime.utcnow()}")
        return data
