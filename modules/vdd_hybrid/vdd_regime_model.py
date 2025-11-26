import numpy as np
import pandas as pd
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

class VDDRegimeModel:
    """
    Hybrid Markov Regime Model untuk TUYUL FX
    """
    def __init__(self):
        self.model = None

    def fit(self, data: pd.DataFrame):
        features = data[['VIX_Z1M', 'DXY_Z1M', 'VIX_DXY_CORR', 'VIX_TERM']]
        self.model = MarkovRegression(features['VIX_Z1M'], k_regimes=3, trend='c', switching_variance=True)
        self.result = self.model.fit(disp=False)
        return self.result

    def predict_state(self):
        data = self.result.smoothed_marginal_probabilities.idxmax(axis=1)
        return data.iloc[-1]  # 0=Tranquil, 1=Stressed, 2=Crisis
