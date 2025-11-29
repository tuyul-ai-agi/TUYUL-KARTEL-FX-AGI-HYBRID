"""
Vault Sync v5.4.0
-----------------
Sinkronisasi vault AGI (FX, Kartel, Journal) dengan verifikasi integritas file JSON.
"""

from __future__ import annotations

import hashlib
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class VaultSync:
    """Sinkronisasi dan verifikasi integritas file vault."""

    def __init__(self, base_path: str = "vaults/") -> None:
        self.base_path = Path(base_path)
        self.vaults = ["fx_vault", "kartel_vault", "journal_vault"]
        self.log_path = Path("logs") / "vault_sync.log"
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def compute_hash(self, file_path: Path) -> str:
        """Hitung SHA256 hash untuk file."""

        with file_path.open("rb") as file:
            return hashlib.sha256(file.read()).hexdigest()

    def sync(self) -> List[Dict[str, str]]:
        """Sinkronisasi seluruh vault dan kembalikan laporan hash."""

        report: List[Dict[str, str]] = []
        for vault in self.vaults:
            vault_path = self.base_path / vault
            if not vault_path.exists():
                continue
            for filename in os.listdir(vault_path):
                if filename.endswith(".json"):
                    full_path = vault_path / filename
                    file_hash = self.compute_hash(full_path)
                    report.append({"vault": vault, "file": filename, "hash": file_hash})
        with self.log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.utcnow()}] Synced {len(report)} files.\n")
        return report
