"""
🐺 Reflective Cycle – TUYUL FX AGI HYBRID
-----------------------------------------
Menjalankan siklus reflektif penuh:
Fusion → Monte Carlo → Vault Sync → Logging
-----------------------------------------
"""

from datetime import datetime
from core.reflective.reflective_analyzer import analyze_reflective_layers
from core.reflective.reflective_live_bridge import run_live_montecarlo
from core.reflective.reflective_sync import sync_quad_repo
from core.reflective.reflective_status import update_status_log

def run_reflective_cycle(pair="XAUUSD", timeframe="H4"):
    print(f"🐺 [REFLECTIVE] Menjalankan siklus penuh untuk {pair} ({timeframe})")

    fusion = analyze_reflective_layers(pair, timeframe)
    monte = run_live_montecarlo(pair)
    sync_info = sync_quad_repo()

    reflective_state = {
        **fusion,
        **monte,
        "integrity_index": sync_info["integrity_index"],
        "reflective_sync": sync_info["reflective_sync"],
        "timestamp": datetime.utcnow().isoformat()
    }

    update_status_log(reflective_state)
    print("✅ Siklus reflektif selesai Bossku. Gaskeun serigala! 🐺⚡")
    return reflective_state


if __name__ == "__main__":
    run_reflective_cycle("XAUUSD", "H4")
