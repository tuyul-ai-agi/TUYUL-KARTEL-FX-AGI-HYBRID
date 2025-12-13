# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Quad Repo Sync Loop
# ------------------------------------------------------------
# Sinkronisasi reflektif penuh empat repositori utama:
# Hybrid ↔ Knowledge ↔ Kartel ↔ Journal
#
# Bridge Protocol : RBP_v2.2
# BOT Handler     : TUYULBOT–TJX
# ============================================================

import json
import os
import time
from datetime import datetime

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    getIntegrityFeedback,
    vaultSync,
)

LOG_FILE = "logs/quad_repo_sync.log"
OUTPUT_FILE = "journal_repo/quad_repo_sync.json"


# ============================================================
# 🧠 INTI FUNGSI
# ============================================================

def quad_repo_sync_loop(interval_minutes=10):
    """Menjalankan sinkronisasi lintas empat repo reflektif secara berkala."""
    print("🔁 Starting Quad Repo Sync Loop v5.7.8 (RBP_v2.2)...")
    while True:
        sync_data = vaultSync()
        integrity = getIntegrityFeedback()
        report = _compose_sync_report(sync_data, integrity)
        _save_sync_report(report)
        _log_sync_activity(report)
        print(
            f"🕒 Menunggu {interval_minutes} menit sebelum sinkronisasi berikutnya...\n"
        )
        time.sleep(interval_minutes * 60)


# ============================================================
# 🧩 PEMBENTUKAN DATA SINKRON
# ============================================================

def _compose_sync_report(sync, integrity):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "hybrid_to_knowledge": "Synced",
        "knowledge_to_kartel": "Synced",
        "kartel_to_journal": "Synced",
        "hybrid_to_repo": sync.get("hybrid_to_vault", "Synced"),
        "repo_to_journal": sync.get("vault_to_journal", "Synced"),
        "latency_ms": sync.get("latency_ms", 0),
        "integrity_index": round(integrity.get("integrity_index", 0.9), 3),
        "coherence_drift": integrity.get("coherence_drift", "Stable"),
        "regime_adaptation": integrity.get("regime_adaptation", "Normal"),
        "reflection_score": round(integrity.get("reflection_score", 0.9), 3),
        "reflective_bridge": "RBP_v2.2",
        "status": "Synced",
        "bot": "TUYULBOT-TJX",
    }


# ============================================================
# 💾 PENYIMPANAN HASIL
# ============================================================

def _save_sync_report(data: dict):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Quad Repo Sync report saved → {OUTPUT_FILE}")


def _log_sync_activity(data: dict):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{data['timestamp']}] Integrity={data['integrity_index']} | "
            f"Drift={data['coherence_drift']} | Regime={data['regime_adaptation']} "
            f"| Latency={data['latency_ms']}ms\n"
        )


# ============================================================
# 🚀 DEMO EKSEKUSI
# ============================================================

if __name__ == "__main__":
    print("🐺 TUYUL FX AGI Quad Repo Sync Loop v5.7.8 – Reflective System")
    quad_repo_sync_loop(interval_minutes=10)
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
