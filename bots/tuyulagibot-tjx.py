# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.2-HYBRID+
# BOT ORCHESTRATOR — tuyulagibot-tjx.py
# ============================================================
# Fungsi:
#  - Mengelola siklus penuh Quad Repo System
#  - Menjalankan Reflective Feedback dan Bridge Manager
#  - Memantau latency antar repo
#  - Menjalankan corrective cycle otomatis
# ============================================================

import os
import time
import json
import subprocess
import requests
from datetime import datetime

CONFIG_FILE = "configs/repo_map.yml"
LOG_FILE = "logs/tuyulagibot.log"
SYNC_AUDIT_FILE = "journal_repo/logs/sync_audit.json"
REFLECTIVE_FEEDBACK_FILE = "journal_repo/logs/reflective_feedback.json"

# ============================================================
# LOGGING SYSTEM
# ============================================================

def log_event(message: str):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"[{timestamp}] [TUYULBOT] {message}"
    print(entry)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

# ============================================================
# BOT CORE FUNCTIONALITY
# ============================================================

def run_quad_repo_sync():
    """Menjalankan sinkronisasi lintas 4 repo TUYUL."""
    log_event("🚀 Menjalankan Quad Repo Sync System...")
    try:
        subprocess.run(["python3", "tools/quad_repo_sync.py"], check=True)
        log_event("✅ Quad Repo Sync selesai tanpa error.")
    except subprocess.CalledProcessError as e:
        log_event(f"❌ Gagal menjalankan Quad Repo Sync: {e}")


def run_reflective_bridge():
    """Menjalankan Reflective Feedback antar repo."""
    log_event("🔄 Menjalankan Reflective Bridge Manager...")
    try:
        subprocess.run(["python3", "reflective/repo_bridge_manager.py"], check=True)
        log_event("✅ Reflective Bridge berhasil dijalankan.")
    except subprocess.CalledProcessError as e:
        log_event(f"❌ Gagal menjalankan Reflective Bridge: {e}")


def check_system_integrity():
    """Mengevaluasi hasil sinkronisasi terakhir (ICI dan status repo)."""
    if not os.path.exists(SYNC_AUDIT_FILE):
        log_event("⚠️ File sync_audit.json tidak ditemukan.")
        return 0.0

    with open(SYNC_AUDIT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    ici = data.get("integrity_index", 0)
    state = data.get("state", "Unknown")
    log_event(f"🧠 Integrity Coherence Index (ICI): {ici} | State: {state}")
    return ici


def check_latency():
    """Mengecek waktu respon antar repo (simulasi latency check)."""
    log_event("📡 Mengecek latency antar repo...")
    repo_urls = [
        "https://github.com/tuyulfx/agi_hybrid_tools",
        "https://github.com/tuyulfx/knowledge_vault_agi",
        "https://github.com/tuyulfx/kartel_macro_vault",
        "https://github.com/tuyulfx/journal_vault_agi",
    ]

    latencies = {}
    for url in repo_urls:
        start = time.time()
        try:
            requests.get(url, timeout=3)
            latency = round((time.time() - start) * 1000, 2)
            latencies[url] = latency
            log_event(f"🌐 {url} → {latency} ms")
        except Exception:
            latencies[url] = None
            log_event(f"⚠️ Timeout pada {url}")
    return latencies


def reflective_auto_correction(ici: float):
    """Menjalankan koreksi reflektif otomatis jika integritas < 0.85"""
    if ici < 0.85:
        log_event("🔴 Integritas rendah — menjalankan auto-correction cycle.")
        subprocess.run(["python3", "reflective/repo_bridge_manager.py"], check=False)
        time.sleep(2)
        subprocess.run(["python3", "tools/quad_repo_sync.py"], check=False)
        log_event("🧩 Reflective auto-correction selesai.")
    else:
        log_event("🟢 Sistem dalam keadaan stabil, tidak perlu koreksi.")


def summary_report(ici, latencies):
    """Menyimpan laporan status BOT."""
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "integrity_index": ici,
        "latencies_ms": latencies,
        "status": "Stable" if ici >= 0.85 else "Degraded",
    }
    with open("logs/tuyulagibot_summary.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    log_event("🧾 Laporan BOT disimpan ke logs/tuyulagibot_summary.json")

# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    log_event("🐺 Memulai TUYUL FX BOT Orchestrator v5.7.2-HYBRID+ ...")

    ici = 0
    latencies = {}

    # Step 1: Jalankan sinkronisasi repo
    run_quad_repo_sync()

    # Step 2: Cek integritas sistem
    ici = check_system_integrity()

    # Step 3: Jalankan Reflective Feedback Loop
    run_reflective_bridge()

    # Step 4: Periksa latency antar repo
    latencies = check_latency()

    # Step 5: Jalankan auto-correction jika perlu
    reflective_auto_correction(ici)

    # Step 6: Simpan laporan BOT
    summary_report(ici, latencies)

    log_event("✅ TUYULBOT selesai menjalankan siklus penuh.\n")


if __name__ == "__main__":
    main()
