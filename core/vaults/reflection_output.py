"""
Reflection Output Writer
------------------------
Menulis hasil reasoning reflektif ke Vault output JSON.
"""

import json
import os
from datetime import datetime

class ReflectionOutput:
    def __init__(self, vault_path="vaults/journal_vault/reflection_output.json"):
        self.vault_path = vault_path
        os.makedirs(os.path.dirname(self.vault_path), exist_ok=True)

    def write(self, reflection_data: dict):
        reflection_data["timestamp"] = datetime.utcnow().isoformat()
        with open(self.vault_path, "w") as f:
            json.dump(reflection_data, f, indent=2)
        return {"status": "written", "path": self.vault_path}

    def read(self):
        if not os.path.exists(self.vault_path):
            return {"error": "Reflection file not found"}
        with open(self.vault_path) as f:
            return json.load(f)
