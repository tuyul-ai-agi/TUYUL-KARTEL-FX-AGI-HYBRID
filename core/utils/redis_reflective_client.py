"""
Redis Reflective Bridge Client Utility (v5.7.3r++)
--------------------------------------------------
Provides publish/subscribe helpers for the TUYUL FX AGI Hybrid reflective bridge.
"""

import datetime
import json
import os

import redis
import yaml


# ===============================================================
# ⚙️ Load Redis Bridge Configuration
# ===============================================================
def load_redis_config(path="configs/redis_reflective_bridge.yml"):
    """Membaca konfigurasi Redis dari YAML."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)


# ===============================================================
# 🔗 Create Redis Client Connection
# ===============================================================
def get_reflective_client():
    """Inisialisasi koneksi Redis berdasarkan konfigurasi reflektif."""
    config = load_redis_config()
    redis_conf = config.get("redis", {})
    r = redis.Redis(
        host=redis_conf.get("host", "localhost"),
        port=redis_conf.get("port", 6379),
        db=redis_conf.get("db", 0),
        username=redis_conf.get("username", None),
        password=redis_conf.get("password", None),
        decode_responses=True,
        socket_timeout=10,
        retry_on_timeout=True,
    )
    print(f"[Bridge ✅] Connected to Redis Reflective Core ({config['bridge_protocol']})")
    return r, config


# ===============================================================
# 📡 Publish Reflective Event
# ===============================================================
def publish_reflective_event(
    channel, payload, origin_repo="Hybrid", conf12=None, integrity=None
):
    """
    Mengirim event reflektif antar repo dengan metadata lengkap.
    channel: nama channel Redis
    payload: data utama event (dict)
    origin_repo: repo pengirim (Hybrid / Knowledge / Kartel / Journal)
    conf12: optional, nilai confidence reflektif
    integrity: optional, indeks integritas saat event dikirim
    """
    try:
        r, config = get_reflective_client()

        event = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "origin_repo": origin_repo,
            "version": config["version"],
            "bridge_protocol": config["bridge_protocol"],
            "reflective_mode": config.get("reflective_mode", "adaptive_sync"),
            "payload": payload,
            "meta": {"conf12": conf12, "integrity": integrity},
        }

        r.publish(channel, json.dumps(event))
        print(f"[Bridge →] Event published → {channel} | Repo={origin_repo}")

    except Exception as e:
        print(f"[Bridge ERROR ❌] Failed to publish to {channel}: {e}")


# ===============================================================
# 🧭 Subscribe Listener (Optional)
# ===============================================================
def subscribe_reflective_channels(channels):
    """
    Mendengarkan channel reflektif Redis.
    Dapat digunakan oleh BOT TJX atau sistem monitoring.
    """
    r, _ = get_reflective_client()
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe(channels)
    print(f"[Bridge 🎧] Subscribed to: {', '.join(channels)}")

    for message in pubsub.listen():
        try:
            data = json.loads(message["data"])
            print(f"[Reflective Event] {data['origin_repo']} → {message['channel']}")
            print(f"  Payload: {json.dumps(data['payload'], indent=2)}\n")
        except Exception as e:
            print(f"[Bridge ERROR] {e}")


# ===============================================================
# 🧩 Example Usage
# ===============================================================
if __name__ == "__main__":
    payload = {"event": "sync_completed", "pair": "XAUUSD", "fusion_confidence": 0.874}
    publish_reflective_event(
        "hybrid_sync", payload, origin_repo="Hybrid", conf12=0.874, integrity=0.94
    )
