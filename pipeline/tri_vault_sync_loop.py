# ============================================================
# 🔗 TUYUL FX AGI v5.7.8 – Tri Repo Sync Loop
# ------------------------------------------------------------
# Sinkronisasi adaptif antar repo melalui Reflective Bridge Protocol.
# ============================================================

from datetime import datetime
import json
import time
from pathlib import Path
from typing import Optional

from core.repo.repo_bridge_manager import RepoBridgeManager

LOG_FILE = Path("logs/tri_vault_sync_loop.log")


def tri_repo_sync_loop(interval_minutes: int = 10) -> None:
    """Menjalankan sinkronisasi tri-vault secara berkala."""

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    print("🔗 Starting Tri Repo Sync Loop v5.7.8...")
    bridge_manager = RepoBridgeManager()

    while True:
        sync_result = bridge_manager.sync_repos()
        _save_sync_log(sync_result)
        print(
            f"🕒 Menunggu {interval_minutes} menit sebelum sinkronisasi berikutnya...\n"
        )
        time.sleep(interval_minutes * 60)


def _save_sync_log(sync_result: dict) -> None:
    journal_dir = Path("journal_repo")
    journal_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "quad_repo_bridge": sync_result,
    }

    status_path = journal_dir / "tri_repo_sync_status.json"
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{payload['timestamp']}] sync={sync_result}\n")

    print("✅ Tri-repo sync report saved → journal_repo/tri_repo_sync_status.json")


class TriRepoSyncLoop:
    def __init__(self, bridge_manager: Optional[RepoBridgeManager] = None):
        self.bridge_manager = bridge_manager or RepoBridgeManager()

    def run(self) -> dict:
        sync_result = self.bridge_manager.sync_repos()
        return {"quad_repo_bridge": sync_result}


# Backward compatibility for legacy callers
TriVaultSyncLoop = TriRepoSyncLoop


if __name__ == "__main__":
    tri_repo_sync_loop()
"""Legacy Tri Vault Sync Loop wrapper."""

from pipeline.quad_repo_sync_loop import (
    QuadRepoSyncLoop,
    TriRepoSyncLoop,
    TriVaultSyncLoop,
    quad_repo_sync_loop,
)

__all__ = [
    "QuadRepoSyncLoop",
    "TriRepoSyncLoop",
    "TriVaultSyncLoop",
    "quad_repo_sync_loop",
]
