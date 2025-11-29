"""
Risk Scenario Simulator
-----------------------
Simulasi risiko (Monte Carlo style) untuk memproyeksikan skenario outcome.
"""

import random


class RiskScenarioSimulator:
    def __init__(self, iterations=1000):
        self.iterations = iterations

    def simulate(self, conf12, balance, volatility):
        outcomes = []
        for _ in range(self.iterations):
            random_factor = random.uniform(-volatility, volatility)
            conf_adj = conf12 + (random_factor / 100)
            balance_change = balance * (conf_adj - 0.5) * 0.02
            outcomes.append(balance + balance_change)
        avg_outcome = sum(outcomes) / len(outcomes)
        return {
            "SimulatedMeanBalance": round(avg_outcome, 2),
            "ExpectedGainLoss(%)": round(((avg_outcome - balance) / balance) * 100, 2),
            "Iterations": self.iterations,
        }
