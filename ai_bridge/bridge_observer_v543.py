"""
Bridge Observer v5.4.3
----------------------
Monitoring aktivitas GPT Bridge, Vault Sync, dan GitHub Hooks.
"""

import os
from datetime import datetime


class BridgeObserver:
    def __init__(self, log_file="logs/bridge_events.log"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def log_event(self, source, action, status, details=""):
        entry = f"[{datetime.utcnow().isoformat()}] [{source}] {action} -> {status} | {details}\n"
        with open(self.log_file, "a") as f:
            f.write(entry)
        print(entry.strip())

    def log_error(self, source, error):
        self.log_event(source, "ERROR", "FAILED", str(error))
