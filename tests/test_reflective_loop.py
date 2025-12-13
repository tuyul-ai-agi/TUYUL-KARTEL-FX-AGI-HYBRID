# ============================================================
# 🧠 Test: Reflective Loop Stability
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    runReflectiveCycle,
)


def test_reflective_loop_stability():
    """Uji kestabilan siklus reflektif penuh."""
    result = runReflectiveCycle()
    assert result["integrity_index"] >= 0.9, (
        f"❌ Integrity rendah: {result['integrity_index']}"
    )
    assert result["reflective_coherence"] >= 0.9, (
        f"❌ Koherensi reflektif lemah: {result['reflective_coherence']}"
    )
    print(
        "✅ Reflective Loop Stable — Integrity="
        f"{result['integrity_index']} | Coherence={result['reflective_coherence']}"
    )
