import json
import redis
import yaml
import time
import threading
from datetime import datetime

# Core modules
from core.reflective.reflective_loop_handler import run_reflective_cycle
from core.repo.kartel_macro_bridge import get_macro_context
from core.journal.reflective_journal_sync import sync_to_journal
from core.utils.data_feed_adapter import load_price_volume


# ===============================================================
# 🔹 1️⃣ Load Redis Configuration
# ===============================================================
def load_bridge_config(config_path="configs/redis_reflective_bridge.yml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


# ===============================================================
# 🔹 2️⃣ Initialize Redis Client
# ===============================================================
def connect_reflective_redis(config):
    redis_conf = config["redis"]
    r = redis.Redis(
        host=redis_conf["host"],
        port=redis_conf["port"],
        db=redis_conf.get("db", 0),
        socket_timeout=10,
        retry_on_timeout=True
    )
    print(f"[Bridge] Connected to Redis Reflective Core (RBP {config['bridge_protocol']})")
    return r


# ===============================================================
# 🔹 3️⃣ Publish Reflective Events
# ===============================================================
def publish_reflective_event(r, channel, payload):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": payload
    }
    r.publish(channel, json.dumps(event))
    print(f"[Bridge→] Published reflective event → {channel}")


# ===============================================================
# 🔹 4️⃣ Listen for Commands from TUYULBOT / Other Repos
# ===============================================================
def listen_to_reflective_bridge(r, channels):
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe(channels)
    print(f"[Bridge] Listening to channels: {', '.join(channels)}")

    for message in pubsub.listen():
        try:
            data = json.loads(message["data"])
            event = data.get("event", {})
            print(f"[Reflective Event] Received → {event}")

            if event.get("command") == "run_cycle":
                pair = event.get("pair", "XAUUSD")
                handle_reflective_cycle(pair)
            elif event.get("command") == "sync_journal":
                handle_journal_sync()
            elif event.get("command") == "get_macro":
                handle_macro_broadcast()
            elif event.get("command") == "status":
                print("[Bridge] Reflective Bridge is alive ✅")

        except Exception as e:
            print(f"[Bridge ERROR] {e}")


# ===============================================================
# 🔹 5️⃣ Handle Reflective Cycle (TRQ3D → RGO → Fusion → Journal)
# ===============================================================
def handle_reflective_cycle(pair="XAUUSD"):
    print(f"🧠 [Cycle] Running Reflective Loop for {pair}")
    price, volume = load_price_volume(pair)
    result = run_reflective_cycle(price, volume, pair)
    sync_to_journal(result["entry"])
    print(f"✅ [Cycle Completed] {pair} → CONF₁₂={result['fusion']['conf12']} | RCAdj={result['fusion']['rcadj']}")


# ===============================================================
# 🔹 6️⃣ Handle Journal Sync Command
# ===============================================================
def handle_journal_sync():
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Manual reflective sync triggered",
        "reflective_version": "v5.7.3r++"
    }
    sync_to_journal(entry)
    print("[🧾] Manual reflective sync logged.")


# ===============================================================
# 🔹 7️⃣ Handle Macro Data Broadcast (Kartel Repo)
# ===============================================================
def handle_macro_broadcast():
    macro = get_macro_context()
    print(f"[🌍 Kartel] Broadcast: VIX={macro['VIX']} | RVI={macro['RVI']} | Regime={macro['GlobalRegime']}")
    return macro


# ===============================================================
# 🔹 8️⃣ Heartbeat Loop for Reflective Awareness
# ===============================================================
def reflective_heartbeat(r, config):
    interval = config["redis"]["heartbeat_interval_sec"]
    while True:
        payload = {
            "status": "alive",
            "timestamp": datetime.utcnow().isoformat(),
            "integrity_check": get_macro_context()["integrity_index"]
        }
        publish_reflective_event(r, "hybrid_sync", payload)
        time.sleep(interval)


# ===============================================================
# 🔹 9️⃣ Main Runtime Loop
# ===============================================================
def start_reflective_bridge():
    config = load_bridge_config()
    r = connect_reflective_redis(config)

    # Channels yang aktif
    channels = list(config["channels"].keys())

    # Start listener thread
    listener_thread = threading.Thread(target=listen_to_reflective_bridge, args=(r, channels))
    listener_thread.daemon = True
    listener_thread.start()

    # Start heartbeat
    heartbeat_thread = threading.Thread(target=reflective_heartbeat, args=(r, config))
    heartbeat_thread.daemon = True
    heartbeat_thread.start()

    print("🚀 Reflective Bridge Runtime Started (v5.7.3r++) ✅")
    print("Listening and syncing across Hybrid–Knowledge–Kartel–Journal...\n")

    # Keep alive
    while True:
        time.sleep(5)


# ===============================================================
# 🔹 10️⃣ Entrypoint
# ===============================================================
if __name__ == "__main__":
    try:
        start_reflective_bridge()
    except KeyboardInterrupt:
        print("\n🧠 Reflective Bridge gracefully stopped.")
