# ===============================================================
# 🎧 TUYULBOT Reflective Event Listener
# Version: v6.0
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

from bots.tuyulbot_commands import TUYULBotCommands

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

    cmd = TUYULBotCommands()
    event_log = "logs/tuyulbot_events.json"

    while True:
        try:
            event = {"timestamp": datetime.utcnow().isoformat(), "event": "reflective_ping"}
            json.dump(event, open(event_log, "a"))
            print("🔔 Event detected: reflective_ping")
            cmd.execute("reflect")

            time.sleep(900)

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
