# ===============================================================
# 💰 SMART MONEY DETECTOR v5.4.1-HYBRID
# ===============================================================
# Author: TUYUL KARTEL LABS 🐺
# Date: 2025-11-27
# Purpose:
#   Deteksi aktivitas institusional berbasis VWAP deviation,
#   MFI–CCI spread, RSI ekstrem, dan Reflex–Fusion validation.
#   Terintegrasi penuh dengan Reflex Layer & Vault AutoSync.
# ===============================================================

import datetime
import math
from typing import Any, Dict

import pandas as pd


class SmartMoneyDetector:
    def __init__(self):
        self.version = "v5.4.1-HYBRID"
        self.last_signal = None

    def summarize_bias(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Ringkasan bias sederhana berbasis pergerakan harga.

        Jika DataFrame kosong atau kolom penting tidak ada, fallback ke bias WAIT.
        """

        if df is None or df.empty or "close" not in df.columns:
            return {"bias": "WAIT", "confidence": 0.5}

        delta = df["close"].iloc[-1] - df["close"].iloc[0]
        bias = "BUY" if delta >= 0 else "SELL"
        volatility = df["close"].diff().std() or 0.0
        confidence = max(0.5, min(0.95, 1 - (volatility * 0.01)))
        return {"bias": bias, "confidence": round(confidence, 3)}

    def detect_institutional_flow(self, pair, price, vwap, atr, rsi, mfi, cci50, rsi_h4, rc=0.85, conf12=0.82):
        """
        Deteksi aktivitas Smart Money (institusional) dan kembalikan hasil sinyal
        dengan konfirmasi penuh terhadap Reflex dan Fusion Layer.
        """
        vwap_deviation = abs(price - vwap)
        spread = abs(mfi - cci50)

        vwap_threshold = 1.05 * atr * (1 + (1 - rc))
        spread_threshold = 45 + (5 * (1 - conf12))

        is_rsi_extreme = (rsi >= 80 and price > vwap) or (rsi <= 20 and price < vwap)
        is_rsi_h4_supportive = (rsi_h4 >= 65 and price > vwap) or (rsi_h4 <= 35 and price < vwap)

        reflex_confirmed = rc >= 0.8 and conf12 >= 0.78

        if vwap_deviation >= vwap_threshold and spread >= spread_threshold and is_rsi_extreme and is_rsi_h4_supportive and reflex_confirmed:
            signal_type = "SELL" if price > vwap else "BUY"
            sl = price + vwap_deviation if signal_type == "SELL" else price - vwap_deviation
            tp = vwap
            confidence = round(min(1.0, conf12 + (rc - 0.8) * 0.2), 3)

            signal = {
                "pair": pair,
                "entry": round(price, 5),
                "sl": round(sl, 5),
                "tp": round(tp, 5),
                "type": signal_type,
                "rsi": rsi,
                "mfi": mfi,
                "cci_50": cci50,
                "spread": round(spread, 2),
                "deviation": round(vwap_deviation, 5),
                "confidence": confidence,
                "reflex_validation": True,
                "institutional_support": confidence - 0.75,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "note": f"Smart Money Detector {self.version} (Fusion–Reflex Enhanced)"
            }

            self.last_signal = signal
            return signal

        signal = {
            "status": "No institutional confirmation",
            "pair": pair,
            "rsi": rsi,
            "rsi_h4": rsi_h4,
            "spread": round(spread, 2),
            "deviation": round(vwap_deviation, 5),
            "reflex_validation": False,
            "institutional_support": 0.0,
            "timestamp": datetime.datetime.utcnow().isoformat(),
        }

        self.last_signal = signal
        return signal

    def update_reflex_state(self, reflex_state):
        """Perkuat Reflex Coherence Index jika ada institutional confirmation."""
        if self.last_signal and self.last_signal.get("institutional_support", 0) > 0:
            reflex_state["RCAdj"] = round(min(1.0, reflex_state["RCAdj"] + 0.05), 3)
            reflex_state["CogScore"] = round(min(1.0, reflex_state["CogScore"] + 0.03), 3)
            reflex_state["institutional_feedback"] = True
        else:
            reflex_state["institutional_feedback"] = False
        return reflex_state

    def get_last_signal(self):
        return self.last_signal or {"status": "no-signal"}


# ===============================================================
# 🧪 TEST SMART MONEY DETECTOR
# ===============================================================
if __name__ == "__main__":
    smd = SmartMoneyDetector()
    result = smd.detect_institutional_flow(
        pair="XAUUSD",
        price=1.1050,
        vwap=1.0980,
        atr=0.0045,
        rsi=83,
        mfi=78,
        cci50=10,
        rsi_h4=70,
        rc=0.87,
        conf12=0.83
    )
    reflex_state = {"RCAdj": 0.82, "CogScore": 0.84}
    print("SMD Output:", result)
    print("Updated Reflex State:", smd.update_reflex_state(reflex_state))
