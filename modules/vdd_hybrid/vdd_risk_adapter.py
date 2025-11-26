class VDDRiskAdapter:
    """
    Adaptive Risk Multiplier berdasarkan RegimeState
    """
    def __init__(self):
        self.map = {
            0: {"name": "Tranquil", "multiplier": 1.0},
            1: {"name": "Stressed", "multiplier": 0.5},
            2: {"name": "Crisis", "multiplier": 0.1}
        }

    def get_risk_multiplier(self, state):
        return self.map[state]
