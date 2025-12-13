import datetime
import os


def reflective_log(message: str) -> None:
    """Catat aktivitas reflektif ke log."""
    os.makedirs("logs", exist_ok=True)
    with open("logs/reflective_activity.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.utcnow().isoformat()}Z] {message}\n")
    print(f"🪶 Log reflektif: {message}")


if __name__ == "__main__":
    reflective_log("startup")
