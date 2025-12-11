#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUYUL FX AGI HYBRID v5.7.3r++
Reflective Diagnostics & Coherence Analyzer
--------------------------------------------
Author  : TUYUL Labs – Reflective Systems Division
Version : v5.7.3r++
Protocol: RBP v2.2
Date    : 2025-12-11

Fungsi:
  • Menganalisa hasil siklus reflektif (Hybrid–FX–Kartel–Journal)
  • Menghitung Reflective Coherence Index (RCI) & Integrity Delta (SID)
  • Mendeteksi bias drift & sinkronisasi vault
  • Menulis laporan reflektif ke JournalVault & ReflectiveLogger
"""

import os, json, datetime, statistics
from .reflective_logger import ReflectiveLogger

class ReflectiveDiagnostics:
    LOG_PATH = "logs/reflective_diagnostics.json"

    def __init__(self):
        os.makedirs("logs", exist_ok=True)

    def analyze_cycle(self, cycle_output):
        """Analisa hasil reflektif cycle dari Bridge Manager"""
        ts = datetime.datetime.utcnow().isoformat() + "Z"
        fusion_conf = cycle_output.get("fusion_confidence", 0.0)
        integrity_summary = cycle_output.get("integrity_summary", {})
        avg_integrity = integrity_summary.get("average_integrity", 0.0)
        drift = integrity_summary.get("drift", 0.0)

        # 🔢 Hitung metrik reflektif
        reflective_coherence_index = round((fusion_conf + avg_integrity) / 2, 3)
        system_integrity_delta = round(1 - abs(fusion_conf - avg_integrity), 3)
        reflection_score = round((reflective_coherence_index + system_integrity_delta) / 2, 3)

        # ⚙️ Buat laporan reflektif
        report = {
            "timestamp": ts,
            "fusion_confidence": fusion_conf,
            "avg_integrity": avg_integrity,
            "drift": drift,
            "reflective_coherence_index": reflective_coherence_index,
            "system_integrity_delta": system_integrity_delta,
            "reflection_score": reflection_score,
            "reflective_state": "stable" if reflection_score >= 0.9 else "adaptive"
        }

        # 💾 Simpan ke log
        self._write_diagnostics(report)
        ReflectiveLogger.log("reflective_diagnostics", report)

        print("\n🧩 Reflective Diagnostics Report")
        print(json.dumps(report, indent=2))
        print("✅ Reflective self-assessment completed successfully.\n")

        return report

    def _write_diagnostics(self, report):
        """Simpan hasil ke file JSON"""
        logs = []
        if os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "r") as f:
                try:
                    logs = json.load(f)
                except:
                    logs = []
        logs.append(report)
        with open(self.LOG_PATH, "w") as f:
            json.dump(logs[-100:], f, indent=2)

    def summary(self):
        """Menampilkan ringkasan diagnostik terkini"""
        if not os.path.exists(self.LOG_PATH):
            print("❌ Belum ada hasil diagnostic reflektif.")
            return None

        with open(self.LOG_PATH, "r") as f:
            logs = json.load(f)

        if not logs:
            print("❌ Log masih kosong.")
            return None

        last = logs[-1]
        trend = statistics.mean(r["reflection_score"] for r in logs[-10:]) if len(logs) >= 10 else last["reflection_score"]

        print("\n🧠 Reflective Diagnostic Summary (Last 10 Cycles)")
        print(f"🟢 Average Reflection Score: {round(trend, 3)}")
        print(f"🧩 Current State: {last['reflective_state']}")
        print(f"📈 Last Integrity: {last['avg_integrity']}, Drift: {last['drift']}")
        print(f"🕒 Updated: {last['timestamp']}")
        return last
