"""
Vault Adapter v6.0
-----------------------------------------
Connects the reflective chat system with TUYUL Vault Repos (FX, Kartel, Journal).
Allows read/write reflective dialogue logs.
"""

import json
from datetime import datetime
from pathlib import Path

class VaultAdapter:
    def __init__(self, vault_path="reflective_repos/journal_repo/chat_log.json"):
        self.path = Path(vault_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]")

    def save_message(self, user, message):
        logs = json.loads(self.path.read_text())
        logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "message": message
        })
        self.path.write_text(json.dumps(logs, indent=2))

    def read_recent(self, limit=5):
        logs = json.loads(self.path.read_text())
        return logs[-limit:]
