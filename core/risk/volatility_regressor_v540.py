"""
Volatility Regressor v5.4.0
---------------------------
Regressor sederhana untuk estimasi volatilitas pasar.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


class VolatilityRegressor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, df: pd.DataFrame):
        df["range"] = df["high"] - df["low"]
        X = np.arange(len(df)).reshape(-1, 1)
        y = df["range"].values
        self.model.fit(X, y)

    def predict_next(self, steps=1):
        X_pred = np.array([[i] for i in range(100, 100 + steps)])
        preds = self.model.predict(X_pred)
        return round(float(preds[-1]), 4)
