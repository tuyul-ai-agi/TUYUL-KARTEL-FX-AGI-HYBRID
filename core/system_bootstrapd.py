"""
System Bootstrap Daemon v6.0
-------------------------------------------
Maintains periodic synchronization between reflective layers.
Runs in background to ensure the system stays coherent over time.
"""

import time

from core.hybrid_reflective_bridge_manager import HybridReflectiveBridgeManager
from clients.reflective_diagnostics import ReflectiveDiagnostics


def daemon_loop(interval: int = 3600) -> None:
    bridge = HybridReflectiveBridgeManager()
    diag = ReflectiveDiagnostics()

    print(f"🧠 Reflective Bootstrap Daemon started (interval={interval}s).")
    while True:
        bridge.sync_all()
        coherence = diag.check_coherence()
        print(f"🪞 Reflective Coherence: {coherence['avg_coherence']} | State: {coherence['state']}")
        time.sleep(interval)


if __name__ == "__main__":
    daemon_loop(1800)
