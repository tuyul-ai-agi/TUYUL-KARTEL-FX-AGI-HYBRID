"""
Client AGI Hybrid — Journal Writer v5.7.3r++
--------------------------------------------
Menulis hasil reasoning dan simulasi ke Journal Vault (JSON)
dengan awareness Monte Carlo v2.2 (20k/90d).
"""

import json
import os
from datetime import datetime


class JournalVaultClient:
    def __init__(self, path="vaults/journal_vault/reflective_log.json"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def write_entry(self, pair: str, mc_result: dict, fusion_conf: float, rcadj: float):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "pair": pair,
            "fusion_confidence": fusion_conf,
            "rcadj": rcadj,
            "monte_carlo_confidence": mc_result["confidence"],
            "monte_carlo_spec": mc_result["spec"],
            "reflective_bridge_version": "RBP v2.2",
            "version": "v5.7.3r++"
        }
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(json.dumps(entry) + "\n")
        print(f"[LOG] Journal updated → {self.path}")
        return entry
