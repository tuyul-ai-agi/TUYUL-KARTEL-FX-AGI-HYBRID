# ============================================================
# 🧠 Check Quad Repo Reflective Sync
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import getIntegrityFeedback


def check_quad_repo_sync():
    """Cek integritas sinkronisasi Quad Repo."""

    feedback = getIntegrityFeedback()
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
