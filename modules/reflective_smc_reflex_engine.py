"""SMC Reflex layer integration utilities for TUYUL FX AGI."""

from __future__ import annotations

import datetime
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import yaml

DEFAULT_CONFIG_PATH = Path("configs/smc_reflex_config.yml")


@dataclass
class SMCReflexConfig:
    pivot_window: int = 5
    ema_fast_len: int = 9
    ema_slow_len: int = 21
    slope_weight: float = 0.2
    confidence_threshold: float = 65.0
    log_path: Path = Path("logs/smc_reflex_log.json")


def load_smc_reflex_config(config_path: Path | str = DEFAULT_CONFIG_PATH) -> SMCReflexConfig:
    """Load configuration for the SMC reflex engine."""

    path = Path(config_path)
    if not path.exists():
        return SMCReflexConfig()

    with open(path, "r", encoding="utf-8") as handle:
        raw_cfg = yaml.safe_load(handle) or {}

    smc_cfg = raw_cfg.get("smc_reflex", {})
    return SMCReflexConfig(
        pivot_window=int(smc_cfg.get("pivot_window", 5)),
        ema_fast_len=int(smc_cfg.get("ema_fast_len", 9)),
        ema_slow_len=int(smc_cfg.get("ema_slow_len", 21)),
        slope_weight=float(smc_cfg.get("slope_weight", 0.2)),
        confidence_threshold=float(smc_cfg.get("confidence_threshold", 65)),
        log_path=Path(smc_cfg.get("log_path", "logs/smc_reflex_log.json")),
    )


def detect_structure_shift(
    highs: np.ndarray, lows: np.ndarray, pivot_window: int
) -> Tuple[bool, bool, bool, bool]:
    """Detect CHoCH and BOS style structural shifts."""

    window = max(2, min(pivot_window, len(highs)))
    bullish_choch = bool(
        highs[-1] > float(np.mean(highs[-window:])) and lows[-1] > float(lows[-window])
    )
    bearish_choch = bool(
        lows[-1] < float(np.mean(lows[-window:])) and highs[-1] < float(highs[-window])
    )
    bullish_bos = bool(len(highs) >= 2 and highs[-1] > highs[-2])
    bearish_bos = bool(len(lows) >= 2 and lows[-1] < lows[-2])
    return bullish_choch, bearish_choch, bullish_bos, bearish_bos


def compute_trend_confidence(
    closes: np.ndarray, ema_fast: float, ema_slow: float, slope_weight: float = 0.2
) -> float:
    """Calculate a reflective confidence score based on EMA gap and slope."""

    last_close = float(closes[-1])
    ema_gap_pct = abs(ema_fast - ema_slow) / last_close * 100
    slope_component = float(np.gradient(closes)[-1]) * 100
    return float(np.clip(ema_gap_pct * 0.4 + slope_component * slope_weight, 0, 100))


def compute_reflective_bias_state(
    closes: np.ndarray,
    highs: np.ndarray,
    lows: np.ndarray,
    ema_fast: float,
    ema_slow: float,
    config: SMCReflexConfig | None = None,
) -> Dict[str, object]:
    """Generate a bias snapshot from simplified SMC signals."""

    cfg = config or SMCReflexConfig()
    bullish_choch, bearish_choch, bullish_bos, bearish_bos = detect_structure_shift(
        highs, lows, cfg.pivot_window
    )
    conf_score = compute_trend_confidence(closes, ema_fast, ema_slow, cfg.slope_weight)
    bias = (
        "Bullish"
        if bullish_choch or bullish_bos
        else "Bearish"
        if bearish_choch or bearish_bos
        else "Neutral"
    )

    reflective_output: Dict[str, object] = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "bias": bias,
        "bullish_choch": bullish_choch,
        "bearish_choch": bearish_choch,
        "bullish_bos": bullish_bos,
        "bearish_bos": bearish_bos,
        "trend_conf_score": round(conf_score, 2),
    }
    cfg.log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cfg.log_path, "a", encoding="utf-8") as handle:
        json.dump(reflective_output, handle, ensure_ascii=False)
        handle.write("\n")

    return reflective_output
