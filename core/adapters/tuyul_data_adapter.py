from __future__ import annotations

import json
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping


@dataclass
class FeedRecord:
    pair: str
    interval: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: datetime

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pair": self.pair,
            "interval": self.interval,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "timestamp": self.timestamp.isoformat(),
        }


class TuyulDataAdapter:
    def __init__(self, live_feed_path: Path | str | None = None) -> None:
        self.live_feed_path = Path(live_feed_path) if live_feed_path else Path("vaults/live_feed.jsonl")

    def fetch_live_data(self, pair: str, interval: str) -> Dict[str, Any]:
        base_price = random.uniform(100, 200)
        high = base_price + random.uniform(0, 5)
        low = base_price - random.uniform(0, 5)
        close = random.uniform(low, high)

        record = FeedRecord(
            pair=pair,
            interval=interval,
            open=base_price,
            high=high,
            low=low,
            close=close,
            volume=random.uniform(10_000, 100_000),
            timestamp=datetime.now(tz=timezone.utc),
        )
        return record.to_dict()

    def save_feed(self, data: Mapping[str, Any]) -> None:
        self.live_feed_path.parent.mkdir(parents=True, exist_ok=True)
        with self.live_feed_path.open("a", encoding="utf-8") as file:
            json.dump(data, file, default=str)
            file.write("\n")
