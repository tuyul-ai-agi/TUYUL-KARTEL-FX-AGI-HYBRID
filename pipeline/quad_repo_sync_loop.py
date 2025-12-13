"""Quad Repo Sync Loop
----------------------
Sinkronisasi reflektif empat repo melalui Reflective Bridge Protocol v2.2.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Dict, Optional

from core.repo.repo_bridge_manager import RepoBridgeManager

LOG_FILE = "logs/quad_repo_sync.log"
JOURNAL_FILE = "journal_repo/quad_repo_sync.json"


class QuadRepoSyncLoop:
    def __init__(self, bridge_manager: Optional[RepoBridgeManager] = None):
        self.bridge_manager = bridge_manager or RepoBridgeManager()

    def run(self) -> Dict[str, object]:
        sync_result = self.bridge_manager.sync_repos()
        integrity_report = self._build_integrity_report(sync_result)
        self._persist(sync_result, integrity_report)
        return {"quad_repo_bridge": sync_result, "integrity": integrity_report}

    def _build_integrity_report(self, sync_result: Dict[str, object]) -> Dict[str, object]:
        coherence_drift = round(max(0.0, 1 - float(sync_result["integrity_index"])), 3)
        reflection_score = round(min(1.0, float(sync_result["wlwci"]) + 0.03), 3)
        regime_adaptation = (
            "stable" if float(sync_result["integrity_index"]) >= 0.92 else "recovering"
        )

        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "integrity_index": sync_result["integrity_index"],
            "wlwci": sync_result["wlwci"],
            "coherence_drift": coherence_drift,
            "reflection_score": reflection_score,
            "regime_adaptation": regime_adaptation,
        }

    def _persist(self, sync_result: Dict[str, object], integrity_report: Dict[str, object]) -> None:
        os.makedirs(os.path.dirname(JOURNAL_FILE), exist_ok=True)
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

        payload = {
            "timestamp": integrity_report["timestamp"],
            "hybrid_to_knowledge": "synced",
            "knowledge_to_kartel": "synced",
            "kartel_to_journal": "synced",
            "latency_ms": sync_result["latency_ms"],
            "integrity_index": integrity_report["integrity_index"],
            "coherence_drift": integrity_report["coherence_drift"],
            "reflection_score": integrity_report["reflection_score"],
            "regime_adaptation": integrity_report["regime_adaptation"],
            "wlwci": integrity_report["wlwci"],
            "bridge_state": sync_result["bridge_state"],
            "vaults": sync_result["vaults"],
        }

        with open(JOURNAL_FILE, "w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2)

        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(
                f"[{payload['timestamp']}] "
                f"Integrity={payload['integrity_index']} | "
                f"Drift={payload['coherence_drift']} | "
                f"Latency={payload['latency_ms']}ms | "
                f"Regime={payload['regime_adaptation']}\n"
            )

        print(f"✅ Quad Repo Sync saved → {JOURNAL_FILE}")


# Backward compatibility for legacy callers
TriRepoSyncLoop = QuadRepoSyncLoop
TriVaultSyncLoop = QuadRepoSyncLoop
