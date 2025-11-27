"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.0
AUTO-START REFLEXIVE SYSTEM MODULE

Deskripsi:
    File ini dijalankan otomatis saat sistem hybrid aktif.
    Ia akan men-trigger GPT Bridge Executor → Fusion Analysis →
    Vault Sync → Reflective Cycle.
"""

import os
from datetime import datetime

# Jalur relatif ke modul bridge executor
try:
    from scripts.gpt_bridge_executor import run_gpt_hybrid_bridge
except ImportError as e:
    print("❌ Gagal import GPT Bridge Executor:", e)
    run_gpt_hybrid_bridge = None

# Opsi tambahan: reflective sync
try:
    from scripts.vault_sync_reflective_fusion import run_reflective_sync
except ImportError:
    run_reflective_sync = None


def start_hybrid_system():
    """
    Menjalankan sistem hybrid AGI otomatis:
    1️⃣ GPT Bridge Reflex → Fusion Layer-12
    2️⃣ Sinkronisasi Vault
    3️⃣ Reflective Fusion Layer
    """
    print("===============================================")
    print("🐺 TUYUL KARTEL FX HYBRID v5.4.0 — SYSTEM START")
    print("===============================================")
    print(f"🕓 Boot Time : {datetime.utcnow().isoformat()}")
    print(f"🌐 Working Dir: {os.getcwd()}")
    print("-----------------------------------------------\n")

    # Baca konfigurasi environment
    pair = os.getenv("DEFAULT_PAIR", "XAUUSD")
    tf = os.getenv("DEFAULT_TF", "H1")

    # Jalankan GPT–AGI Bridge Executor
    if run_gpt_hybrid_bridge:
        print("⚙️  Menjalankan GPT Bridge Executor...")
        try:
            run_gpt_hybrid_bridge(pair=pair, timeframe=tf)
        except Exception as e:
            print("❌ Error saat menjalankan Bridge:", e)
    else:
        print("⚠️ GPT Bridge Executor tidak tersedia.")

    # Jalankan Reflective Vault Sync (opsional)
    if run_reflective_sync:
        print("🔁 Menjalankan Reflective Vault Synchronization...")
        try:
            run_reflective_sync()
            print("🧠 Reflective Fusion selesai disinkronisasi.")
        except Exception as e:
            print("⚠️ Gagal menjalankan reflective sync:", e)
    else:
        print("⚠️ Modul reflective fusion belum tersedia.")

    print("-----------------------------------------------")
    print("🐺✅ Sistem TUYUL HYBRID aktif sepenuhnya.")
    print("📘 Semua pipeline siap dijalankan otomatis.")
    print("===============================================\n")

    # Simpan log startup
    os.makedirs("vaults/logs", exist_ok=True)
    with open("vaults/logs/hybrid_start.log", "a") as log:
        log.write(f"[{datetime.utcnow().isoformat()}] HYBRID SYSTEM START - OK\n")


# ==========================================
# 🚀 Auto-Run saat package di-load
# ==========================================
try:
    start_hybrid_system()
except Exception as e:
    print("❌ Startup error:", e)
