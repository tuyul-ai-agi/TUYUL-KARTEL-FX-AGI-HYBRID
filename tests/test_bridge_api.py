# ============================================================
# 🧠 Test: Reflective Bridge API
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    gptBridge,
)


def test_reflective_bridge():
    """Uji komunikasi GPT Bridge antar layer reflektif."""
    result = gptBridge(
        {"prompt": "analyze EURUSD fusion bias", "layer": "Fusion", "model": "GPT-5"}
    )
    assert "conf12" in result or "wlwci" in result, (
        "❌ Bridge tidak mengembalikan data reflektif!"
    )
    print("✅ GPT Bridge test OK — Response:", result)
