"""
Risk Layer Initialization
-------------------------
Mengelola perhitungan risiko adaptif (lot, RR, regime awareness)
untuk TUYUL FX AGI HYBRID v5.7.3r++.
"""

from core.risk.adaptive_risk_calculator import AdaptiveRiskCalculator
from core.risk.regime_state_detector import RegimeStateDetector

__version__ = "5.7.3r++"
__author__ = "Tuyul Kartel AGI Core Team"
__protocol__ = "RBP v2.2"

__all__ = ["AdaptiveRiskCalculator", "RegimeStateDetector"]


def init_summary():
    print("────────────────────────────────────────────")
    print("⚖️ RISK LAYER INITIALIZED")
    print(f"Version  : {__version__}")
    print(f"Protocol : {__protocol__}")
    print("Adaptive Risk Layer aktif — kesadaran risiko dinamis berjalan.")
    print("────────────────────────────────────────────")


if __name__ == "__main__":
    init_summary()
