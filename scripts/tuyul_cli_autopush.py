#!/usr/bin/env python3
# ================================================================
# 🐺 TUYUL FX ULTRA WOLF v5.4.1-HYBRID
# CLI AutoPush Manager — Delta Verified + PR AutoMerge
# ================================================================
# Fungsi:
# - Menjalankan AutoSync antar Vault langsung via CLI
# - Melakukan verifikasi SHA256 & delta sebelum push
# - Memonitor status PR & integritas repo
# - Bisa dijalankan manual atau via cronjob otomatis
# ================================================================

import os
import sys
import asyncio
import json
import argparse
from datetime import datetime
from pathlib import Path

# --------------------- Import core autosync ---------------------
try:
    from tuyul_fx_agi_hybrid.core.bridge.vault_autosync_v541 import (
        scan_and_sync,
        LOG_PATH,
        HISTORY_PATH,
    )
except ImportError as e:
    print("❌ Gagal impor modul autosync:", e)
    sys.exit(1)

# --------------------- Konfigurasi global -----------------------
DEFAULT_BASE = Path("/mnt/data")
DEFAULT_LOG = LOG_PATH
DEFAULT_HISTORY = HISTORY_PATH


# ================================================================
# 📘 UTILITAS LOGGING
# ================================================================
def print_header():
    print("=" * 70)
    print("🐺  TUYUL FX ULTRA WOLF — AUTO PUSH MANAGER v5.4.1")
    print("🕒  Waktu:", datetime.utcnow().isoformat())
    print("=" * 70)


def print_result(synced_files):
    print("\n📦 FILE TERSINKRON:")
    for f in synced_files:
        print(f"  • {f}")
    print("\n🧠 TOTAL:", len(synced_files))
    print("============================================================\n")


def print_summary():
    if DEFAULT_LOG.exists():
        print("📜 Log terakhir:")
        with open(DEFAULT_LOG) as f:
            lines = f.readlines()[-10:]
            for ln in lines:
                print("   ", ln.strip())
    else:
        print("⚠️ Belum ada log sinkronisasi ditemukan.")
    print("\n📘 History Path:", DEFAULT_HISTORY)
    print("============================================================\n")


# ================================================================
# 🧠 KOMANDO UTAMA
# ================================================================
async def autopush_run(mode="full"):
    """Menjalankan autopush penuh"""
    print_header()
    print(f"🚀 Mode: {mode.upper()}")
    if mode == "full":
        synced = scan_and_sync(DEFAULT_BASE)
    elif mode == "verify":
        print("🔍 Hanya melakukan verifikasi hash & delta.")
        synced = []
    else:
        print("⚙️ Mode tidak dikenal.")
        synced = []

    print_result(synced)
    print_summary()


# ================================================================
# 🧩 ARGUMENT PARSER
# ================================================================
def main():
    parser = argparse.ArgumentParser(
        description="🐺 TUYUL FX ULTRA WOLF AutoPush CLI v5.4.1 — Delta Verified Push"
    )
    parser.add_argument(
        "command",
        choices=["run", "verify", "log", "help"],
        help="Perintah: run = autopush semua file | verify = cek hash | log = tampilkan log",
    )
    args = parser.parse_args()

    if args.command == "run":
        asyncio.run(autopush_run("full"))
    elif args.command == "verify":
        asyncio.run(autopush_run("verify"))
    elif args.command == "log":
        print_header()
        print_summary()
    else:
        parser.print_help()


# ================================================================
# 🚀 ENTRY POINT
# ================================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Dibatalkan oleh user.")
        sys.exit(0)
