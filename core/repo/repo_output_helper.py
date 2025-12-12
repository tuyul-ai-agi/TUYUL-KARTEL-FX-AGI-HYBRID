# TUYUL FX AGI HYBRID v5.7.3r++
"""Helper untuk keluaran log reflektif repo."""

import json
import os
from typing import Any, Dict


class RepoOutputHelper:
    """Menyimpan hasil monitor ke journal repo."""

    def __init__(self, base_dir: str = "journal"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def append_log(self, filename: str, payload: Dict[str, Any]):
        if os.path.isabs(filename):
            log_path = filename
        else:
            log_path = os.path.join(self.base_dir, filename)

        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(payload) + "\n")

        return {"status": "written", "path": log_path}


__all__ = ["RepoOutputHelper"]
"""Repo Output Helper — RBP v2.2
Menulis hasil refleksi ke keluaran repo adaptif.
"""

import json
import os
from datetime import datetime
from typing import Dict


class RepoOutputHelper:
    def __init__(self, repo_output_path: str = "repo_outputs/journal_repo/reflection_output.json"):
        self.repo_output_path = repo_output_path
        os.makedirs(os.path.dirname(self.repo_output_path), exist_ok=True)

    def write(self, reflection_data: Dict[str, object]) -> Dict[str, object]:
        reflection_data["timestamp"] = datetime.utcnow().isoformat()
        with open(self.repo_output_path, "w") as f:
            json.dump(reflection_data, f, indent=2)
        return {"status": "written", "path": self.repo_output_path}

    def read(self) -> Dict[str, object]:
        if not os.path.exists(self.repo_output_path):
            return {"error": "Reflection file not found"}
        with open(self.repo_output_path) as f:
            return json.load(f)
