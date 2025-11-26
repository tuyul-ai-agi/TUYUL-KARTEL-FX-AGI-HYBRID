"""
🐺 TUYUL FX v5.4.0 — Reflective Cycle Core
==========================================
Mengatur siklus meta-learning & coherence feedback antara
Fusion Layer ↔ Reflex Layer ↔ Vault Sync.
"""

import datetime
from tuyul_fx_agi_hybrid.core.bridge.vault_autosync_v541 import scan_and_sync

class ReflectiveCycleCoreV540:
    def __init__(self):
        self.last_cycle_time = None
        self.reflection_score = 0.0

    def run_cycle(self, fusion_output, reflex_data, journal_meta):
        """Menjalankan siklus reflektif penuh"""
        self.last_cycle_time = datetime.datetime.utcnow().isoformat()
        coherence = self._calculate_coherence(fusion_output, reflex_data)
        self.reflection_score = self._calculate_reflection_score(coherence, journal_meta)
        print(f"🧠 Reflective cycle complete — Coherence={coherence:.2f}, Reflection={self.reflection_score:.2f}")
        scan_and_sync("/mnt/data")
        return {"coherence": coherence, "reflection_score": self.reflection_score}

    def _calculate_coherence(self, fusion_output, reflex_data):
        try:
            return (fusion_output["RCAdj"] + reflex_data["RC"]) / 2
        except Exception:
            return 0.75

    def _calculate_reflection_score(self, coherence, journal_meta):
        try:
            meta_factor = journal_meta.get("meta_weight", 1.0)
            return round(coherence * meta_factor, 3)
        except Exception:
            return coherence

if __name__ == "__main__":
    core = ReflectiveCycleCoreV540()
    result = core.run_cycle({"RCAdj": 0.82}, {"RC": 0.79}, {"meta_weight": 1.05})
    print(result)
