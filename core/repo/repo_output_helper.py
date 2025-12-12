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
