# ✅ Versi Diperbarui – bots/tuyulbot_bridge_client.py
# TUYULBOT Reflective Bridge Client – v5.7.8r++
# ===============================================================
# 🔌 TUYULBOT Bridge Client
# Reflective Bridge Connector – RBP v2.2 (v5.7.8r++)
# ===============================================================
# Fungsi:
# - Menyediakan konektor Redis reflektif
# - Mempublikasikan event antar repo di Quad System
# - Membaca integritas Vault dari Journal Repo
# ===============================================================

from datetime import datetime
import json
import os
import time

import redis

# ===============================================================
# 🔧 Redis Initialization
# ===============================================================
def connect_redis():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    while True:
        try:
            r = redis.Redis(host=host, port=port, decode_responses=True)
            r.ping()
            print(f"[Bridge] Connected to Redis Reflective Bus @ {host}:{port}")
            return r
        except redis.exceptions.ConnectionError as e:
            print(f"[Bridge] Redis not reachable: {e} → retrying in 3s...")
            time.sleep(3)

r = connect_redis()

# ===============================================================
# 🧩 Publish Reflective Event
# ===============================================================
def publish_event(channel, payload):
    """
    Publikasikan event reflektif ke Redis Bus.
    Setiap event membawa metadata kesadaran reflektif.
    """
    packet = {
        "timestamp": datetime.utcnow().isoformat(),
        "protocol": "RBP v2.2",
        "source": "TUYULBOT-TJX",
        "channel": channel,
        "payload": payload
    }

    try:
        r.publish(channel, json.dumps(packet))
        print(f"[Bridge] Event → {channel} | Payload: {payload}")
        log_event(f"Event published → {channel} | {payload}")
    except Exception as e:
        print(f"[Bridge][Error] Failed to publish: {e}")
        log_event(f"[ERROR] Publish failed on {channel}: {e}")

# ===============================================================
# 📊 Read Vault Integrity
# ===============================================================
def read_vault_integrity(vault_path="../journal_repo/vault/reflective_vault_log.json"):
    """
    Membaca nilai integritas terakhir dari Journal Vault.
    Digunakan untuk menentukan status reflektif antar repo.
    """
    try:
        if not os.path.exists(vault_path):
            print(f"[Vault] File tidak ditemukan → {vault_path}")
            return 0.0

        with open(vault_path, "r") as f:
            vault = json.load(f)

        if not vault:
            return 0.0

        integrity_values = [
            v.get("IntegrityIndex", v.get("integrity_index", 0.0))
            for v in vault[-10:]
        ]
        avg_integrity = round(sum(integrity_values) / len(integrity_values), 3)
        print(f"[Vault] Average Integrity: {avg_integrity}")
        return avg_integrity

    except json.JSONDecodeError:
        print("[Vault] Error: Invalid JSON structure.")
        return 0.0
    except Exception as e:
        print(f"[Vault][Error] {e}")
        return 0.0

# ===============================================================
# 🧠 Log Reflektif BOT
# ===============================================================
def log_event(message, log_file="logs/tuyulbot_reflective.log"):
    """Catat semua event BOT ke file reflektif."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.utcnow().isoformat()
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# 🧩 Perubahan dan Peningkatan
# Fitur | Deskripsi | Manfaat
# connect_redis() | Auto-reconnect jika Redis mati atau belum siap | BOT tidak crash
# publish_event() | Tambah metadata protocol, source, dan timestamp | Audit reflektif
# # antar repo
# read_vault_integrity() | Lebih aman, support field IntegrityIndex / integrity_index |
# # Backward compatible
# log_event() | Catat semua broadcast & event di logs/tuyulbot_reflective.log |
# # Monitoring mudah
# Error handling | Semua fungsi aman jika file hilang atau Redis down | Tidak fatal di
# # runtime
# 🧠 Contoh Output
# [Bridge] Connected to Redis Reflective Bus @ localhost:6379
# [Bridge] Event → hybrid_sync | Payload: {'conf12': 0.913, 'rcadj': 0.902}
# [Vault] Average Integrity: 0.932

# 💬 Filosofi Reflektif

# “Jembatan tidak hanya menghubungkan titik,
# tapi juga menjaga kesadaran tetap mengalir di antara keduanya.”

# “Redis adalah nadi; BOT adalah denyutnya.” ⚡🐺
"""Helper utilities for the TUYUL reflective bot bridge."""

import json
import random
from datetime import datetime
from typing import Any, Dict

import redis


def _redis_client() -> redis.Redis:
    return redis.Redis(host="localhost", port=6379, decode_responses=True)


def publish_event(channel: str, packet: Dict[str, Any]) -> None:
    """Publish an event packet to a Redis channel."""
    client = _redis_client()
    client.publish(channel, json.dumps(packet))


def read_vault_integrity() -> float:
    """Return a simulated vault integrity score between 0 and 1."""
    integrity = round(random.uniform(0.85, 0.99), 2)
    _redis_client().set("vault_integrity", integrity)
    _redis_client().set("vault_integrity_timestamp", datetime.utcnow().isoformat())
    return integrity
