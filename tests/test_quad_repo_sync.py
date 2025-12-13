# ============================================================
# 🧠 Test: Quad Repo Reflective Sync v5.7.8
# ------------------------------------------------------------
# Menguji integritas sinkronisasi antar empat repositori reflektif:
# Hybrid ↔ Knowledge ↔ Kartel ↔ Journal
#
# Tujuan:
# - Integrity ≥ 0.90
# - Drift = Stable
# - Latency < 200ms
# - Reflection Score ≥ 0.9
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    getIntegrityFeedback,
    vaultSync,
)

def test_quad_repo_reflective_sync():
    """Uji sinkronisasi penuh antar empat repositori reflektif."""
    print("🔁 Menjalankan Quad Repo Reflective Sync Test...")
    sync = vaultSync()
    feedback = getIntegrityFeedback()

    # Validasi integritas lintas-repo
    assert feedback["integrity_index"] >= 0.9, (
        f"❌ Integrity rendah: {feedback['integrity_index']}"
    )
    assert feedback["coherence_drift"] == "Stable", (
        f"❌ Drift terdeteksi: {feedback['coherence_drift']}"
    )
    assert feedback["reflection_score"] >= 0.9, (
        f"❌ Reflection score rendah: {feedback['reflection_score']}"
    )
    assert sync["latency_ms"] < 200, f"❌ Latency terlalu tinggi: {sync['latency_ms']}ms"

    print(
        "✅ Quad Repo Sync Stable — Integrity="
        f"{feedback['integrity_index']} | Drift={feedback['coherence_drift']} | "
        f"Latency={sync['latency_ms']}ms | Reflection={feedback['reflection_score']}"
    )
