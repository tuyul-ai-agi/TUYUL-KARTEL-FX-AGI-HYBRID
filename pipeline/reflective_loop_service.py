# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Reflective Loop Service
# ------------------------------------------------------------
# Layanan reflektif utama yang menjalankan siklus:
# Fusion → Reflection → Sync → Balance
# ============================================================

from datetime import datetime
import json
import time
from pathlib import Path

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    runReflectiveCycle,
)
from modules.hybrid_balance_controller import compute_hybrid_balance

LOG_PATH = Path("logs/reflective_loop_service.log")


def reflective_service_cycle(interval_minutes: int = 15) -> None:
    """Menjalankan siklus reflektif otomatis setiap X menit."""

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    print("🐺 Starting Reflective Loop Service v5.7.8 (RBP_v2.2)")
    while True:
        result = runReflectiveCycle()
        balance = compute_hybrid_balance()
        _save_cycle_report(result, balance)
        print(
            f"🕒 Menunggu {interval_minutes} menit sebelum siklus berikutnya...\n"
        )
        time.sleep(interval_minutes * 60)


def _save_cycle_report(reflective_data: dict, balance_data: dict) -> None:
    journal_dir = Path("journal_repo")
    journal_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fusion_confidence": reflective_data["fusion_confidence"],
        "reflective_coherence": reflective_data["reflective_coherence"],
        "integrity_index": reflective_data["integrity_index"],
        "balance": balance_data["balance"],
        "risk_pct": balance_data["risk_pct"],
        "lot": balance_data["lot"],
        "regime_state": balance_data["regime_state"],
        "result": reflective_data["result"],
    }

    report_path = journal_dir / "reflective_loop_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(
            f"[{data['timestamp']}] Reflective={data['reflective_coherence']} | "
            f"Integrity={data['integrity_index']} | Regime={data['regime_state']} | "
            f"Balance={data['balance']}\n"
        )

    print("✅ Reflective cycle report saved → journal_repo/reflective_loop_report.json")


if __name__ == "__main__":
    reflective_service_cycle()
