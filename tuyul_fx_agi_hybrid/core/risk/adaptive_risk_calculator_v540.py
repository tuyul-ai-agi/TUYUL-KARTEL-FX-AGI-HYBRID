"""Adaptive risk calculator for TUYUL FX Hybrid."""

from __future__ import annotations

from dataclasses import dataclass

_REFLEX_SAFE_RISK = 0.5
_REFLEX_CONFIRMED_RISK = 1.0
_REFLEX_DEFAULT_RISK = 0.7

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


def select_reflexive_risk(wlwci: float, rlsi: float, conf12: float, rc_adj: float) -> float:
    """Select the reflexive risk level (percentage) based on system coherence metrics."""

    if wlwci < 0.0 or rlsi < 0.0 or conf12 < 0.0 or rc_adj < 0.0:
        raise ValueError("Coherence metrics must be non-negative")

    if wlwci < 0.90 or rlsi < 0.65:
        return _REFLEX_SAFE_RISK
    if conf12 >= 0.80 and rc_adj >= 0.85:
        return _REFLEX_CONFIRMED_RISK
    return _REFLEX_DEFAULT_RISK


def calculate_lot_size(
    balance: float,
    risk_percent: float,
    sl_pips: float,
    pip_value: float = _PIP_VALUE,
) -> float:
    """Calculate lot size using a provided risk percentage and stop-loss distance."""

    if balance <= 0:
        raise ValueError("Balance must be positive")
    if risk_percent <= 0:
        raise ValueError("Risk percent must be positive")
    if sl_pips <= 0:
        raise ValueError("Stop-loss pips must be positive")
    if pip_value <= 0:
        raise ValueError("Pip value must be positive")

    risk_amount = balance * (risk_percent / 100)
    lot_size = risk_amount / (sl_pips * pip_value)
    return round(lot_size, 2)


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
