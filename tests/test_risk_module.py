# ============================================================
# 🧠 Test: Adaptive Risk Calculation
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import (
    riskCalculate,
)


def test_adaptive_risk_engine():
    """Uji kalkulasi risk & lot dinamis reflektif."""
    risk = riskCalculate({"balance": 100000, "sl_pips": 50, "pair": "EURUSD"})
    assert 0.3 <= risk["risk_pct"] <= 1.5, (
        "❌ Risk % diluar batas reflektif (0.3–1.5%)"
    )
    assert risk["rr_ratio"] >= 1.5, "❌ R:R Ratio terlalu kecil!"
    print(
        "✅ Risk Engine test OK — Risk="
        f"{risk['risk_pct']}% | Lot={risk['lot']} | R:R={risk['rr_ratio']}"
    )
