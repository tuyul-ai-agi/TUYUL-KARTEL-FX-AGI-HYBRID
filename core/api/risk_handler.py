"""
Risk Handler
------------
Endpoint untuk kalkulasi risiko adaptif AGI berdasarkan parameter reflektif.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/calculate")
def calculate_risk(balance: float = 10000, conf12: float = 0.9, rcadj: float = 0.88):
    risk_pct = round((1 - ((conf12 + rcadj) / 2)) * 5, 2)
    lot_size = round((balance * (risk_pct / 100)) / 1000, 2)
    return {
        "balance": balance,
        "conf12": conf12,
        "rcadj": rcadj,
        "risk_percent": f"{risk_pct}%",
        "recommended_lot": lot_size
    }
