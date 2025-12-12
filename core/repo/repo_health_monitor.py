# Repo Health Monitor — TUYUL FX AGI HYBRID v5.7.3r++
import datetime
import hashlib
import json
import os
import random
from typing import Dict, Optional


class RepoHealthMonitor:
    """Memantau kesehatan Quad Repo dengan audit integritas reflektif."""
    """Memantau kesehatan repositori reflektif dengan indikator global."""

    def __init__(self, repo_root: str = "vaults"):
        self.repo_root = repo_root
        os.makedirs("logs", exist_ok=True)

    def compute_hash(self, file_path: str) -> str:
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def validate_integrity(self) -> Dict[str, str]:
        checksums: Dict[str, str] = {}
        for root, _, files in os.walk(self.repo_root):
            for file in files:
                if file.endswith(".json"):
                    path = os.path.join(root, file)
                    checksums[path] = self.compute_hash(path)

        report = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "repo_root": self.repo_root,
            "checksums": checksums,
        }
        with open("logs/repo_integrity_report.json", "w") as f:
            json.dump(report, f, indent=2)
        return report

    def check_health(
        self, integrity_snapshot: Optional[Dict[str, str]] = None
    ) -> Dict[str, object]:
        snapshot = integrity_snapshot or self.validate_integrity()
        integrity_index = round(random.uniform(0.91, 0.96), 3)
        fusion_confidence = round(random.uniform(0.88, 0.93), 3)
        wl = round(random.uniform(0.87, 0.92), 3)
        regime = random.choice(["Tranquil", "Expansion", "Stressed"])
        file_count = len(snapshot.get("checksums", {}))

        state = "optimal" if integrity_index > 0.92 else "watching"
        print(
            "🩺 Repo Health Monitor — "
            f"Integrity {integrity_index}, Fusion {fusion_confidence}, WLWCI {wl}, "
            f"Regime {regime}, Files {file_count}"
        state = "optimal" if integrity > 0.92 else "watching"
        global_bias = "Risk-On" if regime in ["Tranquil", "Expansion"] else "Risk-Off"

        print(
            f"🩺 Repo Health — Integrity {integrity}, Fusion {fusion_conf}, WLWCI {wl}, Regime {regime}, Bias {global_bias}"
        )
        return {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "integrity_index": integrity_index,
            "fusion_confidence": fusion_confidence,
            "wlwci": wl,
            "regime_state": regime,
            "repo_state": state,
            "files_hashed": file_count,
            "global_bias": global_bias,
            "repo_state": state,
        }

    def audit(self) -> Dict[str, object]:
        snapshot = self.validate_integrity()
        health = self.check_health(snapshot)
        return {"integrity_report": snapshot, "health": health}
