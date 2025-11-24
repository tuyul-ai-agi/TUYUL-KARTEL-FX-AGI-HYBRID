"""Manual text feed parser for OHLC data."""

import json
from pathlib import Path
from typing import Dict, List

VAULT_ROOT = Path(__file__).resolve().parents[2] / "vaults"


def parse_text_to_json(text_feed: str) -> Dict[str, List[Dict[str, float]]]:
    """Parse comma-separated OHLC lines into JSON feed structure."""

    lines = text_feed.strip().split("\n")
    data = []
    for line in lines:
        time_value, open_value, high_value, low_value, close_value = line.split(",")
        data.append(
            {
                "time": time_value,
                "open": float(open_value),
                "high": float(high_value),
                "low": float(low_value),
                "close": float(close_value),
            }
        )
    return {"feed": data}


def save_manual_feed(feed: Dict[str, List[Dict[str, float]]]) -> None:
    """Save manual feed content into the manual vault file."""

    vault_path = VAULT_ROOT / "manual_feed.json"
    vault_path.parent.mkdir(parents=True, exist_ok=True)
    with vault_path.open("w", encoding="utf-8") as file:
        json.dump(feed, file, indent=2)
