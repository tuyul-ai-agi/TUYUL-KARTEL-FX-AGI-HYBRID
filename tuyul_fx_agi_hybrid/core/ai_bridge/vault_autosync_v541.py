"""
🐺 TUYUL FX ULTRA WOLF v5.4.1 — Vault AutoSync (Differential Mode)
==================================================================
Sinkronisasi lintas repositori dengan deteksi perubahan berbasis SHA256.
Hanya file yang berubah (berbeda hash) yang akan di-push.
"""

import os
import json
import hashlib
import datetime
from pathlib import Path
from api_github_com__jit_plugin import githubCommitFile

# ==========================================================
# 🔧 Konfigurasi Repositori & Path Dasar
# ==========================================================
REPO_HYBRID = "tjx578/TUYUL-KARTEL-FX-AGI-HYBRID"
REPO_KNOWLEDGE = "tjx578/TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI"
REPO_JOURNAL = "tjx578/TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI"

CACHE_FILE = "/mnt/data/vault_sync_cache.json"

SYNC_RULES = {
    ".py": {
        "target_repo": REPO_HYBRID,
        "base_path": "tuyul_fx_agi_hybrid/core/",
    },
    ".md": {
        "target_repo": REPO_KNOWLEDGE,
        "base_path": "docs/modules/",
    },
    ".json": {
        "target_repo": REPO_JOURNAL,
        "base_path": "journal/logs/",
    },
}

# ==========================================================
# 🧠 Fungsi Utilitas Hash & Cache
# ==========================================================
def compute_sha256(filepath: str) -> str:
    """Hitung hash SHA256 dari sebuah file."""
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

def load_cache() -> dict:
    """Muat cache hash terakhir."""
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_cache(cache: dict):
    """Simpan hash cache terbaru ke file."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)

# ==========================================================
# ⚙️ Sinkronisasi File dengan Deteksi Perubahan
# ==========================================================
def detect_file_type(filename: str):
    ext = Path(filename).suffix.lower()
    return SYNC_RULES.get(ext, None)

async def sync_file(filepath: str, cache: dict):
    """Sinkronkan satu file, hanya jika hash berubah."""
    if not os.path.exists(filepath):
        print(f"❌ File tidak ditemukan: {filepath}")
        return cache

    file_info = detect_file_type(filepath)
    if not file_info:
        print(f"⚠️ Tipe file tidak dikenali: {filepath}")
        return cache

    # Hitung hash file saat ini
    current_hash = compute_sha256(filepath)
    if cache.get(filepath) == current_hash:
        print(f"🟢 Tidak ada perubahan: {os.path.basename(filepath)} (skip)")
        return cache

    # Baca isi file dan push ke repo
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    target_repo = file_info["target_repo"]
    target_path = file_info["base_path"] + os.path.basename(filepath)
    message = f"AutoSync (diff) {os.path.basename(filepath)} [{datetime.datetime.utcnow().isoformat()}]"

    print(f"🚀 Sinkronisasi {os.path.basename(filepath)} ke {target_repo}/{target_path} ...")

    try:
        await githubCommitFile(
            repo=target_repo.split("/")[1],
            path=target_path,
            content=content,
            message=message,
            branch="main"
        )
        print(f"✅ Sinkronisasi sukses: {target_repo}/{target_path}")
        cache[filepath] = current_hash
    except Exception as e:
        print(f"❌ Gagal sinkronisasi {os.path.basename(filepath)}: {e}")

    return cache

def scan_and_sync(directory: str):
    """Pindai direktori dan sinkronkan file yang berubah."""
    cache = load_cache()
    print(f"🔍 Memindai direktori: {directory} (mode differential)")

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if Path(path).suffix.lower() in SYNC_RULES:
                import asyncio
                cache = asyncio.run(sync_file(path, cache))

    save_cache(cache)
    print("🧾 Cache sinkronisasi diperbarui.")

# ==========================================================
# 🧩 Continuous Watcher (opsional)
# ==========================================================
def start_watcher(directory="/mnt/data", interval=60):
    """Pantau perubahan file dan sinkronkan otomatis setiap N detik."""
    import time
    print(f"👁️ Watching {directory} setiap {interval}s...")
    while True:
        try:
            scan_and_sync(directory)
            time.sleep(interval)
        except KeyboardInterrupt:
            print("🛑 Watcher dihentikan manual.")
            break

# ==========================================================
# 🚀 Entry Point
# ==========================================================
if __name__ == "__main__":
    BASE_PATH = "/mnt/data"
    print(f"🐺 TUYUL AUTO SYNC (v5.4.1) STARTED — {datetime.datetime.utcnow().isoformat()}")
    scan_and_sync(BASE_PATH)
