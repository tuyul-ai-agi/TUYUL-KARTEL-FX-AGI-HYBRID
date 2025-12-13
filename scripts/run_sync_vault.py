"""
Run Sync Repo
-------------
Manual sync antar repos (Hybrid ↔ Knowledge ↔ Kartel ↔ Journal).
"""

from pipeline.quad_repo_sync_loop import QuadRepoSyncLoop

if __name__ == "__main__":
    sync = QuadRepoSyncLoop()
    result = sync.run()
    print("[SYNC RESULT]")
    print(result)
