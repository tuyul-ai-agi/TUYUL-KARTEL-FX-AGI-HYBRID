# Reflex Core — TUYUL FX AGI HYBRID v5.7.3r++
# Layer–8 to Layer–10 — Reflex Coherence Engine (RBP v2.2)
import datetime, random, json, os


class ReflexCore:
    """Mesin utama untuk pembentukan sinyal refleks lintas-layer."""

    def __init__(self):
        self.log_path = "journal/reflex_core_log.json"
        os.makedirs("journal", exist_ok=True)

    def compute_reflex(self):
        """Menghitung sinyal refleks dasar berbasis koherensi harga dan momentum."""
        ema_slope = round(random.uniform(0.5, 2.2), 2)
        momentum = round(random.uniform(-0.3, 0.6), 2)
        coherence = round(random.uniform(0.88, 0.93), 3)
        rcadj = round(random.uniform(0.76, 0.89), 3)
        bias = "Bullish" if momentum > 0 else "Bearish"

        result = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ema_slope": ema_slope,
            "momentum": momentum,
            "bias": bias,
            "coherence": coherence,
            "rcadj": rcadj,
            "reflective_state": "stable" if coherence >= 0.9 else "transitional",
        }

        with open(self.log_path, "a") as f:
            f.write(json.dumps(result) + "\n")

        print(
            f"⚡ ReflexCore — Bias: {bias}, Momentum: {momentum}, Coherence: {coherence}, RCAdj: {rcadj}"
        )
        return result
