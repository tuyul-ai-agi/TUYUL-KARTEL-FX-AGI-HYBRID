"""
GPT Bridge Handler v5.8r++
----------------------------
Menghubungkan GPT Reasoning ↔ Fusion–Reflective Engine.
Menambahkan konteks organisasi GitHub (tuyul-ai-agi) ke GPT Memory.
"""

import json
import os
import requests
from datetime import datetime
from modules.montecarlo_engine_v22 import simulate_price_paths


# =============================================================
# 🧩 GPT Bridge Core
# =============================================================

class GPTBridgeHandler:
    def __init__(self):
        self.version = "v5.8r++"

    def process_signal(self, message: str, prices: list[float]):
        """Memproses sinyal reflektif melalui Monte Carlo Engine."""
        mc_result = simulate_price_paths(prices)
        response = {
            "message": message,
            "reflection": "Reflex–Fusion–Reflective processed",
            "montecarlo": mc_result,
            "bridge_version": "RBP v2.2",
            "timestamp": datetime.utcnow().isoformat(),
        }

        os.makedirs("logs", exist_ok=True)
        with open("logs/gpt_bridge.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(response) + "\n")
        print(f"🧠 GPT Bridge processed signal: {message}")
        return response


# =============================================================
# 🧠 3️⃣ PENAMBAHAN ORGANIZATION CONTEXT KE GPT
# =============================================================

ORG = "tuyul-ai-agi"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def list_org_repos():
    """Ambil daftar semua repository dari organisasi GitHub."""
    url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code != 200:
        print(f"⚠️ Gagal mengambil daftar repos ({response.status_code}): {response.text}")
        return []
    return [repo["full_name"] for repo in response.json()]


def get_repo_files(repo):
    """Ambil semua file di branch main dari repo tertentu."""
    url = f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code != 200:
        print(f"⚠️ Gagal membaca file dari {repo}: {response.text}")
        return []
    data = response.json()
    return [item["path"] for item in data.get("tree", []) if item["type"] == "blob"]


def sync_org_context():
    """Sinkronisasi seluruh struktur organisasi ke GPT memory context."""
    print("🔁 Menyinkronkan struktur organisasi GitHub → GPT Context...")
    repos = list_org_repos()
    context = {}

    for r in repos:
        context[r] = get_repo_files(r)

    os.makedirs("knowledge", exist_ok=True)
    with open("knowledge/org_context.json", "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2)

    print(f"📦 Organization structure synced → {len(repos)} repos updated.")
    return context


# =============================================================
# 🧭 Entry Point
# =============================================================

if __name__ == "__main__":
    print("🐺 Starting GPT Bridge Handler v5.8r++ — Reflective Org Sync Mode ⚡")
    handler = GPTBridgeHandler()

    # Contoh simulasi sinyal GPT
    test_signal = handler.process_signal("analyze fusion EURUSD H4", [1.084, 1.086, 1.088])
    print(f"✅ Reflective Result → {test_signal['bridge_version']}")

    # Jalankan sinkronisasi organisasi
    if GITHUB_TOKEN:
        sync_org_context()
    else:
        print("⚠️ Environment variable GITHUB_TOKEN tidak ditemukan — lewati sync.")
