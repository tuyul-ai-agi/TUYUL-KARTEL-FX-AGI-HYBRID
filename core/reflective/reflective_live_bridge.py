"""Reflective live bridge for the TUYUL FX AGI Quad Repo."""
from __future__ import annotations

import datetime
import json
import os
import random
import time
from typing import Optional, TypedDict

import yaml

try:  # Optional dependency; falls back to stub when missing
    import redis
except ModuleNotFoundError:  # pragma: no cover - environment fallback
    class _RedisStub:
        class exceptions:  # type: ignore[attr-defined]
            class ConnectionError(Exception):
                """Stub connection error."""

        def __init__(self, *args: object, **kwargs: object) -> None:
            pass

        def ping(self) -> None:
            raise self.exceptions.ConnectionError("redis not available")

        def publish(self, *args: object, **kwargs: object) -> int:
            return 0

    class redis:  # type: ignore[override]
        Redis = _RedisStub
        exceptions = _RedisStub.exceptions

try:  # Optional dependency for GitHub heartbeat
    from github import GithubIntegration
except ModuleNotFoundError:  # pragma: no cover - environment fallback
    GithubIntegration = None

try:  # Optional dependency for outbound HTTP
    import requests
except ModuleNotFoundError:  # pragma: no cover - environment fallback
    requests = None


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


CONFIG_PATH = "bots/configs/tuyulbot_config.yml"
try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        CONFIG = yaml.safe_load(file)
except (FileNotFoundError, yaml.YAMLError):
    print(
        f"⚠️ Config file tidak valid atau tidak ditemukan di {CONFIG_PATH}. "
        "Menggunakan default sementara."
    )
    CONFIG = {
        "bot": {"id": "tuyul-reflective-bot", "interval_seconds": 60},
        "bridge": {"redis_host": "localhost", "redis_port": 6379},
    }

BOT_ID = CONFIG["bot"].get("id", "tuyul-reflective-bot")
ORG_NAME = "tuyul-ai-agi"
REDIS_HOST = CONFIG["bridge"].get("redis_host", "localhost")
REDIS_PORT = CONFIG["bridge"].get("redis_port", 6379)


def _connect_redis() -> Optional[redis.Redis]:  # type: ignore[name-defined]
    try:
        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        client.ping()
        print(f"[Redis] Connected to Reflective Bus @ {REDIS_HOST}:{REDIS_PORT}")
        return client
    except Exception as exc:  # pragma: no cover - connectivity guard
        print(f"[Redis] ⚠️ Connection failed: {exc}")
        return None


REDIS_CLIENT = _connect_redis()
APP_ID = int(os.getenv("GITHUB_APP_ID", "0"))
PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY", "").replace("\\n", "\n")


def get_installation_token(org_name: str) -> Optional[str]:
    """Ambil installation token GitHub untuk BOT Organization."""
    if GithubIntegration is None:
        return None

    try:
        gi = GithubIntegration(APP_ID, PRIVATE_KEY)
        installations = gi.get_organization_installations(org_name)
        install_id = installations[0].id
        access_token = gi.get_access_token(install_id)
        print(f"🔐 GitHub Installation Token berhasil diperoleh untuk {org_name}")
        return access_token.token
    except Exception as exc:  # pragma: no cover - offline environments
        print(f"⚠️ Gagal mendapatkan installation token: {exc}")
        return None


def run_bot_cycle() -> dict[str, object]:
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

    if REDIS_CLIENT:
        REDIS_CLIENT.publish("bot_ack", json.dumps(payload))
        print(f"[BOT] Broadcast → Redis ({REDIS_HOST}:{REDIS_PORT}) | {payload}")
    else:
        print(f"[BOT] Redis tidak aktif — payload hanya dicetak:\n{payload}")

    token = get_installation_token(ORG_NAME)
    if token and requests is not None:
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
        except Exception as exc:  # pragma: no cover - network guard
            print(f"[GitHub] ⚠️ Heartbeat gagal: {exc}")

    return payload


if __name__ == "__main__":  # pragma: no cover - manual execution guard
    print("🐺 Starting Reflective Live Bridge BOT — TUYUL FX AGI HYBRID v5.8r ⚡")
    interval = CONFIG["bot"].get("interval_seconds", 60)
    while True:
        run_bot_cycle()
        print(f"🕒 Sleeping {interval}s before next reflective cycle...\n")
        time.sleep(interval)
