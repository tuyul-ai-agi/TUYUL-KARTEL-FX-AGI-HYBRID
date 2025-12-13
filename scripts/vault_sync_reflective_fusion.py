"""
Repo Sync Reflective Fusion
---------------------------
Sinkronisasi repos dan jalankan refleksi AGI Hybrid sekaligus.
"""

from pipeline.quad_repo_sync_loop import QuadRepoSyncLoop
from pipeline.wolf_reflective_loop import WolfReflectiveLoop

if __name__ == "__main__":
    sync = QuadRepoSyncLoop()
    reflective = WolfReflectiveLoop()
    sync_result = sync.run()
    reflection = reflective.run()
    print("✅ Vault Sync and Reflection Done")
    print(sync_result, reflection)
