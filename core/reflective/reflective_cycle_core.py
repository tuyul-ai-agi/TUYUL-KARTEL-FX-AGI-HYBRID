"""Reflective Cycle Core — TUYUL FX AGI HYBRID v5.7.3r++"""
import datetime
import json
import os

from .reflective_live_bridge import ReflectiveLiveBridge
from .reflective_mcp_handler import ReflectiveMCPHandler
from .reflective_reasoner import ReflectiveReasoner


class ReflectiveCycleCore:
    """Menjalankan siklus inti reflektif: bridge → reasoning → synchronization."""

    def __init__(self):
        self.bridge = ReflectiveLiveBridge()
        self.reasoner = ReflectiveReasoner()
        self.mcp = ReflectiveMCPHandler()
        self.log_path = "journal/reflective_cycle_core_log.json"

    def execute(self):
        """Jalankan full meta-cycle reflektif dan tulis log hasil sinkronisasi."""
        bridge_status = self.bridge.ping_all()
        reasoning = self.reasoner.evaluate_cycle()
        meta_core = self.mcp.reflective_compute(bridge_status, reasoning)

        result = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "fusion_confidence": reasoning["fusion_confidence"],
            "wlwci": reasoning["wlwci"],
            "rcadj": reasoning["rcadj"],
            "integrity_index": meta_core["integrity_index"],
            "reflective_state": meta_core["reflective_state"],
            "reflective_sync": "complete",
        }

        os.makedirs("journal", exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(result) + "\n")

        print(
            "🔁 Reflective Core Cycle — State: {state} | Integrity: {integrity}".format(
                state=result["reflective_state"], integrity=result["integrity_index"]
            )
        )
        return result
