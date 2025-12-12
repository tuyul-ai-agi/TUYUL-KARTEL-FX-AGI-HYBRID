"""Tri Repo Sync Loop
---------------------
Sinkronisasi adaptif antar Repo melalui Reflective Bridge Protocol.
"""

from typing import Optional

from core.repo.repo_bridge_manager import RepoBridgeManager


class TriRepoSyncLoop:
    def __init__(self, bridge_manager: Optional[RepoBridgeManager] = None):
        self.bridge_manager = bridge_manager or RepoBridgeManager()

    def run(self):
        sync_result = self.bridge_manager.sync_repos()
        return {"quad_repo_bridge": sync_result}


# Backward compatibility for legacy callers
TriVaultSyncLoop = TriRepoSyncLoop
