"""
Report Generator
----------------
Membuat laporan harian AGI Hybrid berdasarkan log runtime & refleksi.
"""

import json
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, log_dir="logs/"):
        self.log_dir = log_dir

    def _load_log(self, name):
        path = os.path.join(self.log_dir, name)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            lines = f.readlines()
        return lines[-10:]  # Ambil 10 terakhir untuk ringkasan

    def generate_report(self):
        report = {
            "runtime": self._load_log("runtime_hybrid.log"),
            "fusion": self._load_log("fusion_engine.log"),
            "reflective": self._load_log("reflective_cycle.log"),
            "vault_sync": self._load_log("vault_sync.log"),
            "timestamp": datetime.utcnow().isoformat()
        }
        out_path = os.path.join(self.log_dir, f"daily_report_{datetime.utcnow().strftime('%Y%m%d')}.json")
        with open(out_path, "w") as f:
            json.dump(report, f, indent=2)
        return {"status": "report_generated", "path": out_path}


if __name__ == "__main__":
    rg = ReportGenerator()
    print(rg.generate_report())
