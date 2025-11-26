"""
🐺 TUYUL FX ULTRA WOLF v5.4.0 — Journal Writer v540
==================================================
Modul ini bertugas mencatat hasil Fusion Layer, VDDHybrid, dan Adaptive Risk
ke dalam file meta JSON agar Journal Vault dapat membaca dan menganalisis
evolusi performa TUYUL secara otomatis.

Sinkronisasi otomatis ke Journal & Knowledge Vault melalui Bridge Hook.
"""

import os
import json
import datetime
from pathlib import Path
from core.modules.bridge_module_v540 import auto_sync_hook

# Lokasi penyimpanan log
JOURNAL_PATH = Path("/journal/logs/")
JOURNAL_PATH.mkdir(parents=True, exist_ok=True)
LOG_FILE = JOURNAL_PATH / "journal_output12_meta.json"


class JournalWriterV540:
    def __init__(self):
        self.log_file = LOG_FILE

    def _timestamp(self):
        return datetime.datetime.utcnow().isoformat()

    def _default_meta(self):
        """Struktur dasar file meta jika belum ada."""
        return {
            "version": "v5.4.0-HYBRID",
            "module": "Fusion-Orchestrator-VDDHybrid",
            "timestamp": self._timestamp(),
            "pair": "UNSET",
            "market_phase": "Unknown",
            "sync_status": "Pending",
            "core_metrics": {},
            "macro_context": {},
            "fusion_components": {},
            "risk_parameters": {},
            "journal_feedback": {},
            "orchestrator_status": {},
        }

    async def write_entry(self, fusion_output: dict):
        """
        Menulis hasil Fusion Layer ke file meta log.
        File akan ditimpa setiap eksekusi baru, dan sinkron otomatis
        ke Journal Vault serta Knowledge Vault.
        """
        meta = self._default_meta()

        # Ambil data inti dari hasil Fusion
        meta["timestamp"] = self._timestamp()
        meta["pair"] = fusion_output.get("pair", "UNKNOWN")
        meta["market_phase"] = fusion_output.get("RegimeName", "UNDEFINED")
        meta["sync_status"] = "Synced"

        meta["core_metrics"] = {
            "CONF12": fusion_output.get("CONF12", None),
            "RLSI": fusion_output.get("RLSI", None),
            "WLWCI": fusion_output.get("WLWCI", None),
            "RCAdj": fusion_output.get("RCAdj", None),
            "RegimeState": fusion_output.get("RegimeState", None),
            "RegimeName": fusion_output.get("RegimeName", None),
            "FusionConfidence": fusion_output.get("FusionConfidence", None),
            "RiskMultiplier": fusion_output.get("RiskMultiplier", None),
        }

        meta["macro_context"] = fusion_output.get("macro_context", {})
        meta["fusion_components"] = fusion_output.get("fusion_components", {})
        meta["risk_parameters"] = fusion_output.get("risk_parameters", {})
        meta["journal_feedback"] = {
            "sync_to_knowledge": True,
            "sync_to_journal": True,
            "meta_update": "Fusion entry logged",
        }
        meta["orchestrator_status"] = {
            "last_sync_time": self._timestamp(),
            "bridge_connection": "OK",
            "autosync_hook": "active"
        }

        # Tulis ke file JSON
        with open(self.log_file, "w") as f:
            json.dump(meta, f, indent=2)

        print(f"[JournalWriterV540] ✅ Fusion log updated at {meta['timestamp']}")

        # Jalankan autosync
        await auto_sync_hook(event="fusion_pass", payload=meta)
        return meta

    def read_last_entry(self):
        """Membaca isi log terakhir (jika ada)."""
        if not self.log_file.exists():
            return None
        with open(self.log_file, "r") as f:
            return json.load(f)


# Contoh eksekusi manual (opsional)
if __name__ == "__main__":
    import asyncio

    writer = JournalWriterV540()
    dummy_fusion = {
        "pair": "EURUSD",
        "CONF12": 0.812,
        "RLSI": 0.621,
        "WLWCI": 0.742,
        "RCAdj": 0.808,
        "RegimeState": 1,
        "RegimeName": "STRESSED",
        "FusionConfidence": 0.784,
        "RiskMultiplier": 0.5,
        "macro_context": {"VIX": 22.4, "DXY": 104.1, "Corr_VIX_DXY": 0.72},
    }

    asyncio.run(writer.write_entry(dummy_fusion))
