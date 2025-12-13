"""
🧠 TUYUL FX AGI v5.7.8 – Hybrid Balance Controller
Modul pengendali keseimbangan reflektif untuk distribusi risiko,
ukuran lot, dan adaptive R:R berdasarkan integrasi Reflective Bridge,
Monte Carlo, serta Integrity Tracker.
"""

import json
import os
from datetime import datetime
from typing import Any, Dict

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    riskCalculate,
)

PATHS: Dict[str, str] = {
    "bridge": "journal_repo/reflective_bridge_output.json",
    "montecarlo": "journal_repo/montecarlo_reflective.json",
    "integrity": "journal_repo/integrity_status.json",
    "output": "journal_repo/hybrid_balance_output.json",
}

DEFAULT_BALANCE = 100_000  # USD
DEFAULT_SL_PIPS = 50  # stop loss in pips
PAIR_DEFAULT = "EUR/USD"


def load_json(path: str) -> Dict[str, Any]:
    """Safely read JSON content from *path*; fallback to empty dict on error."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def compute_hybrid_balance(
    pair: str = PAIR_DEFAULT,
    balance: float = DEFAULT_BALANCE,
    sl_pips: int = DEFAULT_SL_PIPS,
) -> Dict[str, Any]:
    """Hitung distribusi keseimbangan reflektif sistem."""
    bridge = load_json(PATHS["bridge"])
    montecarlo = load_json(PATHS["montecarlo"])
    integrity = load_json(PATHS["integrity"])

    conf12 = bridge.get("conf12", 0.9)
    integrity_index = integrity.get("integrity_index", 0.9)
    win_prob = montecarlo.get("win_probability", 90.0)
    bias = bridge.get("bias", "Neutral")

    adaptive_risk = round(((conf12 + integrity_index + (win_prob / 100)) / 3) * 1.0, 3)
    risk_pct = min(1.5, max(0.3, adaptive_risk))
    risk_calc = riskCalculate({"balance": balance, "sl_pips": sl_pips, "pair": pair})

    hybrid_output: Dict[str, Any] = {
        "pair": pair,
        "balance": balance,
        "bias": bias,
        "conf12": conf12,
        "integrity_index": integrity_index,
        "win_probability": win_prob,
        "risk_pct": round(risk_pct, 3),
        "lot": risk_calc["lot"],
        "rr_ratio": risk_calc["rr_ratio"],
        "hybrid_equilibrium": round((conf12 + integrity_index) / 2, 3),
        "regime_state": bridge.get("regime_state", "Neutral"),
        "reflective_bridge": "RBP_v2.2",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    save_balance_output(hybrid_output)
    print(
        "🧮 [HybridBalance] Pair="
        f"{pair} | Bias={bias} | CONF₁₂={conf12:.3f} | "
        f"Integrity={integrity_index:.3f} | Risk={risk_pct:.2f}% | Lot="
        f"{risk_calc['lot']:.2f}"
    )

    return hybrid_output


def save_balance_output(data: Dict[str, Any]) -> None:
    """Persist hasil keseimbangan ke jurnal."""
    os.makedirs(os.path.dirname(PATHS["output"]), exist_ok=True)
    with open(PATHS["output"], "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"✅ Hybrid Balance output saved → {PATHS['output']}")


def auto_hybrid_cycle(interval_minutes: int = 15) -> None:
    """Menjalankan siklus keseimbangan otomatis setiap *interval_minutes*."""
    import time

    while True:
        compute_hybrid_balance()
        print(
            f"🕒 Menunggu {interval_minutes} menit sebelum siklus berikutnya...\n"
        )
        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    print("🐺 TUYUL FX AGI Hybrid Balance Controller v5.7.8 (RBP_v2.2)")
    compute_hybrid_balance()
