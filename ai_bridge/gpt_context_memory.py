"""
Reflective Context Memory v6.0
-----------------------------------------
Stores and retrieves reflective context sequences for multi-layer reasoning.
"""

import json
from datetime import datetime
from pathlib import Path


class GPTContextMemory:
    def __init__(self, path: str = "logs/gpt_context_memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.save([])

    def load(self):
        return json.loads(self.path.read_text())

    def save(self, data):
        self.path.write_text(json.dumps(data, indent=2))

    def append(self, reflection: str):
        memory = self.load()
        memory.append({
            "timestamp": datetime.utcnow().isoformat(),
            "reflection": reflection,
        })
        self.save(memory)"""
GPT Context Memory v5.7.3r++
----------------------------
Menyimpan konteks percakapan reflektif GPT dan meta-learning.
"""

import json
from datetime import datetime

CONTEXT_FILE = "knowledge/context_memory.json"


def store_context(user_input: str, model_output: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": user_input,
        "output": model_output,
        "context_version": "v5.7.3r++"
    }
    with open(CONTEXT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print("[MEMORY] Context stored.")


def load_context(limit=10):
    try:
        with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
        return [json.loads(line) for line in lines]
    except FileNotFoundError:
        return []
