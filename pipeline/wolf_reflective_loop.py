# ============================================================
# 🐺 TUYUL FX AGI v5.7.8 – Wolf Reflective Loop
# ------------------------------------------------------------
# Pengawas tertinggi loop reflektif yang menjalankan pipeline
# utama dan menjaga ritme kesadaran AGI.
# ============================================================

import threading
import time
from typing import Callable, Dict, Tuple

from pipeline.reflective_loop_service import reflective_service_cycle
from pipeline.reflective_meta_cycle import reflective_meta_cycle
from pipeline.tri_vault_sync_loop import tri_repo_sync_loop
from modules.hybrid_balance_controller import compute_hybrid_balance


LoopSpec = Tuple[Callable[..., None], Dict[str, int]]


def _start_loop(name: str, func: Callable[..., None], kwargs: Dict[str, int]) -> threading.Thread:
    def runner() -> None:
        while True:
            try:
                func(**kwargs)
            except Exception as exc:  # pragma: no cover - defensive guard
                print(f"❌ Loop {name} crashed: {exc}. Restarting in 5s...")
                time.sleep(5)
            else:
                break

    thread = threading.Thread(target=runner, name=name, daemon=True)
    thread.start()
    return thread


def wolf_reflective_loop() -> None:
    print("🐺 Starting WOLF Reflective Supervisor Loop v5.7.8...")

    loop_specs: Dict[str, LoopSpec] = {
        "reflective_service": (reflective_service_cycle, {"interval_minutes": 15}),
        "reflective_meta": (reflective_meta_cycle, {"interval_minutes": 30}),
        "tri_repo_sync": (tri_repo_sync_loop, {"interval_minutes": 10}),
    }

    threads = {
        name: _start_loop(name, func, kwargs)
        for name, (func, kwargs) in loop_specs.items()
    }

    while True:
        for name, (func, kwargs) in loop_specs.items():
            thread = threads[name]
            if not thread.is_alive():
                print(f"⚠️ Loop {name} stopped. Restarting...")
                threads[name] = _start_loop(name, func, kwargs)

        compute_hybrid_balance()
        time.sleep(60)


if __name__ == "__main__":
    wolf_reflective_loop()
