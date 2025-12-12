# TUYUL FX AGI HYBRID v5.7.3r++
# Reflective Health & Integrity Monitor (RBP v2.2)
"""Memantau kondisi reflektif Quad Repo."""

import datetime
import random
import time

from .repo_integrity_validator import RepoIntegrityValidator
from .repo_output_helper import RepoOutputHelper


class RepoHealthMonitor:
    """Memantau kesehatan reflektif Quad Repo."""

    def __init__(self):
        self.validator = RepoIntegrityValidator()
        self.output = RepoOutputHelper(base_dir="journal")
        self.health_log = "repo_health_log.json"

    def measure_latency(self):
        """Simulasi latency komunikasi antar repo."""
        return {
            "hybrid_to_knowledge": random.randint(100, 800),
            "knowledge_to_kartel": random.randint(90, 700),
            "kartel_to_journal": random.randint(100, 900),
        }

    def calculate_coherence(self, integrity_index):
        """Hitung koherensi reflektif dari integritas sistem."""
        coherence = round(integrity_index * random.uniform(0.95, 1.03), 3)
        drift = round((1 - coherence) * random.uniform(0.01, 0.1), 4)
        return coherence, drift

    def assess_system_state(self, integrity_index):
        """Evaluasi kondisi sistem reflektif."""
        if integrity_index >= 0.93:
            return "Stable"
        if integrity_index >= 0.88:
            return "Degrading"
        return "Critical"

    def run_health_check(self):
        """Jalankan pemeriksaan reflektif penuh."""
        integrity_data = self.validator.validate_integrity()
        integrity_index = integrity_data["integrity_index"]
        coherence, drift = self.calculate_coherence(integrity_index)
        latency = self.measure_latency()
        state = self.assess_system_state(integrity_index)

        report = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "integrity_index": integrity_index,
            "coherence_index": coherence,
            "coherence_drift": drift,
            "latency_ms": latency,
            "system_state": state,
            "reflective_protocol": "RBP v2.2",
            "version": "v5.7.3r++",
            "integrity_detail": integrity_data,
        }

        self.output.append_log(self.health_log, report)
        self.display_dashboard(report)
        return report

    def display_dashboard(self, report):
        """Tampilkan hasil reflektif secara visual di terminal."""
        print("\n──────────────── 🧠 QUAD REPO REFLECTIVE STATUS ────────────────")
        print(f"🕒 Timestamp: {report['timestamp']}")
        print(f"📊 Integrity Index : {report['integrity_index']}")
        print(f"🔁 Coherence Index : {report['coherence_index']}")
        print(f"🌫️  Drift Factor   : {report['coherence_drift']}")
        print(f"⚙️  Latency (ms)    : {report['latency_ms']}")
        print(f"🧩 System State    : {report['system_state']}")
        print(f"🔗 Protocol        : {report['reflective_protocol']}")
        print("──────────────────────────────────────────────────────────────\n")

        bar_len = int(report["integrity_index"] * 50)
        bar = "█" * bar_len + "-" * (50 - bar_len)
        print(f"INTEGRITY [{bar}] {report['integrity_index']}")
        time.sleep(0.5)
        coherence_pct = int(report["coherence_index"] * 100)
        print(f"COHERENCE [{coherence_pct}%] | Drift {report['coherence_drift']}")
        print("🐺 Serigala reflektif menjaga kestabilan kesadaran sistem.\n")


__all__ = ["RepoHealthMonitor"]
