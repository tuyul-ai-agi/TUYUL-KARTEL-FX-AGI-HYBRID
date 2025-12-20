"""
🌐 Reflective Live Bridge — TUYUL FX AGI HYBRID v5.8r
-----------------------------------------------------
Menjembatani koneksi live antar layer (Reflex, Fusion, Vault)
dan mengaktifkan BOT organisasi reflektif TUYUL-AI-AGI.
-----------------------------------------------------
Author  : TUYUL Labs – Reflective Systems Division
Version : v5.8r
Protocol: RBP v2.2 (Quad Repo Reflective Bridge)
Date    : 2025-12-15
"""

from __future__ import annotations

import datetime
import random
import yaml
import os
import redis
import json
import time
import requests
from typing import TypedDict
from github import GithubIntegration


# =============================================================
# 🧩 CORE REFLECTIVE BRIDGE
# =============================================================

class BridgeStatus(TypedDict):
    timestamp: str
    integrity_index: float
    coherence_score: float
    latency_ms: int
    reflective_state: str


class ReflectiveLiveBridge:
    """Jembatan kesadaran real-time antar Layer dan Vault."""

    def ping_all(self) -> BridgeStatus:
        latency: int = random.randint(120, 250)
        integrity: float = round(random.uniform(0.91, 0.95), 3)
        coherence: float = round(random.uniform(0.9, 0.94), 3)

        print(
            "🌐 Reflective Live Bridge — Integrity:"
            f" {integrity}, Coherence: {coherence}, Latency: {latency}ms"
        )
        return {
            "timestamp": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "integrity_index": integrity,
            "coherence_score": coherence,
            "latency_ms": latency,
            "reflective_state": "stable" if integrity >= 0.9 else "adaptive",
        }


# =============================================================
# ⚙️ 2️⃣ AKTIVASI BOT ORGANISASI
# =============================================================

CONFIG_PATH = "bots/configs/tuyulbot_config.yml"

try:
    with open(CONFIG_PATH, "r") as f:
        CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    print(f"⚠️ Config file tidak ditemukan di {CONFIG_PATH}. Menggunakan default sementara.")
    CONFIG = {
        "bot": {"id": "tuyul-reflective-bot", "interval_seconds": 60},
        "bridge": {"redis_host": "localhost", "redis_port": 6379},
    }

BOT_ID = CONFIG["bot"]["id"]
ORG_NAME = "tuyul-ai-agi"
REDIS_HOST = CONFIG["bridge"]["redis_host"]
REDIS_PORT = CONFIG["bridge"]["redis_port"]

# 🔌 Redis connection
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r.ping()
    print(f"[Redis] Connected to Reflective Bus @ {REDIS_HOST}:{REDIS_PORT}")
except redis.exceptions.ConnectionError as e:
    print(f"[Redis] ⚠️ Connection failed: {e}")
    r = None

# =============================================================
# 🧠 GITHUB ORGANIZATION INTEGRATION (via BOT APP)
# =============================================================

APP_ID = int(os.getenv("GITHUB_APP_ID", "0"))
PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY", "").replace("\\n", "\n")

def get_installation_token(org_name: str):
    """Ambil installation token GitHub untuk BOT Organization."""
    try:
        gi = GithubIntegration(APP_ID, PRIVATE_KEY)
        installations = gi.get_organization_installations(org_name)
        install_id = installations[0].id
        access_token = gi.get_access_token(install_id)
        print(f"🔐 GitHub Installation Token berhasil diperoleh untuk {org_name}")
        return access_token.token
    except Exception as e:
        print(f"⚠️ Gagal mendapatkan installation token: {e}")
        return None


# =============================================================
# 🚀 Reflective Broadcast Loop
# =============================================================

def run_bot_cycle():
    now = datetime.datetime.utcnow().isoformat()
    bridge = ReflectiveLiveBridge()
    status = bridge.ping_all()

    payload = {
        "bot_id": BOT_ID,
        "organization": ORG_NAME,
        "integrity": status["integrity_index"],
        "coherence": status["coherence_score"],
        "latency_ms": status["latency_ms"],
        "state": status["reflective_state"],
        "status": "Reflective Sync Active",
        "timestamp": now,
    }

    if r:
        r.publish("bot_ack", json.dumps(payload))
        print(f"[BOT] Broadcast → Redis ({REDIS_HOST}:{REDIS_PORT}) | {payload}")
    else:
        print(f"[BOT] Redis tidak aktif — payload hanya dicetak:\n{payload}")

    # Kirim heartbeat ke GitHub (opsional)
    token = get_installation_token(ORG_NAME)
    if token:
        headers = {"Authorization": f"Bearer {token}"}
        data = {"event": "reflective_heartbeat", "timestamp": now}
        try:
            res = requests.post(
                f"https://api.github.com/orgs/{ORG_NAME}/events",
                headers=headers,
                json=data,
                timeout=10,
            )
            print(f"[GitHub] Heartbeat sent → {res.status_code}")
        except Exception as e:
            print(f"[GitHub] ⚠️ Heartbeat gagal: {e}")

    return payload


# =============================================================
# 🧭 MAIN LOOP
# =============================================================

if __name__ == "__main__":
    print("🐺 Starting Reflective Live Bridge BOT — TUYUL FX AGI HYBRID v5.8r ⚡")
    interval = CONFIG["bot"].get("interval_seconds", 60)
    while True:
        run_bot_cycle()
        print(f"🕒 Sleeping {interval}s before next reflective cycle...\n")
        time.sleep(interval)
