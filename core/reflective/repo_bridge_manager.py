# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.2-HYBRID+
# Reflective Repo Bridge Manager — Quad Repo Feedback Engine
# ============================================================

import os
import json
import time
from datetime import datetime
import requests

SYNC_LOG = "journal_repo/logs/sync_audit.json"
REFLECTIVE_LOG = "logs/reflective_bridge.log"

REPO_ENDPOINTS = {
    "knowledge": "https://api.github.com/repos/tuyulfx/knowledge_vault_agi/dispatches",
    "kartel": "https://api.github.com/repos/tuyulfx/kartel_macro_vault/dispatches",
    "journal": "https://api.github.com/repos/tuyulfx/journal_vault_agi/dispatches",
}

def log_event(message: str):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"[{timestamp}] [RepoBridge] {message}"
    print(entry)
    os.makedirs(os.path.dirname(REFLECTIVE_LOG), exist_ok=True)
    with open(REFLECTIVE_LOG, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def read_sync_log():
    if not os.path.exists(SYNC_LOG):
        log_event("⚠️ Tidak ditemukan file sync_audit.json.")
        return None
    with open(SYNC_LOG, "r", encoding="utf-8") as f:
        return json.load(f)


def dispatch_event(repo: str, event_type: str, token: str):
    """Mengirim event reflektif ke repositori target melalui GitHub API."""
    try:
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
        }
        payload = {"event_type": event_type}
        r = requests.post(REPO_ENDPOINTS[repo], headers=headers, json=payload)
        if r.status_code == 204:
            log_event(f"✅ Dispatch sukses → {repo.upper()} ({event_type})")
        else:
            log_event(f"⚠️ Dispatch gagal ke {repo.upper()}: {r.status_code} {r.text}")
    except Exception as e:
        log_event(f"❌ Error dispatch ke {repo.upper()}: {e}")


def reflective_feedback(token: str):
    """Menganalisa hasil sync & mengirim feedback reflektif."""
    sync_data = read_sync_log()
    if not sync_data:
        log_event("❌ Tidak ada data sinkronisasi untuk refleksi.")
        return

    integrity = sync_data.get("integrity_index", 0)
    state = sync_data.get("state", "Unknown")
    log_event(f"🧠 Integrity Index: {integrity} | State: {state}")

    # Adaptive feedback rules
    if integrity >= 0.9:
        log_event("🟢 Sistem stabil — mengirim update ringan (meta-learning sync).")
        dispatch_event("knowledge", "reflective_update", token)
        dispatch_event("journal", "reflective_log_commit", token)

    elif 0.75 <= integrity < 0.9:
        log_event("🟡 Stabilitas moderat — trigger coherence reinforcement.")
        dispatch_event("kartel", "macro_coherence_update", token)
        dispatch_event("knowledge", "reflective_update", token)
        dispatch_event("journal", "reflective_log_commit", token)

    else:
        log_event("🔴 Ketidakseimbangan terdeteksi — memicu auto-correction BOT.")
        dispatch_event("knowledge", "stability_alert", token)
        dispatch_event("kartel", "macro_drift_detected", token)
        dispatch_event("journal", "reflective_alert_log", token)

    # Simpan ringkasan reflektif ke Journal Vault
    feedback_summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "integrity_index": integrity,
        "system_state": state,
        "actions": {
            "knowledge": "update" if integrity >= 0.75 else "alert",
            "kartel": "reinforce" if integrity >= 0.75 else "stabilize",
            "journal": "log_commit",
        },
    }

    os.makedirs(os.path.dirname(SYNC_LOG), exist_ok=True)
    with open("journal_repo/logs/reflective_feedback.json", "w", encoding="utf-8") as f:
        json.dump(feedback_summary, f, indent=4)

    log_event("🧾 Reflektif feedback disimpan ke journal_repo/logs/reflective_feedback.json")


def main():
    token = os.getenv("GH_TOKEN") or os.getenv("HYBRID_REPO_TOKEN")
    if not token:
        log_event("❌ Token GitHub tidak ditemukan. Set GH_TOKEN di environment.")
        return

    log_event("🚀 Menjalankan Reflective Repo Bridge Manager...")
    reflective_feedback(token)
    log_event("✅ Siklus reflektif lintas repo selesai.")


if __name__ == "__main__":
    main()
