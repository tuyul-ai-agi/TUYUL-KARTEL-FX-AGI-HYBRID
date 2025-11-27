"""Reflex Coherence API handler."""

from fastapi import APIRouter
from pydantic import BaseModel

from ...fushion.fushion_confidence_core import compute_reflex_coherence

router = APIRouter()


class ReflexResponse(BaseModel):
    Reflex_Coherence: float
    status: str


@router.post("/run", response_model=ReflexResponse)
def run_reflex() -> ReflexResponse:
    """Compute the reflex coherence metric and return a status summary."""

    rc: float = compute_reflex_coherence()
    status = "OK" if rc >= 0.75 else "LOW"
    return ReflexResponse(Reflex_Coherence=rc, status=status)
