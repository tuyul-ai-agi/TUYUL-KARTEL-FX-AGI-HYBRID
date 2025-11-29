"""
Regime State Detector
---------------------
Mendeteksi state pasar berdasarkan volatilitas & coherence index.
"""

class RegimeStateDetector:
    def detect(self, volatility: float, coherence_index: float):
        if volatility < 0.5 and coherence_index > 0.85:
            return "Tranquil"
        elif volatility < 1.0 and coherence_index > 0.75:
            return "Stressed"
        else:
            return "Crisis"
