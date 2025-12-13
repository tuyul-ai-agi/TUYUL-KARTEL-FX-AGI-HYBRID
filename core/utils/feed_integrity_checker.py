"""
Feed Integrity Checker – TUYUL FX AGI HYBRID v5.7.3r++
"""

import datetime
import json
import os
from typing import Any, Dict, List, Optional

import numpy as np


def load_feed_snapshot(repo_name: str = "hybrid", path_base: str = "../") -> Optional[Dict[str, Any]]:
    """Memuat snapshot feed dari masing-masing repo reflektif."""
    path = os.path.join(path_base, f"{repo_name}_repo/repo/feed_snapshot.json")
    try:
        with open(path, "r", encoding="utf-8") as feed_file:
            snapshot = json.load(feed_file)
        return snapshot
    except FileNotFoundError:
        print(f"[Integrity ⚠️] Feed snapshot not found for {repo_name} repo.")
        return None


def compute_feed_drift(feed_a: Optional[Dict[str, Any]], feed_b: Optional[Dict[str, Any]]) -> float:
    """Mengukur deviasi reflektif antara dua feed."""
    if not feed_a or not feed_b:
        return 1.0
    try:
        pa = np.array(feed_a["price_series"][-50:])
        pb = np.array(feed_b["price_series"][-50:])
        drift = np.mean(np.abs(pa - pb)) / np.mean(pa)
        return float(np.clip(drift, 0, 1))
    except Exception as exc:  # noqa: BLE001
        print(f"[Integrity ERROR] Cannot compute drift: {exc}")
        return 1.0


def compute_coherence_index(drifts: List[float]) -> float:
    """
    Hitung indeks koherensi reflektif dari daftar drift antar repo.
    Semakin rendah drift → semakin tinggi koherensi (maks = 1.0).
    """
    coherence = 1 - np.mean(drifts)
    return round(float(np.clip(coherence, 0, 1)), 3)


def assess_feed_integrity() -> Dict[str, Any]:
    """Analisis penuh integritas feed reflektif antar repo."""
    hybrid = load_feed_snapshot("hybrid")
    knowledge = load_feed_snapshot("knowledge")
    kartel = load_feed_snapshot("kartel")
    journal = load_feed_snapshot("journal")

    drift_hk = compute_feed_drift(hybrid, knowledge)
    drift_hkrt = compute_feed_drift(hybrid, kartel)
    drift_hj = compute_feed_drift(hybrid, journal)

    coherence_index = compute_coherence_index([drift_hk, drift_hkrt, drift_hj])

    integrity_status = (
        "Stable"
        if coherence_index >= 0.9
        else "Moderate"
        if coherence_index >= 0.75
        else "Degraded"
    )

    result: Dict[str, Any] = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "coherence_index": coherence_index,
        "drift_hybrid_knowledge": round(drift_hk, 4),
        "drift_hybrid_kartel": round(drift_hkrt, 4),
        "drift_hybrid_journal": round(drift_hj, 4),
        "integrity_status": integrity_status,
    }

    print(f"[Integrity] Coherence={coherence_index} | Status={integrity_status}")
    return result


def save_integrity_report(
    result: Dict[str, Any], path: str = "../journal_repo/repo/integrity_report.json"
) -> None:
    """Simpan hasil analisis integritas ke Journal Repo."""
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as report_file:
                data = json.load(report_file)
        else:
            data = []
        data.append(result)
        with open(path, "w", encoding="utf-8") as report_file:
            json.dump(data, report_file, indent=4)
        print(f"[🧾] Integrity report updated at {result['timestamp']}")
    except Exception as exc:  # noqa: BLE001
        print(f"[Integrity ERROR] Failed to save report: {exc}")


def run_integrity_check() -> Dict[str, Any]:
    """Jalankan pemeriksaan integritas reflektif penuh."""
    result = assess_feed_integrity()
    save_integrity_report(result)
    return result


if __name__ == "__main__":
    SUMMARY = run_integrity_check()
    print(json.dumps(SUMMARY, indent=2))
