"""
VDDHybrid Module v5.4.0
-----------------------
Vault Decision Driver — mendeteksi rezim pasar dan mengatur mode reasoning AGI.
"""

import pandas as pd
from core.risk.volatility_regressor_v540 import VolatilityRegressor
from core.analytics.coherence_monitor import CoherenceMonitor
from core.risk.regime_state_detector import RegimeStateDetector

class VDDHybridModule:
    def __init__(self):
        self.vol_regressor = VolatilityRegressor()
        self.coherence = CoherenceMonitor()
        self.regime = RegimeStateDetector()

    def detect_regime(self, df: pd.DataFrame, reflex_conf: float, fusion_conf: float, wlwci: float):
        self.vol_regressor.train(df)
        vol = self.vol_regressor.predict_next()
        coherence = self.coherence.evaluate(reflex_conf, fusion_conf, wlwci)
        regime_state = self.regime.detect(vol, coherence["coherence_index"])

        return {
            "PredictedVolatility": vol,
            "CoherenceIndex": coherence["coherence_index"],
            "RegimeState": regime_state
        }
