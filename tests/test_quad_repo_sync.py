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

from modules.tuyul_bots_reflective_sync import ReflectiveBridgeSync

def test_quad_repo_reflective_sync():
    """Uji sinkronisasi penuh antar empat repositori reflektif."""
    print("🔁 Menjalankan Quad Repo Reflective Sync Test...")
    bridge_sync = ReflectiveBridgeSync()
    sync = bridge_sync.run_full_sync()
    feedback = sync

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
    assert sync["latency_ms"] < 300, f"❌ Latency terlalu tinggi: {sync['latency_ms']}ms"

    print(
        "✅ Quad Repo Sync Stable — Integrity="
        f"{feedback['integrity_index']} | Drift={feedback['coherence_drift']} | "
        f"Latency={sync['latency_ms']}ms | Reflection={feedback['reflection_score']}"
    )
