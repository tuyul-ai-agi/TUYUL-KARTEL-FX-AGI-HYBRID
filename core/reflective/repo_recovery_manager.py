# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.2-HYBRID+
# Reflective Repo Recovery Manager — Auto-Heal & Resync System
# ============================================================
# Fungsi:
# - Mendeteksi repo yang mengalami drift atau timeout
# - Menjalankan auto-resync antar repo
# - Memulihkan state dari Journal backup
# - Menjalankan BOT reflektif untuk self-healing
# ============================================================

import os
import json
import time
import subprocess
import requests
from datetime import datetime

HEALTH_FILE = "logs/repo_health_report.json"
LOG_FILE = "logs/repo_recovery.log"
RECOVERY_REPORT = "logs/repo_recovery_summary.json"

REPO_API = {
    "hybrid": "https://api.github.com/repos/tuyulfx/agi_hybrid_tools/dispatches",
    "knowledge": "https://api.github.com/repos/tuyulfx/knowledge_vault_agi/dispatches",
    "kartel": "https://api.github.com/repos/tuyulfx/kartel_macro_vault/dispatches",
    "journal": "https://api.github.com/repos/tuyulfx/journal_vault_agi/dispatches"
}


def log_event(msg: str):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [RecoveryManager] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_health_report():
    if not os.path.exists(HEALTH_FILE):
        log_event("⚠️ Tidak ditemukan health report.")
        return None
    with open(HEALTH_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def trigger_repo_resync(repo: str, event_type: str, token: str):
    """Mengirim event dispatch ke repo target untuk re-sync"""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    payload = {"event_type": event_type}
    try:
        r = requests.post(REPO_API[repo], headers=headers, json=payload)
        if r.status_code == 204:
            log_event(f"✅ Resync trigger sukses untuk {repo.upper()} ({event_type})")
            return True
        else:
            log_event(f"⚠️ Resync gagal ke {repo.upper()}: {r.status_code}")
            return False
    except Exception as e:
        log_event(f"❌ Gagal trigger resync {repo.upper()}: {e}")
        return False


def restore_from_journal_backup():
    """Memulihkan data dari backup Journal jika repo tidak merespons"""
    journal_backup = "journal_repo/logs/reflective_feedback.json"
    if not os.path.exists(journal_backup):
        log_event("⚠️ Tidak ada backup Journal untuk pemulihan.")
        return None

    with open(journal_backup, "r", encoding="utf-8") as f:
        data = json.load(f)

    log_event(f"💾 Memulihkan state dari Journal backup ({journal_backup})")
    return data


def run_bot_autoheal():
    """Menjalankan BOT reflektif (tuyulagibot-tjx) untuk koreksi otomatis"""
    log_event("🤖 Menjalankan BOT TUYULAGIBOT-TJX untuk siklus auto-heal...")
    try:
        subprocess.run(["python3", "bots/tuyulagibot-tjx.py"], check=False)
        log_event("✅ BOT auto-heal selesai dijalankan.")
    except Exception as e:
        log_event(f"❌ BOT gagal dijalankan: {e}")


def execute_recovery(token: str):
    """Proses utama: membaca health report, memutuskan langkah recovery"""
    report = load_health_report()
    if not report:
        log_event("❌ Tidak ada health report untuk recovery.")
        return

    state = report.get("system_state", "UNKNOWN")
    latencies = report.get("details", {}).get("latencies", {})
    drifts = report.get("details", {}).get("drifts", {})

    degraded_repos = [r for r, v in latencies.items() if v.get("status") != "OK" or (drifts.get(r, 0) or 0) > 10]

    log_event(f"🧩 Repo dalam status menurun: {degraded_repos or 'Tidak ada'}")

    recovery_actions = {}
    for repo in degraded_repos:
        success = trigger_repo_resync(repo, "reflective_resync", token)
        recovery_actions[repo] = "resync_triggered" if success else "failed"

    # Jika semua gagal → gunakan backup Journal
    if all(v == "failed" for v in recovery_actions.values()) and degraded_repos:
        backup = restore_from_journal_backup()
        if backup:
            log_event("🧠 State sistem sementara dipulihkan dari Journal backup.")
            recovery_actions["journal_restore"] = "success"

    # Jalankan BOT auto-heal
    run_bot_autoheal()

    # Buat laporan hasil recovery
    recovery_report = {
        "timestamp": datetime.utcnow().isoformat(),
        "system_state": state,
        "recovery_actions": recovery_actions,
        "affected_repos": degraded_repos,
        "journal_used": "journal_restore" in recovery_actions
    }

    os.makedirs(os.path.dirname(RECOVERY_REPORT), exist_ok=True)
    with open(RECOVERY_REPORT, "w", encoding="utf-8") as f:
        json.dump(recovery_report, f, indent=4)

    log_event("🧾 Laporan recovery disimpan ke logs/repo_recovery_summary.json")
    return recovery_report


def main():
    log_event("🐺 Menjalankan Reflective Repo Recovery Manager v5.7.2+ ...")
    token = os.getenv("GH_TOKEN") or os.getenv("HYBRID_REPO_TOKEN")

    if not token:
        log_event("❌ GH_TOKEN tidak ditemukan. Recovery dibatalkan.")
        return

    execute_recovery(token)
    log_event("✅ Reflective recovery cycle selesai.\n")


if __name__ == "__main__":
    main()
