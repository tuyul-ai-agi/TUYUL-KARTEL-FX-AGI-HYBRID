"""
Reflective Cycle Core — TUYUL FX AGI HYBRID v5.7.3r++
Menjalankan siklus reflektif penuh (Bridge → Reason → Sync → Vault).
"""

import datetime
import json
import os

from .reflective_live_bridge import ReflectiveLiveBridge
from .reflective_reasoner import ReflectiveReasoner
from .reflective_mcp_handler import ReflectiveMCPHandler
from .reflective_sync import ReflectiveSync


class ReflectiveCycleCore:
    """Menjalankan siklus reflektif penuh (Bridge → Reason → Sync → Vault)."""

    def __init__(self):
        self.bridge = ReflectiveLiveBridge()
        self.reasoner = ReflectiveReasoner()
        self.mcp = ReflectiveMCPHandler()
        self.sync = ReflectiveSync()
        self.log_path = "journal/reflective_cycle_core.json"

    def execute(self):
        bridge_status = self.bridge.ping_all()
        reasoning = self.reasoner.evaluate_cycle()
        meta = self.mcp.reflective_compute(bridge_status, reasoning)
        sync_result = self.sync.run_sync(meta)

        result = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "fusion_confidence": reasoning["fusion_confidence"],
            "wlwci": reasoning["wlwci"],
            "rcadj": reasoning["rcadj"],
            "integrity_index": meta["integrity_index"],
            "reflective_state": meta["reflective_state"],
            "sync_integrity": sync_result["sync_integrity"],
            "reflective_sync": "completed",
        }

        os.makedirs("journal", exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(result) + "\n")

        print(
            "🔁 Reflective Cycle — State:"
            f" {result['reflective_state']} | Sync Integrity: {result['sync_integrity']}"
        )
        return result
