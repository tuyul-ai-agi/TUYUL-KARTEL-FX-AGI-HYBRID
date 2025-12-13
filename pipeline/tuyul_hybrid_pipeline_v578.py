# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Hybrid Reflective Pipeline
# ------------------------------------------------------------
# Pipeline utama yang menggabungkan seluruh siklus reflektif:
# Reflex → Fusion → Monte Carlo → Integrity → Balance → Journal
# ============================================================

from modules.bridge_module_v578 import (
    reflective_bridge,
    reflective_montecarlo,
    reflective_vix_sync,
)
from modules.hybrid_balance_controller import compute_hybrid_balance
from modules.reflective_integrity_tracker import run_reflective_integrity_check


def run_hybrid_pipeline(pair: str = "EUR/USD") -> dict:
    print("🐺 Running TUYUL FX AGI Hybrid Reflective Pipeline v5.7.8...")

    bridge = reflective_bridge(pair)
    monte = reflective_montecarlo(pair)
    vix = reflective_vix_sync()
    integrity = run_reflective_integrity_check()
    balance = compute_hybrid_balance(pair)

    print(
        "✅ Reflective Pipeline Completed → "
        f"Bias={bridge['bias']} | Integrity={integrity['integrity_index']} | "
        f"Balance={balance['risk_pct']}%"
    )

    return {
        "bridge": bridge,
        "montecarlo": monte,
        "vix": vix,
        "integrity": integrity,
        "balance": balance,
    }


if __name__ == "__main__":
    run_hybrid_pipeline()
