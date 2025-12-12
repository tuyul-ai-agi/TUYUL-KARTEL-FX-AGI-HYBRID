# Volume Flow Reflective Analyzer — TUYUL v5.7.3r++
import numpy as np, datetime

class VolumeFlowReflectiveAnalyzer:
    """Analisis volume flow dengan validasi VWAP deviation reflektif"""
    def __init__(self):
        self.integrity_index = 0.0

    def evaluate(self, volumes, prices, vwap):
        flow_ratio = np.mean(volumes) / (np.std(volumes) + 1e-9)
        deviation = abs(np.mean(prices) - vwap) / vwap
        integrity = round(1 - deviation, 3)
        state = "stable" if integrity > 0.9 else "adaptive"

        reflection = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "flow_ratio": round(flow_ratio, 3),
            "vwap_deviation": round(deviation, 4),
            "integrity_index": integrity,
            "reflective_state": state
        }
        print(f"📈 Volume Flow Reflective — {state.upper()} | Int: {integrity}, Dev: {deviation}")
        return reflection
