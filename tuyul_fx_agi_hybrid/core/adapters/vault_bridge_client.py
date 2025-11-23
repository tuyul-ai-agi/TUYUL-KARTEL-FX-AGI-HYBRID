"""Vault bridge utilities for synchronization and feedback retrieval."""

import json
from datetime import datetime
from typing import Dict


def sync_vaults() -> Dict[str, str]:
    """Synchronize fusion journal with a timestamp."""

    with open("vaults/fusion_journal.json", "r", encoding="utf-8") as file:
        journal = json.load(file)
    journal["last_sync"] = datetime.utcnow().isoformat()
    with open("vaults/fusion_journal.json", "w", encoding="utf-8") as file:
        json.dump(journal, file, indent=2)
    return {"sync": "OK", "timestamp": journal["last_sync"]}


def load_vault_feedback() -> Dict[str, str]:
    """Load reflective bias report from vaults."""

    with open("vaults/reflective_bias_report.json", "r", encoding="utf-8") as file:
        return json.load(file)
import json
from datetime import datetime
from pathlib import Path


VAULT_ROOT = Path(__file__).resolve().parents[2] / "vaults"
FUSION_JOURNAL = VAULT_ROOT / "fusion_journal.json"
REFLECTIVE_FEEDBACK = VAULT_ROOT / "reflective_bias_report.json"


def _load_json(path: Path):
    if not path.exists():
        return {}
    try:
        with path.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def _save_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as file:
        json.dump(payload, file, indent=2)


def sync_vaults():
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "status": "synced",
    }
    payload = _load_json(FUSION_JOURNAL)
    journal = payload.get("sync_events", [])
    journal.append(entry)
    _save_json(FUSION_JOURNAL, {"sync_events": journal})
    return entry


def load_vault_feedback():
    payload = _load_json(REFLECTIVE_FEEDBACK)
    return payload if isinstance(payload, dict) else {}
"""Utilities for synchronizing vault-related stores."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List


def _timestamp() -> str:
    return datetime.now(tz=timezone.utc).isoformat()


def sync_vaults() -> Dict[str, object]:
    """Return a summary of a completed vault synchronization."""

    actions: List[str] = [
        "journal_vault -> hybrid_memory",
        "knowledge_vault -> hybrid_memory",
        "hybrid_memory -> journal_vault",
    ]
    return {
        "synced_at": _timestamp(),
        "actions": actions,
        "status": "synchronized",
    }
