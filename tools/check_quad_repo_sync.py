# ============================================================
# 🧠 Check Quad Repo Reflective Sync
# ============================================================

from modules.tuyul_bots_reflective_sync import ReflectiveBridgeSync


def check_quad_repo_sync():
    """Cek integritas sinkronisasi Quad Repo."""

    feedback = ReflectiveBridgeSync().run_full_sync()
    print(
        f"🧠 Integrity={feedback['integrity_index']} | "
        f"Drift={feedback['coherence_drift']} | Regime={feedback['regime_adaptation']}"
    )
    if feedback["integrity_index"] < 0.9:
        print("⚠️ Integrity di bawah 0.9 — perlu re-sync manual.")
    else:
        print("✅ Quad Repo sinkron dan stabil.")


if __name__ == "__main__":
    check_quad_repo_sync()
