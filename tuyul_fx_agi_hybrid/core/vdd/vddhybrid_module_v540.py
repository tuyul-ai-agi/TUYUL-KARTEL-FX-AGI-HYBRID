"""
🐺 TUYUL FX ULTRA WOLF v5.4.0 — VDDHybrid Module
Service-ready Regime Detector: VIX–DXY–Volatility
Integrates probabilistic Markov-Switching logic for global volatility regime detection.
"""

import asyncio
import json
import datetime
import numpy as np
import redis
from fastapi import FastAPI
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression
from core.modules.bridge_module_v540 import (
    pushReasoningToJournal,
    pushHeuristicUpdate,
)

app = FastAPI(title="VDDHybrid Service v5.4.0")

class VDDHybridDetector:
    def __init__(self):
        self.redis_client = redis.Redis(host="localhost", port=6379, db=0)
        self.scaler = StandardScaler()
        self.model = None
        self.last_state = None
        self.features = []
        self.regime_states = ["TRANQUIL", "STRESSED", "CRISIS"]

    async def fit_model(self, data):
        """Train or update Markov Switching model with 3 regimes."""
        vix = data["VIX"]
        dxy = data["DXY"]
        vix_z = (vix - np.mean(vix)) / np.std(vix)
        dxy_z = (dxy - np.mean(dxy)) / np.std(dxy)
        corr = np.corrcoef(vix, dxy)[0, 1]

        self.features = np.column_stack([vix_z, dxy_z])
        y = np.mean(self.features, axis=1)
        self.model = MarkovRegression(y, k_regimes=3, trend='c', switching_variance=True)
        self.model_fit = self.model.fit(disp=False)
        return self.model_fit

    async def detect_regime(self, data):
        if not self.model:
            await self.fit_model(data)
        smoothed_probs = self.model_fit.smoothed_marginal_probabilities
        last_probs = smoothed_probs.iloc[-1].to_dict()
        state = int(max(last_probs, key=last_probs.get))
        timestamp = datetime.datetime.utcnow().isoformat()

        signal = {
            "RegimeState": state,
            "RegimeName": self.regime_states[state],
            "Probabilities": last_probs,
            "Timestamp": timestamp,
        }
        self.last_state = signal

        # Publish to Redis for Fusion Orchestrator
        self.redis_client.publish("vdd_regime_signal", json.dumps(signal))

        # Sync with Vaults
        await pushReasoningToJournal(signal)
        await pushHeuristicUpdate()

        return signal


detector = VDDHybridDetector()

@app.get("/vdd/regime")
async def get_regime_status():
    """Return current regime classification."""
    if detector.last_state:
        return detector.last_state
    return {"message": "Model not yet initialized"}

@app.post("/vdd/update")
async def update_regime(data: dict):
    """Update regime model and broadcast result."""
    signal = await detector.detect_regime(data)
    return signal

@app.get("/vdd/signal")
async def get_last_signal():
    """Get last published regime signal."""
    return detector.last_state or {"status": "no data"}

