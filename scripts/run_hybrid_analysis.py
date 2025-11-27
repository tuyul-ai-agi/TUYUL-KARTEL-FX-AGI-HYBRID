"""
🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0
Execution Runner for Hybrid AGI Analysis
"""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

    status = bridge.get_status()
    print(f"Bridge Status: {status['bridge_status']} | Last Sync: {status['last_sync']}")
    print(f"API Base: {status['api_base']} | Repo: {status['repo']}")

    print("\n🚀 Menjalankan analisa XAU/USD [H1]...\n")
    result = bridge.run_analysis("XAU/USD", "H1")

    print("=== HYBRID ANALYSIS OUTPUT ===")
    for key, value in result.items():
        print(f"{key}: {value}")

from argparse import ArgumentParser

from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler


def main(pair: str = "XAU/USD", timeframe: str = "H1") -> None:
    """Main entrypoint untuk menjalankan analisa AGI Hybrid."""
    print("⚡ Initializing TUYUL AGI Hybrid Bridge...")
    bridge = GPTBridgeHandler()
    print("Bridge Status:", bridge.get_status())

    result = bridge.run_analysis(pair, timeframe)

    print("\n=== HYBRID ANALYSIS OUTPUT ===")
    for key, val in result.items():
        print(f"{key}: {val}")

    print("\n✅ Vault synchronized & Meta Reflection complete.")
    print("Siap Bossku, gaskeun serigala. Tuyul log di Journal Boss 📝")


if __name__ == "__main__":
    parser = ArgumentParser(description="Run TUYUL AGI Hybrid analysis")
    parser.add_argument("pair", nargs="?", default="XAU/USD", help="Symbol pair to analyze")
    parser.add_argument(
        "timeframe", nargs="?", default="H1", help="Timeframe for the analysis (e.g. H1)"
    )
    args = parser.parse_args()

    main(pair=args.pair, timeframe=args.timeframe)
