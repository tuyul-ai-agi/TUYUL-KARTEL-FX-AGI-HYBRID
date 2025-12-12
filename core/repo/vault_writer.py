# Repo Writer — TUYUL FX AGI HYBRID v5.7.3r++
import datetime
import json
import os
import random


class RepoWriter:
    """Menulis hasil reflektif ke Repo dengan rebalancing otomatis."""

    def __init__(self):
        self.repo_log_path = "repo/sync_repo_log.json"
        os.makedirs("repo", exist_ok=True)

    def write_entry(self, data):
        drift_correction = round(random.uniform(0.01, 0.03), 3)
        data["rebalance_drift"] = drift_correction
        data["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
        with open(self.repo_log_path, "a") as f:
            f.write(json.dumps(data) + "\n")

        print(f"💾 Repo Writer — Entry stored with drift correction {drift_correction}")
        return {"status": "saved", "drift_correction": drift_correction}
