#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUYUL FX AGI HYBRID v5.7.3r++
Reflective Adapter Logger — RBP v2.2
-------------------------------------
Author  : TUYUL Labs — Reflective Systems Division
Version : v5.7.3r++
Protocol: Reflective Bridge Protocol v2.2
Date    : 2025-12-11

Fungsi:
  • Menyimpan hasil reflektif dari adapter (OCR, Data Feed, dll.)
  • Menghitung koherensi antar adapter & integritas total
  • Mengirim telemetry ke JournalVault & Dashboard API
  • Menulis file log reflektif ke /logs/adapter_reflective_log.json
"""

import os, json, datetime, statistics, requests

class ReflectiveAdapterLogger:
    LOG_PATH = "logs/adapter_reflective_log.json"
    DASHBOARD_API = "http://localhost:5733/metrics"  # sinkron ke web_ui FastAPI

    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        self.records = []

    def log(self, adapter_name, reflection_data):
        """Menulis hasil reflektif dari adapter tertentu"""
        ts = datetime.datetime.utcnow().isoformat() + "Z"
        record = {
            "timestamp": ts,
            "adapter": adapter_name,
            "fusion_confidence": reflection_data.get("fusion_confidence", None),
            "bias_drift": reflection_data.get("bias_drift", None),
            "integrity_index": reflection_data.get("integrity_index", None),
            "reflective_state": reflection_data.get("reflective_state", "unknown")
        }
        self.records.append(record)
        self._write_to_file(record)
        print(f"🧠 Logged reflective result from {adapter_name}: {record['reflective_state']}")
        return record

    def _write_to_file(self, record):
        """Append log ke JSON"""
        logs = []
        if os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "r") as f:
                try:
                    logs = json.load(f)
                except:
                    logs = []
        logs.append(record)
        with open(self.LOG_PATH, "w") as f:
            json.dump(logs[-200:], f, indent=2)

    def analyze_integrity(self):
        """Menghitung rata-rata integritas reflektif dari semua adapter"""
        if not self.records:
            print("⚠️ Tidak ada data reflektif untuk dianalisa.")
            return None

        integrities = [r["integrity_index"] for r in self.records if r.get("integrity_index")]
        drifts = [r["bias_drift"] for r in self.records if r.get("bias_drift")]

        avg_integrity = round(statistics.mean(integrities), 3) if integrities else 0
        avg_drift = round(statistics.mean(drifts), 4) if drifts else 0
        coherence = round(1 - avg_drift, 3)

        summary = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "average_integrity": avg_integrity,
            "average_drift": avg_drift,
            "coherence_score": coherence,
            "reflective_state": "stable" if avg_integrity >= 0.9 else "adaptive"
        }

        print(f"🧩 Adapter Coherence Summary → {summary}")
        self._push_to_dashboard(summary)
        return summary

    def _push_to_dashboard(self, summary):
        """Kirim telemetry ke dashboard web"""
        try:
            res = requests.post(self.DASHBOARD_API, json=summary, timeout=3)
            if res.status_code in (200, 201):
                print("📡 Telemetry synced with Dashboard.")
        except Exception as e:
            print(f"⚠️ Dashboard sync failed: {e}")

    def export_to_journal(self, path="journal/adapter_reflective_export.json"):
        """Ekspor hasil reflektif ke JournalVault"""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        summary = self.analyze_integrity()
        with open(path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"🧾 Reflective adapter data exported to {path}")
