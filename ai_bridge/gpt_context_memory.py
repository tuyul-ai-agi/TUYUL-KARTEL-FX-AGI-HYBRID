"""
GPT Context Memory v5.4.0
-------------------------
Simpan dan ambil memori reasoning GPT antar sesi.
"""

import json
import os
from datetime import datetime


class ContextMemory:
    def __init__(self, file_path="vaults/journal_vault/context_memory.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def save(self, role, prompt, result):
        memory_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "role": role,
            "prompt": prompt,
            "result": result,
        }
        data = self.load()
        data.append(memory_entry)
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def clear(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)
