"""
🐺 TUYUL FX ULTRA WOLF v5.4.1-HYBRID
Vault AutoSync Engine — Full Remote Commit Integration
=======================================================

Fungsi:
- Melakukan sinkronisasi otomatis antar repo TUYUL AGI (Hybrid, Knowledge, Journal)
- Menjalankan verifikasi SHA256 sebelum push
- Menyimpan delta history (5 versi terakhir)
- Membuat pull request otomatis di GitHub jika ada perubahan
"""

import os
import json
import hashlib
import datetime
from pathlib import Path

# ====================== 🔧 KONFIGURASI REPO ==========================
REMOTE_SYNC = True   # aktifkan untuk push ke GitHub
REPO_HYBRID = "tjx578/tuyul-kartel-fx-agi-hybrid"
REPO_KNOWLEDGE = "tjx578/TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI"
REPO_JOURNAL = "tjx578/TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI"

SYNC_BASE = Path("/mnt/data")
LOG_PATH = SYNC_BASE / "journal/logs/vault_sync_meta.json"
HISTORY_PATH = SYNC_BASE / "history"

# ====================== ⚙️ SYNC RULES ================================
SYNC_RULES = {
    ".py": {"repo": REPO_HYBRID, "target": "tuyul_fx_agi_hybrid/core/"},
    ".md": {"repo": REPO_KNOWLEDGE, "target": "knowledge_base/modules/"},
    ".yaml": {"repo": REPO_KNOWLEDGE, "target": "knowledge_base/_index/"},
    ".json": {"repo": REPO_JOURNAL, "target": "data/"},
}

# ====================== 🧩 IMPOR MODUL LAIN =========================
from tuyul_fx_agi_hybrid.core.bridge.vault_delta_history_v541 import (
    update_delta_history,
    rollback_module,
)

try:
    from api_github_com__jit_plugin import githubCommitFile, triggerRuntimeReload
except ImportError:
    githubCommitFile = None
    triggerRuntimeReload = None


# ====================== 🔐 HASH & VERIFIKASI ========================
def compute_sha256(file_path: Path) -> str:
    """Hitung hash SHA256 dari file"""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def verify_file_integrity(file_path: Path, ref_hash: str = None) -> bool:
    """Verifikasi file menggunakan hash"""
    if not file_path.exists():
        print(f"❌ File hilang: {file_path}")
        return False
    new_hash = compute_sha256(file_path)
    if ref_hash and new_hash != ref_hash:
        print(f"⚠️ Hash mismatch pada {file_path.name}")
        return False
    return True


# ====================== 📘 LOGGING FUNKSI ============================
def log_event(event: str, status: str = "info"):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event,
        "status": status,
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[{status.upper()}] {event}")


# ====================== 🧠 FILE SCANNER ==============================
def scan_files(base_dir: Path):
    """Pindai semua file relevan untuk sinkronisasi"""
    files = []
    for ext in SYNC_RULES.keys():
        for f in base_dir.rglob(f"*{ext}"):
            files.append(f)
    return files


# ====================== 🧬 SYNC PROCESSOR ============================
def push_file_to_repo(file_path: Path, repo: str, target_path: str):
    """Push file ke GitHub jika REMOTE_SYNC aktif"""
    if not REMOTE_SYNC:
        print(f"🧩 [LOCAL MODE] {file_path.name} -> {repo}/{target_path}")
        return True

    if githubCommitFile is None:
        print("⚠️ Plugin GitHub API tidak aktif.")
        return False

    try:
        content = file_path.read_text()
        githubCommitFile({
            "repo": repo,
            "path": target_path,
            "content": content,
            "message": f"AutoSync TUYUL v5.4.1-DHT — {file_path.name}",
            "branch": "autosync/v541",
        })
        log_event(f"✅ Commit success: {file_path.name} → {repo}")
        return True
    except Exception as e:
        log_event(f"❌ Commit gagal: {file_path.name} ({e})", status="error")
        return False


def create_automerge_pr(repo: str, branch: str = "autosync/v541"):
    """Buat pull request otomatis"""
    if not REMOTE_SYNC or triggerRuntimeReload is None:
        return
    try:
        triggerRuntimeReload({
            "event_type": "create_pull_request",
            "client_payload": {
                "repo": repo,
                "branch": branch,
                "title": f"AutoSync TUYUL v5.4.1-DHT",
                "body": "Automated synchronization from TUYUL AGI system.",
            },
        })
        log_event(f"🔁 Pull Request dibuat untuk {repo}")
    except Exception as e:
        log_event(f"⚠️ Gagal membuat PR di {repo}: {e}", status="error")


# ====================== 🧩 SYNC MAIN FUNCTION ========================
def scan_and_sync(base_dir: Path = SYNC_BASE):
    """Fungsi utama sinkronisasi TUYUL FX"""
    log_event("🚀 Memulai AutoSync Vault v5.4.1 ...")
    files = scan_files(base_dir)
    synced = []

    for f in files:
        ext = f.suffix
        if ext not in SYNC_RULES:
            continue

        repo = SYNC_RULES[ext]["repo"]
        target = f"{SYNC_RULES[ext]['target']}{f.name}"

        # 🔐 1. Update delta history
        update_delta_history(f.stem, str(f))

        # 🔎 2. Verifikasi hash
        if not verify_file_integrity(f):
            rollback_module(f.stem)
            continue

        # 📤 3. Push file ke repo
        if push_file_to_repo(f, repo, target):
            synced.append(f.name)

    # 🔁 4. Buat pull request jika ada file baru
    if REMOTE_SYNC and synced:
        for repo in set(rule["repo"] for rule in SYNC_RULES.values()):
            create_automerge_pr(repo)

    log_event(f"✅ Sinkronisasi selesai. Total file: {len(synced)}")
    return synced


# ====================== CLI Interface ===============================
if __name__ == "__main__":
    print("\n🐺 TUYUL FX AutoSync v5.4.1 — Remote Mode:", REMOTE_SYNC)
    synced_files = scan_and_sync()
    print(f"\n📦 File tersinkron: {len(synced_files)} → {', '.join(synced_files)}")
    print("🐺 TUYUL siap lanjut ke siklus reflektif 🔄\n")
