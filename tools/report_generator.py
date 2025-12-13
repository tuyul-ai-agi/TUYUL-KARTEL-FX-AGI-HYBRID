import datetime
import json


def generate_daily_report() -> None:
    with open("journal_repo/quad_repo_sync.json", "r", encoding="utf-8") as f:
        sync = json.load(f)
    report = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "integrity_index": sync["integrity_index"],
        "coherence_drift": sync["coherence_drift"],
    }
    with open("docs/daily_reflective_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("✅ Daily Reflective Report generated.")


if __name__ == "__main__":
    generate_daily_report()
