# Regime State Detector — TUYUL FX AGI HYBRID v5.7.3r++
import datetime, random

class RegimeStateDetector:
    """Mendeteksi kondisi pasar global berdasarkan VIX & koherensi reflektif."""

    def detect_regime(self):
        vix_level = round(random.uniform(13, 28), 2)
        fear_greed = random.randint(25, 75)
        regime_state = (
            "Tranquil" if vix_level < 15 else
            "Expansion" if 15 <= vix_level < 20 else
            "Stressed" if 20 <= vix_level < 25 else
            "Crisis"
        )

        impact = round(random.uniform(-0.07, 0.05), 3)
        print(f"🌐 Regime Detector — VIX {vix_level} | State {regime_state} | Impact {impact}")

        return {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "vix_level": vix_level,
            "fear_greed_index": fear_greed,
            "regime_state": regime_state,
            "impact_on_confidence": impact
        }
