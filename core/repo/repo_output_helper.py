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
