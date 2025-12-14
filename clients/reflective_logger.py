import datetime
import json
import os


class ReflectiveLogger:
    LOG_PATH = "logs/reflective_telemetry.json"
    MAX_ENTRIES = 100

    @staticmethod
    def log(event_type, payload):
        os.makedirs("logs", exist_ok=True)
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "event_type": event_type,
            "payload": payload,
        }

        logs = []
        if os.path.exists(ReflectiveLogger.LOG_PATH):
            try:
                with open(ReflectiveLogger.LOG_PATH, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except (json.JSONDecodeError, OSError):
                logs = []  # reset corrupted log to keep pipeline running

        logs.append(entry)
        with open(ReflectiveLogger.LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(logs[-ReflectiveLogger.MAX_ENTRIES :], f, indent=2)
        print(f"🧾 [ReflectiveLogger] Event logged: {event_type}")
