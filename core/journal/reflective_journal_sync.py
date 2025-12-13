"""Sync reflective journal entries to the journal repository."""

from __future__ import annotations

import datetime
import json
import os
from typing import Any, Dict


def _resolve_integrity_tag(entry: Dict[str, Any]) -> Any:
    if "integrity_tag" in entry:
        return entry["integrity_tag"]
    if "integrity_index" in entry:
        return entry["integrity_index"]
    if "IntegrityIndex" in entry:
        return entry["IntegrityIndex"]
    return 0.9


def sync_to_journal(
    entry: Dict[str, Any], repo_path: str = "../repos/journal_repo/reflective_log.json"
) -> None:
    """Persist a reflective entry to the journal repository."""

    entry["sync_time"] = datetime.datetime.utcnow().isoformat()
    entry["reflective_version"] = "v5.7.3r++"
    entry["sync_mode"] = "QuadRepo"
    entry["repo_origin"] = "Hybrid"
    entry["integrity_tag"] = _resolve_integrity_tag(entry)

    os.makedirs(os.path.dirname(repo_path), exist_ok=True)

    if os.path.exists(repo_path):
        with open(repo_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(repo_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"[REPO ✅] Reflective Commit synced @ {entry['sync_time']} → {repo_path}")
