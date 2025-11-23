import json
from pathlib import Path
from datetime import datetime


VAULT_PATH = Path(__file__).resolve().parents[2] / "vaults" / "reflection_output.json"


def _load_reports():
    if not VAULT_PATH.exists():
        return {"reflections": []}
    try:
        with VAULT_PATH.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"reflections": []}


def save_reflection_report(report: dict):
    payload = _load_reports()
    payload.setdefault("reflections", []).append(
        {"timestamp": datetime.utcnow().isoformat(), **report}
    )
    VAULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with VAULT_PATH.open("w") as file:
        json.dump(payload, file, indent=2)
    return payload
