# TUYUL FX AGI HYBRID v5.7.3r++
"""Helper untuk keluaran log reflektif repo (RBP v2.2)."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class RepoOutputHelper:
    """Menyimpan hasil monitor ke journal repo dan output refleksi."""

    def __init__(
        self,
        base_dir: str = "journal",
        repo_output_path: str = "repo_outputs/journal_repo/reflection_output.json",
    ):
        self.base_dir = base_dir
        self.repo_output_path = repo_output_path
        Path(self.base_dir).mkdir(parents=True, exist_ok=True)
        Path(self.repo_output_path).parent.mkdir(parents=True, exist_ok=True)

    def append_log(self, filename: str, payload: Dict[str, Any]) -> Dict[str, str]:
        """Tambahkan satu entri JSON ke file log (newline-delimited)."""
        log_path = Path(filename) if os.path.isabs(filename) else Path(self.base_dir) / filename
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(payload) + "\n")
        return {"status": "written", "path": str(log_path)}

    def write(self, reflection_data: Dict[str, object], path: Optional[str] = None) -> Dict[str, str]:
        """Tulis snapshot refleksi tunggal ke file JSON (overwrite)."""
        target_path = Path(path) if path else Path(self.repo_output_path)
        reflection_data["timestamp"] = datetime.utcnow().isoformat()
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(reflection_data, f, indent=2)
        return {"status": "written", "path": str(target_path)}

    def read(self, path: Optional[str] = None) -> Dict[str, object]:
        """Baca file refleksi; kembalikan error bila tidak ada."""
        target_path = Path(path) if path else Path(self.repo_output_path)
        if not target_path.exists():
            return {"error": "Reflection file not found"}
        with open(target_path, encoding="utf-8") as f:
            return json.load(f)


__all__ = ["RepoOutputHelper"]
