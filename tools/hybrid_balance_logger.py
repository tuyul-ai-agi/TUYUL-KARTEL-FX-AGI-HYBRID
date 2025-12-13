# ============================================================
# 🧾 TUYUL FX AGI v5.7.8 — Hybrid Balance Logger
# ------------------------------------------------------------
# Mencatat hasil reflektif keseimbangan sistem dari controller.
# Ditulis ke Journal Repo dan diintegrasikan dengan BOT-TJX.
# ============================================================

import json
import os
from datetime import datetime

SOURCE_FILE = "journal_repo/logs/hybrid_balance_feedback.json"
LOG_ARCHIVE = "journal_repo/logs/balance_audit.json"


def log_reflective_balance():
    """Menyalin hasil dari controller ke arsip audit reflektif."""

    if not os.path.exists(SOURCE_FILE):
        print("⚠️ Tidak ditemukan file balance feedback. Pastikan controller sudah dijalankan.")
        return

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "balance_state": data.get("balance_state", "Unknown"),
        "integrity_index": data.get("integrity_index", 0.0),
        "coherence_balance": data.get("coherence_balance", 0.0),
        "drawdown_delta": data.get("drawdown_delta", 0.0),
        "sync_status": data.get("reflective_sync", "pending"),
        "bot": "TUYULBOT-TJX",
    }

    os.makedirs(os.path.dirname(LOG_ARCHIVE), exist_ok=True)
    if not os.path.exists(LOG_ARCHIVE):
        with open(LOG_ARCHIVE, "w", encoding="utf-8") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(LOG_ARCHIVE, "r", encoding="utf-8") as f:
            logs = json.load(f)
        logs.append(entry)
        with open(LOG_ARCHIVE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)

    print(f"🧾 Balance log updated → {entry['balance_state']} @ {entry['timestamp']}")


if __name__ == "__main__":
    print("🐺 TUYUL FX Hybrid Balance Logger v5.7.8")
    log_reflective_balance()
