# Smart Money Reflective Analyzer — TUYUL v5.7.3r++
import numpy as np, pandas as pd, datetime

class SmartMoneyReflectiveAnalyzer:
    """Deteksi absorpsi/distribusi institusional dengan konteks reflektif"""

    def analyze(self, volume_series, price_series):
        df = pd.DataFrame({"volume": volume_series, "price": price_series})
        df["delta"] = df["price"].diff()
        df["smc_score"] = (df["volume"] * np.sign(df["delta"])) / (df["volume"].abs().sum() + 1e-9)

        absorption = df[df["smc_score"] > 0].sum()["smc_score"]
        distribution = df[df["smc_score"] < 0].sum()["smc_score"]
        bias_score = round(abs(absorption / (absorption + abs(distribution) + 1e-9)), 3)
        reflective_state = "accumulation" if absorption > abs(distribution) else "distribution"

        reflection = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "absorption": float(absorption),
            "distribution": float(distribution),
            "bias_score": bias_score,
            "reflective_state": reflective_state
        }
        print(f"💰 Smart Money Reflective — {reflective_state.upper()} ({bias_score})")
        return reflection
