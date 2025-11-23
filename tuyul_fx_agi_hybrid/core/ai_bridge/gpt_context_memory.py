import json
from datetime import datetime


class GPTContextMemory:
    def __init__(self, path="vaults/context_memory.json"):
        self.path = path
        self.memory = self._load_memory()

    def _load_memory(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"sessions": []}

    def save_context(self, pair, timeframe, conf12, rcadj):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "pair": pair,
            "timeframe": timeframe,
            "conf12": conf12,
            "rcadj": rcadj,
        }
        self.memory["sessions"].append(entry)
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def last_context(self):
        return self.memory["sessions"][-1] if self.memory["sessions"] else None
