"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.0
GPT Bridge Executor — Reflex–Cognition Fusion Trigger

Menjalankan siklus penuh AGI Hybrid Layer-12 dari GPT engine secara langsung.
Pipeline: Fusion → Vault Sync → Meta Reflection → Journal Output
"""

from gpt_bridge_handler_v540 import GPTBridgeHandler


def run_gpt_hybrid_bridge(pair: str = "XAUUSD", timeframe: str = "H1") -> None:
    """
    Jalankan GPT–AGI Hybrid Bridge secara langsung.
    Args:
        pair (str): Simbol pair, default XAUUSD.
        timeframe (str): Timeframe analisa, default H1.
    """

    print("==========================================")
    print("🐺 TUYUL KARTEL FX HYBRID v5.4.0 — BRIDGE EXECUTOR")
    print("==========================================")
    print(f"Pair: {pair} | Timeframe: {timeframe}\n")

    try:
        # Inisialisasi Bridge
        bridge = GPTBridgeHandler()
        print("🔗 Inisialisasi GPT Bridge...")

        # Jalankan analisa AGI Hybrid penuh
        result = bridge.run_analysis(pair, timeframe)

        # Output hasil reasoning
        print("\n--- ANALISA AGI HYBRID HASIL ---")
        print(f"Pair: {result['pair']}")
        print(f"Timeframe: {result['timeframe']}")
        print(f"Bridge Status: {result['bridge_status']}")
        print(f"Last Sync: {result['last_sync']}")
        print(f"Fusion Output Keys: {list(result['fusion_output'].keys()) if isinstance(result['fusion_output'], dict) else 'Non-dict Output'}")
        print("------------------------------------------\n")

        print("🐺✅ AGI Fusion selesai dan disinkronisasi ke Vault.")
        print("📘 Hasil reasoning telah dicatat ke Journal Vault Boss.\n")

    except Exception as e:
        print("❌ Terjadi error saat menjalankan bridge:")
        print(e)

    print("==========================================")
    print("Selesai — GPT Bridge Reflexive Mode [OK]")
    print("==========================================\n")


# Eksekusi langsung saat dijalankan via GPT environment
if __name__ == "__main__":
    # Contoh: bisa ubah pair/timeframe sesuai kebutuhan
    run_gpt_hybrid_bridge(pair="EURUSD", timeframe="H4")
