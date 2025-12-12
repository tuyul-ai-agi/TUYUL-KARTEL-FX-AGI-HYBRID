# Journal Integrity Monitor — TUYUL FX AGI HYBRID v5.7.3r++
import datetime
import json
import os


class JournalIntegrityMonitor:
    """Monitor integritas dan drift kesadaran Journal Vault."""

    def __init__(self, path: str = "journal/vault_reflective_log.json"):
        self.path = path

    def evaluate(self):
        if not os.path.exists(self.path):
            return {"status": "empty", "integrity_index": 0.0}
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.readlines()[-50:]
        data = [json.loads(line) for line in lines if line.strip()]
        integrity = round(sum(item["integrity_index"] for item in data) / len(data), 3)
        drift = round(sum(item["bias_drift"] for item in data) / len(data), 3)
        state = "stable" if integrity > 0.9 else "adaptive"
        print(f"🧩 Journal Integrity: {integrity} | Drift: {drift} | State: {state}")
        return {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "integrity_index": integrity,
            "bias_drift": drift,
            "state": state,
            "entries_analyzed": len(data),
        }
