# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Quad Repo Sync Handler
# ------------------------------------------------------------
# Versi ringan non-loop dari Quad Repo Sync.
# Dipanggil manual oleh BOT–TJX atau Reflective Meta Cycle
# saat integritas sistem < 0.9.
#
# Bridge Protocol : RBP_v2.2
# BOT Handler     : TUYULBOT–TJX
# ============================================================

import os
import json
from datetime import datetime
from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    vaultSync,
    getIntegrityFeedback,
)

OUTPUT_FILE = "journal_repo/quad_repo_sync.json"
LOG_FILE = "logs/quad_repo_sync_handler.log"


# ============================================================
# 🧠 HANDLER UTAMA
# ============================================================

def run_quad_repo_sync():
    """Menjalankan sinkronisasi reflektif satu kali antar empat repo."""
    print("🔁 Running Quad Repo Sync Handler (RBP_v2.2)...")

    sync_data = vaultSync()
    integrity = getIntegrityFeedback()

    data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "hybrid_to_knowledge": "Synced",
        "knowledge_to_kartel": "Synced",
        "kartel_to_journal": "Synced",
        "hybrid_to_repo": sync_data.get("hybrid_to_vault", "Synced"),
        "repo_to_journal": sync_data.get("vault_to_journal", "Synced"),
        "latency_ms": sync_data.get("latency_ms", 0),
        "integrity_index": round(integrity.get("integrity_index", 0.9), 3),
        "coherence_drift": integrity.get("coherence_drift", "Stable"),
        "regime_adaptation": integrity.get("regime_adaptation", "Normal"),
        "reflection_score": round(integrity.get("reflection_score", 0.9), 3),
        "reflective_bridge": "RBP_v2.2",
        "bot": "TUYULBOT-TJX",
        "status": "Manual Trigger",
    }

    _save_sync_data(data)
    _log_sync(data)

    print(
        "✅ Quad Repo Sync (Manual) selesai — "
        f"Integrity={data['integrity_index']} | Drift={data['coherence_drift']}"
    )
    return data


# ============================================================
# 💾 PENYIMPANAN & LOGGING
# ============================================================

def _save_sync_data(data: dict):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"🧾 Sync report disimpan → {OUTPUT_FILE}")


def _log_sync(data: dict):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{data['timestamp']}] Integrity={data['integrity_index']} | "
            f"Drift={data['coherence_drift']} | "
            f"Latency={data['latency_ms']}ms | Reflection={data['reflection_score']}\n"
        )


# ============================================================
# 🚀 DEMO EKSEKUSI
# ============================================================

if __name__ == "__main__":
    run_quad_repo_sync()
