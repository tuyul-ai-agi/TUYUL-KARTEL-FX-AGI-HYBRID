"""
Pydantic schemas for reflective dataset validation (TUYUL FX AGI v5.7.3r++).
"""

from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, Field


class DatasetValidationRequest(BaseModel):
    pairs: List[str] = Field(default_factory=lambda: ["btcusd", "eurusd", "xauusd"])
    validation_mode: str = Field(default="full")
    threshold: float = Field(default=0.9, ge=0.0, le=1.0)


class DatasetResult(BaseModel):
    pair: str
    records: int
    reflective_score: float
    coherence_level: str
    integrity_index: float
    fusion_confidence: float
    vix_state: str
    regime_state: str


class DatasetValidationResponse(BaseModel):
    status: str
    timestamp: str
    results: List[DatasetResult]
    meta: Dict[str, str]


__all__ = [
    "DatasetValidationRequest",
    "DatasetValidationResponse",
    "DatasetResult",
]
