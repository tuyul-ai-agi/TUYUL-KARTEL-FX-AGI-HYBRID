# Reflective Coherence Monitor — TUYUL v5.7.3r++
import numpy as np, datetime, json, os

class ReflectiveCoherenceMonitor:
    """Mengukur koherensi lintas layer: CONF₁₂, WLWCI, RCAdj"""
    LOG_PATH = "logs/coherence_monitor.json"

    def __init__(self):
        self.records = []

    def evaluate(self, conf12, wlwci, rcadj):
        avg = round(np.mean([conf12, wlwci, rcadj]), 3)
        stability = round(np.std([conf12, wlwci, rcadj]), 3)
        state = "stable" if avg >= 0.9 and stability < 0.05 else "adaptive"

        reflection = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "conf12": conf12,
            "wlwci": wlwci,
            "rcadj": rcadj,
            "avg_coherence": avg,
            "stability": stability,
            "reflective_state": state
        }
        self.records.append(reflection)
        self._log(reflection)
        print(f"🧩 Coherence Monitor — State: {state}, Avg: {avg}, Stab: {stability}")
        return reflection

    def _log(self, data):
        os.makedirs("logs", exist_ok=True)
        with open(self.LOG_PATH, "a") as f:
            f.write(json.dumps(data) + "\n")
