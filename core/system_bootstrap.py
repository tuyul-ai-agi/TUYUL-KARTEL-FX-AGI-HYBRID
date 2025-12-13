"""
TUYUL FX AGI HYBRID v5.7.3r++
Reflective Bootloader (Adaptive Quad Repo System)
"""

import time
from typing import List


from core.reflective.reflective_loop_handler import run_reflective_cycle
from core.repo.kartel_macro_bridge import get_macro_context
from core.utils.data_feed_adapter import load_price_volume


def boot_reflective_core(pairs: List[str] = None, interval: int = 1800) -> None:
    """Run reflective cycles for multiple pairs with quad-repo sync."""
    if pairs is None:
        pairs = ["EURUSD", "XAUUSD", "GBPUSD"]

    print("\n═══════════════════════════════════════════════════════════════════")
    print("🧠 TUYUL FX AGI HYBRID CORE – Reflective Boot v5.7.3r++")
    print("⚙️  Mode: Adaptive Reflective Quad Repo System")
    print("📡  Booting reflective intelligence loop ...")
    print("═══════════════════════════════════════════════════════════════════\n")

    macro_status = get_macro_context()
    print(
        f"[Bridge] Kartel Repo Sync: {macro_status['reflective_sync_status']} | "
        f"Integrity={macro_status['integrity_index']} | Regime={macro_status['GlobalRegime']}\n"
    )

    for pair in pairs:
        try:
            print(f"🌀 Running Reflective Cycle for {pair} ...")
            price, volume = load_price_volume(pair, n=200)
            result = run_reflective_cycle(price, volume, pair=pair)

            conf12 = result["fusion"]["conf12"]
            rcadj = result["fusion"]["rcadj"]
            integrity = result["macro"]["integrity_index"]

            print(
                f"✅ [SUCCESS] {pair} CONF₁₂={conf12} | RCAdj={rcadj} | "
                f"Integrity={integrity}"
            )
            print("──────────────────────────────────────────────────────────\n")

        except Exception as exc:
            print(f"❌ [ERROR] Reflective loop for {pair} failed: {exc}\n")

        time.sleep(2)

    print("🧾 Reflective Core Completed. Syncing Quad Repo integrity...\n")
    print(f"⏳ Waiting {interval / 60:.1f} minutes before next adaptive cycle...\n")
    time.sleep(interval)


if __name__ == "__main__":
    boot_reflective_core()
