"""
🧠 TUYUL FX — Reflex Core v5.4.0
===============================
Menggabungkan Reflex Coherence Index (RCI) dan RLSI Analyzer.
"""

from tuyul_fx_agi_hybrid.modules.rlsi_module_v_540 import RLSIModuleV540

class ReflexCoreV540:
    def __init__(self):
        self.rlsi = RLSIModuleV540()

    def analyze(self, pair):
        print(f"🔎 Analyzing Reflex Layer for {pair}")
        rlsi_data = self.rlsi.compute(pair)
        rc_value = round((rlsi_data.get("vol_shift", 0.75) + 0.8) / 2, 3)
        print(f"RC (Reflex Coherence) = {rc_value}")
        return {"RC": rc_value, "RLSI": rlsi_data}

if __name__ == "__main__":
    reflex = ReflexCoreV540()
    print(reflex.analyze("EURUSD"))
