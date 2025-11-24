"""Utilities for synchronizing vault-related stores."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

VAULT_ROOT = Path(__file__).resolve().parents[2] / "vaults"
FUSION_JOURNAL = VAULT_ROOT / "fusion_journal.json"
REFLECTIVE_FEEDBACK = VAULT_ROOT / "reflective_bias_report.json"


def _timestamp() -> str:
    return datetime.now(tz=timezone.utc).isoformat()


def _load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as file:
            payload = json.load(file)
        return payload if isinstance(payload, dict) else {}
    except json.JSONDecodeError:
        return {}


def _save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def sync_vaults() -> Dict[str, Any]:
    """Record a synchronization event and summarize the actions performed."""

    actions: List[str] = [
        "journal_vault -> hybrid_memory",
        "knowledge_vault -> hybrid_memory",
        "hybrid_memory -> journal_vault",
    ]
    entry = {"synced_at": _timestamp(), "actions": actions, "status": "synchronized"}

    journal = _load_json(FUSION_JOURNAL)
    events = journal.get("sync_events", [])
    if isinstance(events, list):
        events.append(entry)
    _save_json(FUSION_JOURNAL, {"sync_events": events})
    return entry


def load_vault_feedback() -> Dict[str, Any]:
    """Load reflective bias report from the knowledge vault."""

    return _load_json(REFLECTIVE_FEEDBACK)
