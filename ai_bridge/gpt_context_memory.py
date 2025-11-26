import json
from datetime import datetime, timezone
from pathlib import Path


class GPTContextMemory:
    def __init__(self, path="vaults/context_memory.json"):
        self.path = Path(path)
        self.memory = self._load_memory()

    def _load_memory(self):
        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"sessions": []}
        except json.JSONDecodeError:
            return {"sessions": []}

    def save_context(self, pair, timeframe, conf12, rcadj):
        entry = {
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            "pair": pair,
            "timeframe": timeframe,
            "conf12": conf12,
            "rcadj": rcadj,
        }
        self.memory["sessions"].append(entry)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2)

    def last_context(self):
        return self.memory["sessions"][-1] if self.memory["sessions"] else None
