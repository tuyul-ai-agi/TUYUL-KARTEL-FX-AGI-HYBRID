# ============================================================
# 🧠 Test: Fusion Engine Reflective v5.7.8
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    fusionAnalyze,
)


def test_fusion_engine_reflective():
    """Uji sinkronisasi lintas-layer Fusion–Reflective."""
    fusion = fusionAnalyze({"pair": "XAUUSD", "timeframe": "H4"})
    assert fusion["conf12"] >= 0.9, f"❌ CONF₁₂ terlalu rendah: {fusion['conf12']}"
    assert fusion["wlwci"] >= 0.9, f"❌ WLWCI tidak stabil: {fusion['wlwci']}"
    print(
        f"✅ Fusion Engine test OK — CONF₁₂={fusion['conf12']} | WLWCI={fusion['wlwci']}"
    )
