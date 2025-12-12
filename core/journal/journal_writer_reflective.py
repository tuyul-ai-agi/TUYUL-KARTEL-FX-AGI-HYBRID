# Reflective Journal Writer — TUYUL FX v5.7.3r++
import datetime
import json
import os


class ReflectiveJournalWriter:
    """Menulis hasil reflektif ke Journal Vault dengan metrik lengkap."""

    JOURNAL_PATH = "journal/vault_reflective_log.json"

    def __init__(self):
        os.makedirs("journal", exist_ok=True)

    def write(self, data: dict):
        """Simpan hasil reflektif ke Journal Vault."""
        now = datetime.datetime.utcnow().isoformat() + "Z"
        entry = {
            "timestamp": now,
            "pair": data.get("pair", "EUR/USD"),
            "bias": data.get("bias", "Neutral"),
            "fusion_confidence": data.get("fusion_confidence", 0.90),
            "wlwci": data.get("wlwci", 0.91),
            "rcadj": data.get("rcadj", 0.79),
            "integrity_index": data.get("integrity_index", 0.93),
            "bias_drift": data.get("bias_drift", 0.02),
            "meta_learning_signal": data.get("meta_learning_signal", 0.95),
            "reflective_state": data.get("reflective_state", "stable"),
        }
        with open(self.JOURNAL_PATH, "a", encoding="utf-8") as file:
            file.write(json.dumps(entry) + "\n")
        print(
            "🧠 Reflective Journal entry logged — "
            f"{entry['bias']} | CONF₁₂: {entry['fusion_confidence']}"
        )
        return entry
