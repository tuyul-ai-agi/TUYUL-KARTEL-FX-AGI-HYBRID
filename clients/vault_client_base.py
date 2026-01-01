"""
Vault Client Base v6.0
-----------------------------------------
Base class for reflective vault communication clients.
Provides safe read/write and coherence logging.
"""

import json, os
from datetime import datetime
from pathlib import Path

class VaultClientBase:
    def __init__(self, vault_path, name):
        self.vault_path = Path(vault_path)
        self.name = name
        self.vault_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.vault_path.exists():
            self.vault_path.write_text("[]")

    def read(self):
        try:
            return json.loads(self.vault_path.read_text())
        except Exception as e:
            return {"error": str(e)}

    def write(self, data):
        self.vault_path.write_text(json.dumps(data, indent=2))
        return {"status": "written", "vault": self.name}

    def log_action(self, message):
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_path = log_dir / f"{self.name}_actions.log"
        log_path.write_text(f"[{datetime.utcnow()}] {message}\n", append=True)
