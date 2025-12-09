# Monte Carlo Engine v2.2 (Adaptive 20k / 90 days)
import numpy as np
import json
from datetime import datetime

ITERATIONS = 20000
DURATION_DAYS = 90

def simulate_price_paths(prices: list[float]):
    """Monte Carlo simulation for 90-day horizon."""
    returns = np.diff(np.log(prices))
    mean, std = np.mean(returns), np.std(returns)
    results = []

    for _ in range(ITERATIONS):
        simulated_returns = np.random.normal(mean, std, DURATION_DAYS)
        simulated_path = prices[-1] * np.exp(np.cumsum(simulated_returns))
        results.append(simulated_path[-1])

    conf = np.mean(np.array(results) > prices[-1])
    return {
        "iterations": ITERATIONS,
        "duration_days": DURATION_DAYS,
        "confidence": round(float(conf), 4),
        "spec": f"{ITERATIONS//1000}k/{DURATION_DAYS}d",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "v2.2"
    }

if __name__ == "__main__":
    dummy = [1.10, 1.11, 1.12, 1.13]
    print(json.dumps(simulate_price_paths(dummy), indent=2))
