# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Run Repo Sync (Reflective)
# ============================================================

from pipeline.quad_repo_sync_handler import run_quad_repo_sync


def run_repo_sync():
    print("🔁 Running Quad Repo Reflective Sync (Manual)...")
    run_quad_repo_sync()


if __name__ == "__main__":
    run_repo_sync()
from pipeline.quad_repo_sync_loop import QuadRepoSyncLoop

if __name__ == "__main__":
    sync = QuadRepoSyncLoop()
    result = sync.run()
    print("[SYNC RESULT]")
    print(result)
