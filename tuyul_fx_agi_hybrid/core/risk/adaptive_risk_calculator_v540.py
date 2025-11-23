from .volatility_regressor_v540 import estimate_volatility


def calculate_risk(equity: float, stop_loss_pips: float, risk_percent: float = 1.0):
    volatility_factor = estimate_volatility("XAUUSD", "H1")
    risk_amount = round(equity * (risk_percent / 100), 2)
    pip_value = 10  # placeholder per standard lot
    position_size = round((risk_amount / (stop_loss_pips * pip_value)) * volatility_factor, 3)
    return {
        "risk_amount": risk_amount,
        "position_size": position_size,
        "volatility_factor": volatility_factor,
    }
"""Adaptive risk calculator for TUYUL FX Hybrid."""

from __future__ import annotations

from dataclasses import dataclass

_MIN_RISK = 0.007
_MAX_RISK = 0.01
_PIP_VALUE = 10.0


@dataclass
class RiskResult:
    risk_percent: float
    lot_size: float
    rr_ratio: float


def _clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def calculate_risk(balance: float, sl_pips: float) -> RiskResult:
    """Calculate position sizing using an adaptive 0.7–1% risk window."""

    if balance <= 0:
        raise ValueError("Balance must be positive")
    if sl_pips <= 0:
        raise ValueError("Stop-loss pips must be positive")

    risk_scale = _clamp((_MIN_RISK + (sl_pips / 250.0) * 0.0015), _MIN_RISK, _MAX_RISK)
    lot_size = (balance * risk_scale) / (sl_pips * _PIP_VALUE)
    rr_ratio = round(2.0 + (sl_pips / 100.0), 2)

    return RiskResult(
        risk_percent=round(risk_scale * 100, 3),
        lot_size=round(lot_size, 3),
        rr_ratio=rr_ratio,
    )
