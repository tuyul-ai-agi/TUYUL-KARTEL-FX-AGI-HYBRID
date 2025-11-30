from core.risk.adaptive_risk_calculator_v540 import AdaptiveRisk

def test_risk_calculation():
    risk = AdaptiveRisk(balance=100000)
    output = risk.calculate()
    assert output["risk_percent"] <= 1.0
