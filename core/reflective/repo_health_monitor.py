# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.2-HYBRID+
# Repo Health Monitor — Quad Repo Diagnostics System
# ============================================================
# Fungsi:
# - Mengecek latency, sync delay, dan drift antar repo
# - Menghasilkan health report untuk BOT TUYUL
# - Memberikan notifikasi reflektif bila ada anomali
# ============================================================

import os
import json
import time
import requests
from datetime import datetime

LOG_FILE = "logs/repo_health_monitor.log"
HEALTH_FILE = "logs/repo_health_report.json"

REPO_ENDPOINTS = {
    "hybrid": "https://github.com/tuyulfx/agi_hybrid_tools",
    "knowledge": "https://github.com/tuyulfx/knowledge_vault_agi",
    "kartel": "https://github.com/tuyulfx/kartel_macro_vault",
    "journal": "https://github.com/tuyulfx/journal_vault_agi"
}


def log_event(msg: str):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [HealthMonitor] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def check_latency():
    """Mengukur waktu respon dari tiap repo"""
    results = {}
    for name, url in REPO_ENDPOINTS.items():
        start = time.time()
        try:
            requests.get(url, timeout=3)
            latency = round((time.time() - start) * 1000, 2)
            results[name] = {"latency_ms": latency, "status": "OK"}
            log_event(f"🌐 {name.upper()} latency: {latency} ms ✅")
        except Exception:
            results[name] = {"latency_ms": None, "status": "TIMEOUT"}
            log_event(f"⚠️ {name.upper()} tidak merespons (timeout)")
    return results


def check_sync_delay():
    """Menganalisis perbedaan waktu update antar repo"""
    sync_times = {}
    for repo, url in REPO_ENDPOINTS.items():
        api = url.replace("github.com", "api.github.com/repos") + "/commits/main"
        try:
            r = requests.get(api, timeout=4)
            if r.status_code == 200:
                data = r.json()
                commit_time = data["commit"]["committer"]["date"]
                sync_times[repo] = datetime.fromisoformat(commit_time.replace("Z", "+00:00"))
                log_event(f"⏱ {repo.upper()} terakhir di-update: {commit_time}")
            else:
                log_event(f"⚠️ Gagal membaca waktu commit {repo.upper()}: {r.status_code}")
        except Exception:
            sync_times[repo] = None
            log_event(f"❌ Tidak bisa membaca commit repo {repo.upper()}")

    # Hitung drift waktu antara Hybrid dan repos lain
    drifts = {}
    base_time = sync_times.get("hybrid")
    if base_time:
        for repo, t in sync_times.items():
            if t:
                drift = abs((base_time - t).total_seconds()) / 60
                drifts[repo] = round(drift, 2)
            else:
                drifts[repo] = None
    else:
        log_event("⚠️ Tidak ada waktu referensi dari Hybrid Repo.")

    return drifts


def generate_health_report(latencies, drifts):
    """Membuat laporan kesehatan sistem"""
    avg_latency = sum(v["latency_ms"] or 0 for v in latencies.values() if v["latency_ms"]) / max(1, len(latencies))
    max_drift = max(v or 0 for v in drifts.values())
    state = "EXCELLENT" if avg_latency < 300 and max_drift < 3 else \
            "GOOD" if avg_latency < 600 and max_drift < 10 else "DEGRADED"

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "average_latency_ms": round(avg_latency, 2),
        "max_drift_minutes": max_drift,
        "system_state": state,
        "details": {
            "latencies": latencies,
            "drifts": drifts
        }
    }

    os.makedirs(os.path.dirname(HEALTH_FILE), exist_ok=True)
    with open(HEALTH_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    log_event(f"🧾 Health Report disimpan: {HEALTH_FILE}")
    log_event(f"📊 State: {state} | Avg Latency: {avg_latency:.2f} ms | Max Drift: {max_drift:.2f} min")

    return report


def notify_if_anomaly(report, token=None):
    """Kirim notifikasi reflektif ke Journal jika sistem tidak sehat"""
    if report["system_state"] == "DEGRADED":
        log_event("🚨 Sistem tidak stabil — mengirim notifikasi reflektif ke Journal Repo.")
        if not token:
            return

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}"
        }
        payload = {"event_type": "reflective_health_alert"}
        try:
            r = requests.post("https://api.github.com/repos/tuyulfx/journal_vault_agi/dispatches",
                              headers=headers, json=payload)
            if r.status_code == 204:
                log_event("✅ Journal Repo menerima notifikasi reflektif (health alert).")
            else:
                log_event(f"⚠️ Gagal kirim alert ke Journal Repo: {r.status_code}")
        except Exception as e:
            log_event(f"❌ Error kirim notifikasi reflektif: {e}")


def main():
    log_event("🐺 Menjalankan Repo Health Monitor v5.7.2-HYBRID+ ...")

    token = os.getenv("GH_TOKEN") or os.getenv("HYBRID_REPO_TOKEN")
    latencies = check_latency()
    drifts = check_sync_delay()
    report = generate_health_report(latencies, drifts)
    notify_if_anomaly(report, token)

    log_event("✅ Repo Health Monitor selesai.\n")


if __name__ == "__main__":
    main()
