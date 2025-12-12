"""
Repo Sync Reflective Fusion
---------------------------
Sinkronisasi repos dan jalankan refleksi AGI Hybrid sekaligus.
"""

from pipeline.tri_vault_sync_loop import TriRepoSyncLoop
from pipeline.wolf_reflective_loop import WolfReflectiveLoop

if __name__ == "__main__":
    sync = TriRepoSyncLoop()
    reflective = WolfReflectiveLoop()
    sync_result = sync.run()
    reflection = reflective.run()
    print("✅ Vault Sync and Reflection Done")
    print(sync_result, reflection)
