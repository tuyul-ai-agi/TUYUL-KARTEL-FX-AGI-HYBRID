# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Reflective Meta Cycle
# ------------------------------------------------------------
# Menjalankan pengawasan meta reflektif dan koreksi otomatis
# terhadap integritas lintas-repo.
# ============================================================

from datetime import datetime
import json
import time
from pathlib import Path

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    getReflectiveReport,
    runReflectiveCycle,
)
from modules.reflective_integrity_tracker import run_reflective_integrity_check

LOG_FILE = Path("logs/reflective_meta_cycle.log")


def reflective_meta_cycle(interval_minutes: int = 30) -> None:
    """Menjalankan meta-siklus reflektif setiap 30 menit."""

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    print("🧠 Starting Reflective Meta Cycle v5.7.8...")
    while True:
        report = getReflectiveReport()
        integrity = run_reflective_integrity_check()

        if integrity["integrity_index"] < 0.9:
            print("⚠️ Integrity rendah! Menjalankan sinkronisasi ulang...")
            runReflectiveCycle()

        _save_meta_log(report, integrity)
        print(
            f"🕒 Menunggu {interval_minutes} menit sebelum meta-cycle berikutnya...\n"
        )
        time.sleep(interval_minutes * 60)


def _save_meta_log(report: dict, integrity: dict) -> None:
    journal_dir = Path("journal_repo")
    journal_dir.mkdir(parents=True, exist_ok=True)

    meta = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "bias_drift": report["bias_drift"],
        "coherence_gain": report["coherence_gain"],
        "integrity_index": integrity["integrity_index"],
        "coherence_drift": integrity["coherence_drift"],
        "reflection_score": integrity["reflection_score"],
    }

    status_path = journal_dir / "reflective_meta_status.json"
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{meta['timestamp']}] Drift={meta['bias_drift']} | "
            f"Coherence={meta['coherence_gain']} | "
            f"Integrity={meta['integrity_index']}\n"
        )

    print("✅ Meta cycle report saved → journal_repo/reflective_meta_status.json")


if __name__ == "__main__":
    reflective_meta_cycle()
