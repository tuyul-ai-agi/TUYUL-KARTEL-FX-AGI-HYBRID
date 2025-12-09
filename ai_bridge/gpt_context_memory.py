"""
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
