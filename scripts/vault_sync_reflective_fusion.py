# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Vault→Repo Reflective Fusion Sync
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    fusionSaveJournal,
)


def sync_fusion_to_repo():
    print("🧩 Saving Reflective Fusion Output to Journal Repo...")
    result = fusionSaveJournal()
    print(
        f"✅ Fusion→Repo Sync Complete | Status={result['status']} | Time={result['timestamp']}"
    )
    return result


if __name__ == "__main__":
    sync_fusion_to_repo()
from pipeline.quad_repo_sync_loop import QuadRepoSyncLoop
from pipeline.wolf_reflective_loop import WolfReflectiveLoop

if __name__ == "__main__":
    sync = QuadRepoSyncLoop()
    reflective = WolfReflectiveLoop()
    sync_result = sync.run()
    reflection = reflective.run()
    print("✅ Vault Sync and Reflection Done")
    print(sync_result, reflection)
