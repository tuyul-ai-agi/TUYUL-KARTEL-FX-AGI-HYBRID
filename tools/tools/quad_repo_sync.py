# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.2-HYBRID+
# Quad Repo Sync Engine — Reflex–Fusion–Reflective–VIX Hybrid+
# ============================================================

import os
import json
import subprocess
from datetime import datetime
import yaml

CONFIG_PATH = "configs/repo_map.yml"
LOG_FILE = "logs/bridge_events.log"
SYNC_AUDIT_FILE = "journal_repo/logs/sync_audit.json"


def log_event(message: str):
    """Menulis log ke file dan tampilkan di console."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"[{timestamp}] [QuadRepoSync] {message}"
    print(entry)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def read_repo_map():
    """Membaca daftar repositori dari configs/repo_map.yml"""
    if not os.path.exists(CONFIG_PATH):
        log_event("⚠️ File repo_map.yml tidak ditemukan.")
        return {}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def git_pull(repo_path: str):
    """Menarik pembaruan dari repo target."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "pull", "origin", "main"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            log_event(f"✅ Repo {repo_path} berhasil di-sync.")
            return True
        else:
            log_event(f"⚠️ Gagal sync repo {repo_path}: {result.stderr}")
            return False
    except Exception as e:
        log_event(f"❌ Error saat sync {repo_path}: {e}")
        return False


def sync_all_repos(repo_map):
    """Menjalankan sinkronisasi untuk semua repo yang terdaftar."""
    sync_results = {}
    for name, data in repo_map.get("repos", {}).items():
        repo_path = data.get("path", f"{name}_repo")
        log_event(f"🔁 Menyinkronkan {name.upper()} ({repo_path}) ...")
        status = git_pull(repo_path)
        sync_results[name] = {"status": "OK" if status else "FAILED"}
    return sync_results


def evaluate_integrity(sync_results):
    """Menilai hasil sinkronisasi untuk membuat integritas laporan."""
    success = sum(1 for s in sync_results.values() if s["status"] == "OK")
    total = len(sync_results)
    integrity = round(success / max(total, 1), 3)
    state = "Stable" if integrity >= 0.85 else "Degraded"
    return integrity, state


def write_audit_report(sync_results, integrity, state):
    """Menyimpan hasil audit sinkronisasi ke JSON."""
    os.makedirs(os.path.dirname(SYNC_AUDIT_FILE), exist_ok=True)
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "integrity_index": integrity,
        "state": state,
        "sync_results": sync_results,
    }
    with open(SYNC_AUDIT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    log_event(f"🧠 Sync Integrity Index: {integrity} ({state})")
    log_event(f"📦 Hasil audit disimpan ke {SYNC_AUDIT_FILE}")


def main():
    log_event("🚀 Menjalankan TUYUL Quad Repo Sync Engine...")
    repo_map = read_repo_map()
    if not repo_map:
        log_event("❌ Tidak ada konfigurasi repo yang ditemukan. Sync dibatalkan.")
        return

    results = sync_all_repos(repo_map)
    integrity, state = evaluate_integrity(results)
    write_audit_report(results, integrity, state)

    if state == "Degraded":
        log_event("⚠️ Integritas di bawah ambang aman. Memicu Reflective Bridge...")
        os.system("python3 reflective/repo_bridge_manager.py")

    log_event("✅ Quad Repo Sync selesai tanpa error mayor.")


if __name__ == "__main__":
    main()
