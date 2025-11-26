# ===============================================================
# 🧠 TUYUL FX ULTRA WOLF v5.4.1-HYBRID
# FINAL OUTPUT 12 ENGINE (FULL FUSION–REFLEX–RISK–MACRO–SMARTMONEY)
# ===============================================================
# Author: TUYUL KARTEL LABS 🐺
# Date: 2025-11-27
# Purpose:
#   Unified decision engine integrating:
#   - TWMS, FTA, RLSI, Reflex, Monte Carlo, ATR-Risk, VDDHybrid, SmartMoney
# ===============================================================

from datetime import datetime
from core.reflex.reflex_core_v540 import ReflexCore
from core.fusion.hybrid_fusion_orchestrator_v540 import HybridFusionOrchestrator
from modules.rlsi_module_v540 import ReflexLiquidityShiftIndex
from modules.vddhybrid_module_v540 import VDDHybridModule
from core.analytics.smart_money_detector import SmartMoneyDetector
from modules.adaptive_risk_engine_v540 import AdaptiveRiskEngine
from core.analytics.montecarlo_validator import MonteCarloValidator
from core.analytics.atr_risk_integrator import ATRRiskIntegrator
from core.bridge.vault_autosync_v541 import VaultAutoSync
from core.logging.journal_logger import JournalLogger


class FinalOutput12EngineV541:
    def __init__(self, config):
        self.config = config
        self.reflex = ReflexCore()
        self.rlsi = ReflexLiquidityShiftIndex()
        self.vdd = VDDHybridModule()
        self.fusion = HybridFusionOrchestrator()
        self.smd = SmartMoneyDetector()
        self.monte = MonteCarloValidator()
        self.atr_risk = ATRRiskIntegrator(config)
        self.adaptive_risk = AdaptiveRiskEngine()
        self.vault = VaultAutoSync()
        self.journal = JournalLogger()

    # ============================================================
    # 🔍 FUSION PIPELINE — MAIN EXECUTION
    # ============================================================
    def analyze(self, market_data, psych_state, risk_params):
        pair = market_data["pair"]
        direction = market_data["direction"]
        balance = risk_params["balance"]

        # 1️⃣ FUSION: TWMS + FTA + RLSI
        fusion_result = self.fusion.run_fusion(market_data, self.rlsi)

        # 2️⃣ REFLEX: Coherence & Emotion Delta
        reflex_state = self.reflex.compute_reflex(psych_state)

        # 3️⃣ VDDHYBRID: Regime Detection (Risk Scaling)
        regime_signal = self.vdd.detect_regime()

        # 4️⃣ SMART MONEY CONFIRMATION
        smd_data = self.smd.detect_institutional_flow(
            pair=pair,
            price=market_data.get("price", 0),
            vwap=market_data.get("vwap", 0),
            atr=market_data.get("atr", 0),
            rsi=market_data.get("rsi", 50),
            mfi=market_data.get("mfi", 50),
            cci50=market_data.get("cci50", 0),
            rsi_h4=market_data.get("rsi_h4", 50),
            rc=reflex_state.get("RCAdj", 0.85),
            conf12=fusion_result.get("fusion_confidence", 0.8),
        )

        # 5️⃣ MONTE CARLO: Probabilistic Validation
        monte_result = self.monte.run_validation(pair=pair, rr=3.0)

        # 6️⃣ ATR + RISK
        df = market_data["candles"]
        atr_risk = self.atr_risk.integrate(df, direction, balance, risk_params["risk_percent"], pair)

        # 7️⃣ ADAPTIVE RISK (Based on Regime)
        adaptive_risk = self.adaptive_risk.scale_risk(
            base_risk=risk_params["risk_percent"],
            regime_state=regime_signal["RegimeState"],
            confidence=fusion_result["fusion_confidence"]
        )

        # =========================================================
        # 🔬 FUSION SCORE CALCULATION
        # =========================================================
        integrity_index = (
            fusion_result["fusion_confidence"] *
            reflex_state["coherence"] *
            (1 - reflex_state["emotion_delta"]) *
            monte_result["win_probability"] *
            (1 - regime_signal["RegimeState"] * 0.3) *
            (1 + smd_data.get("institutional_support", 0))
        ) ** 0.2

        verdict = (
            "EXECUTE"
            if integrity_index >= 0.78 and smd_data.get("institutional_support", 0) > 0
            else "WAIT"
            if integrity_index >= 0.65
            else "NO_TRADE"
        )

        # 8️⃣ REFLEX FEEDBACK UPDATE (from Smart Money)
        reflex_state = self.smd.update_reflex_state(reflex_state)

        # =========================================================
        # 🧾 JOURNAL + VAULT SYNC
        # =========================================================
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "pair": pair,
            "direction": direction,
            "integrity_index": round(integrity_index, 3),
            "verdict": verdict,
            "fusion_confidence": round(fusion_result["fusion_confidence"], 3),
            "reflex": reflex_state,
            "rlsi": self.rlsi.get_last_signal(),
            "vdd_regime": regime_signal,
            "smd_data": smd_data,
            "atr_risk": atr_risk,
            "adaptive_risk": adaptive_risk,
            "monte_result": monte_result,
            "final_risk": adaptive_risk["adjusted_risk_percent"],
        }

        self.journal.log(entry)
        self.vault.save(entry)

        # =========================================================
        # 📦 FINAL OUTPUT STRUCTURE (FOR LAYER 12)
        # =========================================================
        return {
            "pair": pair,
            "direction": direction,
            "integrity_index": round(integrity_index, 3),
            "verdict": verdict,
            "fusion_confidence": round(fusion_result["fusion_confidence"], 2),
            "reflex_coherence": reflex_state["coherence"],
            "emotion_delta": reflex_state["emotion_delta"],
            "atr_stop_loss": atr_risk["stop_loss"],
            "atr_take_profit": atr_risk["take_profit"],
            "recommended_lot": atr_risk["recommended_lot"],
            "adaptive_risk_percent": adaptive_risk["adjusted_risk_percent"],
            "regime_state": regime_signal["RegimeState"],
            "institutional_bias": smd_data.get("institutional_support", 0),
            "monte_win_prob": monte_result["win_probability"],
            "final_decision": verdict,
        }


# ===============================================================
# 🧪 TEST EXECUTION
# ===============================================================
if __name__ == "__main__":
    import pandas as pd, numpy as np

    dummy_data = {
        "pair": "XAUUSD",
        "direction": "LONG",
        "price": 1.1050,
        "vwap": 1.0980,
        "atr": 0.0045,
        "rsi": 83,
        "rsi_h4": 70,
        "mfi": 78,
        "cci50": 10,
        "twms_score": 15,
        "fta_score": 82,
        "fta_bias": "BULLISH",
        "candles": pd.DataFrame({
            "open": np.random.rand(200) * 100,
            "high": np.random.rand(200) * 100 + 1,
            "low": np.random.rand(200) * 100 - 1,
            "close": np.random.rand(200) * 100
        }),
    }

    psych = {"emotion_delta": 0.1, "focus_index": 0.9, "confidence_level": 0.95}
    risk = {"balance": 100000, "risk_percent": 1.0}

    engine = FinalOutput12EngineV541(config={})
    result = engine.analyze(dummy_data, psych, risk)
    print(result)
