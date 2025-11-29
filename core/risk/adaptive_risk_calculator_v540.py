"""
Adaptive Risk Calculator v5.4.0
-------------------------------
Menghitung risiko adaptif AGI berdasarkan kepercayaan reasoning & volatilitas.
"""

class AdaptiveRiskCalculator:
    def __init__(self, base_risk=1.0):
        self.base_risk = base_risk

    def calculate(self, conf12: float, rcadj: float, volatility: float, balance: float):
        avg_conf = (conf12 + rcadj) / 2
        adj_factor = max(0.3, 1 - (avg_conf * 0.8)) * (1 + volatility / 100)
        risk_pct = round(self.base_risk * adj_factor, 2)
        lot = round((balance * (risk_pct / 100)) / 1000, 2)

        return {
            "RiskPercent": f"{risk_pct}%",
            "LotSize": lot,
            "ConfidenceAvg": round(avg_conf, 3),
            "Volatility": volatility
        }
