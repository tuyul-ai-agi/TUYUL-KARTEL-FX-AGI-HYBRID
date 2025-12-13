import datetime
import json
import os

from tools.hybrid_balance_controller import balance_control


def log_balance() -> None:
    data = balance_control()
    os.makedirs("journal_repo", exist_ok=True)
    data["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
    with open("journal_repo/hybrid_balance_log.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ Hybrid Balance log tersimpan.")


if __name__ == "__main__":
    log_balance()
