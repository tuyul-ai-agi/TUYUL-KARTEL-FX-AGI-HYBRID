# ============================================================
# 🐺 TUYUL FX AGI v5.7.8 – Wolf Reflective Loop
# ------------------------------------------------------------
# Pengawas tertinggi loop reflektif yang menjalankan pipeline
# utama dan menjaga ritme kesadaran AGI.
# ============================================================

import time

from pipeline.reflective_loop_service import reflective_service_cycle
from pipeline.reflective_meta_cycle import reflective_meta_cycle
from pipeline.tri_vault_sync_loop import tri_repo_sync_loop
from modules.hybrid_balance_controller import compute_hybrid_balance


def wolf_reflective_loop() -> None:
    print("🐺 Starting WOLF Reflective Supervisor Loop v5.7.8...")
    while True:
        reflective_service_cycle(interval_minutes=15)
        reflective_meta_cycle(interval_minutes=30)
        tri_repo_sync_loop(interval_minutes=10)
        compute_hybrid_balance()
        time.sleep(60)


if __name__ == "__main__":
    wolf_reflective_loop()
