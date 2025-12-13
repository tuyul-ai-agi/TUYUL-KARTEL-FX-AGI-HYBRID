# ===============================================================
# 🎧 TUYULBOT Reflective Event Listener
# Version: v5.7.8r++
# ===============================================================
# Fungsi:
# - Mendengarkan event reflektif dari channel Redis (RBP v2.2)
# - Menerjemahkan command reflektif ke aksi BOT
# - Memberi respon balik ke Redis Bridge (status, ack)
# ===============================================================

import json
import os
import time
from datetime import datetime

import redis

from bots.tuyulbot_commands import interpret_command

LOG_PATH = "logs/tuyulbot_listener.log"

# ===============================================================
# 🔌 Connect ke Redis Reflective Bus
# ===============================================================
def connect_redis():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    while True:
        try:
            r = redis.Redis(host=host, port=port, decode_responses=True)
            r.ping()
            print(f"[Listener] Connected to Redis @ {host}:{port}")
            return r
        except redis.exceptions.ConnectionError as e:
            print(f"[Listener][WARN] Redis unreachable: {e}")
            time.sleep(3)


r = connect_redis()
sub = r.pubsub(ignore_subscribe_messages=True)
sub.subscribe("bot_command", "hybrid_sync", "journal_commit")


# ===============================================================
# 🧠 Logging Utility
# ===============================================================
def log_event(msg):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.utcnow().isoformat()}] {msg}\n")
    print(f"[Listener] {msg}")


# ===============================================================
# 📡 Send ACK Response Back to Redis
# ===============================================================
def send_ack(channel, command, result):
    ack_payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": "TUYULBOT-TJX",
        "protocol": "RBP v2.2",
        "ack_for": command,
        "result": result,
    }
    r.publish("bot_ack", json.dumps(ack_payload))
    log_event(f"ACK sent for command → {command}")


# ===============================================================
# 🔁 Reflective Event Listener Main Loop
# ===============================================================
def start_listener():
    print("[BOT] 🧠 Reflective Listener Active — awaiting commands...")
    log_event("Reflective Listener started (RBP v2.2)")

    for msg in sub.listen():
        try:
            data = json.loads(msg["data"]) if isinstance(msg["data"], str) else msg["data"]
            channel = msg["channel"]

            # Extract command text safely
            cmd_text = None
            if isinstance(data, dict):
                cmd_text = data.get("text") or data.get("payload", {}).get("command")
            if not cmd_text:
                log_event(f"⚠️ Invalid command payload: {data}")
                continue

            # Interpret command
            result = interpret_command(cmd_text)
            log_event(f"Command received from [{channel}] → {cmd_text}")
            log_event(f"→ Action: {result['action']} | Desc: {result['desc']}")

            # Send ACK response to Redis
            send_ack(channel, cmd_text, result)

        except json.JSONDecodeError:
            log_event("⚠️ Invalid JSON payload received.")
        except Exception as e:
            log_event(f"[ERROR] Listener exception: {e}")
            time.sleep(1)


# ===============================================================
# 🚀 ENTRY POINT
# ===============================================================
if __name__ == "__main__":
    try:
        start_listener()
    except KeyboardInterrupt:
        log_event("Reflective Listener stopped manually.")
    except Exception as e:
        log_event(f"[CRITICAL] Listener crashed: {e}")
        time.sleep(3)
        start_listener()
