"""Reflective Cycle – TUYUL FX AGI HYBRID."""

from datetime import UTC, datetime

from core.reflective.reflective_analyzer import analyze_reflective_layers
from core.reflective.reflective_cycle_core import ReflectiveCycleCore
from core.reflective.reflective_status import ReflectiveStatus
from core.reflective.reflective_sync import sync_quad_repo


def run_reflective_cycle(pair="XAUUSD", timeframe="H4"):
    """Menjalankan siklus reflektif penuh dengan meta-konsolidasi."""

    print(f"🐺 [REFLECTIVE] Menjalankan siklus penuh untuk {pair} ({timeframe})")

    analysis = analyze_reflective_layers(pair, timeframe)
    core_cycle = ReflectiveCycleCore().execute()
    sync_info = sync_quad_repo()
    status_snapshot = ReflectiveStatus().get_status()

    reflective_state = {
        **analysis,
        **core_cycle,
        "integrity_index": sync_info.get("integrity_index", core_cycle["integrity_index"]),
        "reflective_sync": sync_info.get("reflective_sync", core_cycle["reflective_sync"]),
        "regime_state": status_snapshot["regime_state"],
        "coherence_score": status_snapshot["coherence_score"],
        "status_timestamp": status_snapshot["timestamp"],
        "cycle_timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }

    print("✅ Siklus reflektif selesai Bossku. Gaskeun serigala! 🐺⚡")
    return reflective_state


if __name__ == "__main__":
    run_reflective_cycle("XAUUSD", "H4")
