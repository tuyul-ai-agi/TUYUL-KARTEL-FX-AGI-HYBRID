"""
Run Sync Repo
-------------
Manual sync antar repos (Hybrid ↔ Knowledge ↔ Kartel ↔ Journal).
"""

from pipeline.tri_vault_sync_loop import TriRepoSyncLoop

if __name__ == "__main__":
    sync = TriRepoSyncLoop()
    result = sync.run()
    print("[SYNC RESULT]")
    print(result)
