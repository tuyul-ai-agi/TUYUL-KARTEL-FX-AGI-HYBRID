"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.0
GPT Bridge Executor — Reflex–Fusion–Vault–Journal Runner

Deskripsi:
    Menjalankan pipeline AGI Hybrid Layer-12 langsung dari GPT environment.
    Pipeline: Fusion → Vault Sync → Meta Reflection → Journal Output
"""

import os
import sys
from datetime import datetime

# Pastikan module path mengarah ke root repo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import handler utama dari ai_bridge
from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler


def run_gpt_hybrid_bridge(pair: str = "XAUUSD", timeframe: str = "H1") -> None:
    """
    Jalankan GPT–AGI Hybrid Bridge secara langsung.

    Args:
        pair (str): Simbol pair untuk analisa (default: XAUUSD)
        timeframe (str): Timeframe analisa (default: H1)
    """

    print("==========================================")
    print("🐺 TUYUL KARTEL FX HYBRID v5.4.0 — BRIDGE EXECUTOR")
    print("==========================================")
    print(f"Pair: {pair} | Timeframe: {timeframe}")
    print("------------------------------------------\n")

    try:
        # Inisialisasi Bridge
        print("🔗 Inisialisasi GPT Bridge...")
        bridge = GPTBridgeHandler()

        # Jalankan analisa AGI Hybrid penuh
        result = bridge.run_analysis(pair, timeframe)

        # Tampilkan hasil reasoning
        print("\n--- HASIL ANALISA AGI HYBRID ---")
        print(f"📊 Pair         : {result['pair']}")
        print(f"🕓 Timeframe    : {result['timeframe']}")
        print(f"⚙️ Bridge Status : {result['bridge_status']}")
        print(f"⏱️ Last Sync     : {result['last_sync']}")
        print(f"🧩 Fusion Output : {list(result['fusion_output'].keys()) if isinstance(result['fusion_output'], dict) else 'Non-dict Output'}")
        print("------------------------------------------\n")

        # Simpan log ke vault
        os.makedirs("vaults/logs", exist_ok=True)
        log_path = "vaults/logs/gpt_bridge_exec.log"
        with open(log_path, "a") as log_file:
            log_file.write(f"[{datetime.utcnow().isoformat()}] {pair}/{timeframe} - {result['bridge_status']}\n")

        print(f"✅ Log disimpan di: {log_path}")
        print("🐺✅ AGI Fusion selesai dan disinkronisasi ke Vault.")
        print("📘 Hasil reasoning telah dicatat ke Journal Vault Boss.\n")

    except Exception as e:
        print("❌ Terjadi error saat menjalankan bridge:")
        print(e)

    print("==========================================")
    print("Selesai — GPT Bridge Reflexive Mode [OK]")
    print("==========================================\n")


# ============================================================
# 🚀 Auto-Run Section (opsional, bisa dijalankan manual juga)
# ============================================================
if __name__ == "__main__":
    # Ambil argumen CLI opsional
    import argparse

    parser = argparse.ArgumentParser(description="🐺 Jalankan GPT–AGI Hybrid Bridge Executor")
    parser.add_argument("--pair", type=str, default="XAUUSD", help="Simbol pair (default: XAUUSD)")
    parser.add_argument("--tf", type=str, default="H1", help="Timeframe (default: H1)")
    args = parser.parse_args()

    run_gpt_hybrid_bridge(pair=args.pair, timeframe=args.tf)
