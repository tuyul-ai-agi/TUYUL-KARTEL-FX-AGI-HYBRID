"""Adaptive risk calculation API handler."""

from fastapi import APIRouter
from pydantic import BaseModel

from ...risk.adaptive_risk_calculator_v540 import RiskResult, calculate_risk

router = APIRouter()


class RiskRequest(BaseModel):
    balance: float
    sl_pips: float


@router.post("/calculate", response_model=RiskResult)
def risk_calc(req: RiskRequest) -> RiskResult:
    """Calculate adaptive risk metrics based on account balance and stop-loss size."""

    return calculate_risk(req.balance, req.sl_pips)
