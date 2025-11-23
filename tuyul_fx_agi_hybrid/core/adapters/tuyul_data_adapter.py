"""Data bridge for live price feeds."""

import json
import random
from typing import Dict


class TuyulDataAdapter:
    """Integrate simulated TwelveData feed and persistence to vault."""

    def __init__(self) -> None:
        self.data_source = "TwelveData"

    def fetch_live_data(self, pair: str, interval: str = "1h") -> Dict[str, float]:
        """Return simulated OHLC feed data for a symbol.

        Args:
            pair: Trading pair to fetch.
            interval: Timeframe for the feed.

        Returns:
            Dictionary with OHLC and volume values.
        """

        data = {
            "pair": pair,
            "interval": interval,
            "open": round(random.uniform(1900, 2000), 2),
            "close": round(random.uniform(1900, 2000), 2),
            "high": round(random.uniform(1900, 2005), 2),
            "low": round(random.uniform(1895, 1995), 2),
            "volume": random.randint(1000, 5000),
        }
        return data

    def save_feed(self, data: Dict[str, float]) -> None:
        """Persist feed data to the live feed vault."""

        with open("vaults/live_feed.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
