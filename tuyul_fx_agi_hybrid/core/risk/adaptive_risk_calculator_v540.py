"""Adaptive risk calculation utilities."""

from typing import Dict


def calculate_risk(balance: float, sl_pips: float, risk_percent: float = 1.0) -> Dict[str, float]:
    """Calculate position sizing based on account balance and stop-loss distance."""

    risk_amount = balance * (risk_percent / 100)
    pip_value = 10
    lot_size = round(risk_amount / (sl_pips * pip_value), 2)
    return {
        "risk_percent": risk_percent,
        "risk_usd": round(risk_amount, 2),
        "lot_size": lot_size,
        "rr_ratio": 2.0,
    }
