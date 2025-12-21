#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REFLECTIVE VWAP–MACD RESONANCE ADAPTER
────────────────────────────────────────
Bridges VWAP equilibrium and MACD momentum into
a consistent reflective resonance signal for Layer–12 FusionConf₁₂.
"""

import datetime
import json
from pathlib import Path
from modules.reflective_vwap_engine import get_vwap_equilibrium
from modules.reflective_macd_equilibrium import get_macd_equilibrium


class ReflectiveVWAPMACDResonance:
    """Combine VWAP and MACD equilibria into a resonance snapshot."""

    LOG_PATH = Path("logs/reflective_vwap_macd_resonance.json")

    @staticmethod
    def compute(pair: str, timeframe: str = "1h") -> dict:
        """Compute reflective resonance between VWAP and MACD signals."""

        vwap_eq = get_vwap_equilibrium(pair, timeframe)
        macd_eq = get_macd_equilibrium(pair, timeframe)

        curvature_diff = abs(vwap_eq["vwap_equilibrium_bias"] - macd_eq["macd_equilibrium"])
        reflective_bias = (
            "Bullish" if vwap_eq["vwap_equilibrium_bias"] > macd_eq["macd_equilibrium"] else "Bearish"
        )
        reflective_intensity = round(
            (vwap_eq["vwap_resonance"] + macd_eq["reflective_gradient"]) / 2, 6
        )

        result = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "pair": pair,
            "timeframe": timeframe,
            "fusion_curvature": round(curvature_diff, 6),
            "reflective_bias": reflective_bias,
            "reflective_intensity": reflective_intensity,
            "source": "reflective_vwap_macd_resonance",
        }

        ReflectiveVWAPMACDResonance.LOG_PATH.parent.mkdir(exist_ok=True)
        with open(ReflectiveVWAPMACDResonance.LOG_PATH, "a", encoding="utf-8") as file_handle:
            file_handle.write(json.dumps(result) + "\n")

        return result
