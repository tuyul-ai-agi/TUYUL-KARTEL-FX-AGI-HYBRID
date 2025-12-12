"""
TWMS Layer Initialization
-------------------------
Trend–Wave–Momentum–Structure Layer untuk TUYUL FX AGI HYBRID.
Membaca arah makro pasar sebagai dasar bias reflektif.
"""

from core.twms.twms_fusion_macro_mn import TWMSFusionMacroMN

__version__ = "5.7.3r++"
__author__ = "Tuyul Kartel AGI Core Team"
__protocol__ = "RBP v2.2"

__all__ = ["TWMSFusionMacroMN"]


def init_summary():
    print("────────────────────────────────────────────")
    print("🌊 TWMS LAYER INITIALIZED (Macro Direction Engine)")
    print(f"Version  : {__version__}")
    print(f"Protocol : {__protocol__}")
    print("TWMS aktif — membaca arah tren makro untuk bias reflektif sistem.")
    print("────────────────────────────────────────────")


if __name__ == "__main__":
    init_summary()
