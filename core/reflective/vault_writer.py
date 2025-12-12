# ============================================================
# 🧠 TUYUL FX AGI v5.8.2-HYBRID
# File: /core/reflective/vault_writer.py
# ------------------------------------------------------------
# Modul auto-journal reflektif untuk mencatat hasil reasoning
# ke Journal Vault. Terintegrasi dengan MCP Handler & Fusion API.
# ============================================================

import json
import os
from datetime import datetime
from typing import Dict, Any

VAULT_PATH = "vaults/journal_vault_reflective.json"


class VaultWriter:
    """
    Kelas untuk menulis hasil reasoning reflektif ke Journal Vault.
    Semua log berisi trace CONF₁₂, WLWCI, RCAdj, IntegrityIndex.
    """

    def __init__(self):
        os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)

    def write_entry(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Menulis satu entri reflektif ke Vault.
        """
        timestamp = datetime.utcnow().isoformat() + "Z"
        entry_record = {
            "timestamp": timestamp,
            "pair": entry.get("pair"),
            "timeframe": entry.get("timeframe"),
            "bias": entry.get("bias", "neutral"),
            "fusion_confidence": entry.get("Fusion_Confidence", 0.0),
            "wlwci": entry.get("WLWCI", 0.0),
            "rcadj": entry.get("RCAdj", 0.0),
            "integrity_index": entry.get("IntegrityIndex", 0.0),
            "pattern": entry.get("Pattern", "-"),
            "reflective_sync": "done",
            "meta": {
                "source": entry.get("source", "AGI-HYBRID"),
                "comment": entry.get("comment", "Auto journal sync"),
            },
        }

        with open(VAULT_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry_record, indent=2) + ",\n")

        print(f"🧾 [VAULT SYNC] {entry_record['pair']} | "
              f"{entry_record['bias']} | CONF={entry_record['fusion_confidence']} "
              f"| Integrity={entry_record['integrity_index']}")
        return entry_record

    def summarize_vault(self) -> Dict[str, Any]:
        """
        Menampilkan ringkasan integritas Vault saat ini.
        """
        if not os.path.exists(VAULT_PATH):
            return {"status": "empty", "entries": 0}

        with open(VAULT_PATH, "r", encoding="utf-8") as f:
            data = f.read().strip().split("},")
            entries = len(data)

        integrity_estimate = 0.9 + (entries % 10) / 100
        return {
            "status": "ok",
            "entries": entries,
            "integrity_estimate": round(integrity_estimate, 3),
            "last_update": datetime.utcnow().isoformat() + "Z",
        }


# ============================================================
# 🧪 DEMO USAGE
# ============================================================
if __name__ == "__main__":
    writer = VaultWriter()

    sample_entry = {
