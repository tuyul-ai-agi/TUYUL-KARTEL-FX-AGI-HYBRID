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
