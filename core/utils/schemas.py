"""
schemas.py
-----------
Definisi Pydantic schema untuk Reflective Dataset Validator API.
Versi: TUYUL FX AGI HYBRID v5.7.3r++
Protocol: RBP v2.2
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class DatasetValidationRequest(BaseModel):
    pairs: List[str] = Field(
        default=["btcusd", "eurusd", "xauusd"],
        description="List pasangan simbol untuk divalidasi",
    )
    validation_mode: str = Field(default="full", description="Mode validasi (full atau quick)")
    threshold: float = Field(default=0.9, description="Ambang batas Reflective Score minimum")

    @field_validator("pairs")
    @classmethod
    def validate_pairs(cls, value: List[str]) -> List[str]:
        cleaned = [pair.strip().lower() for pair in value if pair.strip()]
        if not cleaned:
            raise ValueError("pairs tidak boleh kosong")
        return cleaned

    @field_validator("validation_mode")
    @classmethod
    def validate_mode(cls, value: str) -> str:
        allowed = {"full", "quick"}
        if value not in allowed:
            raise ValueError(f"validation_mode harus salah satu dari {allowed}")
        return value

    @field_validator("threshold")
    @classmethod
    def validate_threshold(cls, value: float) -> float:
        if not 0.0 <= value <= 1.0:
            raise ValueError("threshold harus di antara 0.0 dan 1.0")
        return value


class DatasetResult(BaseModel):
    pair: str
    records: int
    reflective_score: float
    coherence_level: str
    integrity_index: float
    fusion_confidence: float
    vix_state: str
    regime_state: str

    @field_validator("pair", "coherence_level", "vix_state", "regime_state")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("field string tidak boleh kosong")
        return value.strip().lower()

    @field_validator("records")
    @classmethod
    def validate_records(cls, value: int) -> int:
        if value < 0:
            raise ValueError("records tidak boleh negatif")
        return value

    @field_validator(
        "reflective_score",
        "integrity_index",
        "fusion_confidence",
    )
    @classmethod
    def validate_scores(cls, value: float) -> float:
        if not 0.0 <= value <= 1.0:
            raise ValueError("score harus di antara 0.0 dan 1.0")
        return value


class DatasetValidationResponse(BaseModel):
    status: str = Field(default="completed", description="Status proses validasi")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Waktu eksekusi (UTC)"
    )
    results: List[DatasetResult]
    meta: dict[str, str | int | float | bool | None]

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("status tidak boleh kosong")
        return value.strip().lower()


class ReflectiveLogEvent(BaseModel):
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Waktu log (UTC)"
    )
    pair: str
    reflective_score: float
    integrity_index: float
    latency_ms: Optional[int]
    status: str
    vix_state: Optional[str]
    system_version: str = Field(default="v5.7.3r++", const=True)
    reflective_protocol: str = Field(default="RBP v2.2", const=True)

    @field_validator("pair", "status")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("field string tidak boleh kosong")
        return value.strip().lower()

    @field_validator("latency_ms")
    @classmethod
    def validate_latency(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 0:
            raise ValueError("latency_ms tidak boleh negatif")
        return value

    @field_validator("reflective_score", "integrity_index")
    @classmethod
    def validate_log_scores(cls, value: float) -> float:
        if not 0.0 <= value <= 1.0:
            raise ValueError("score harus di antara 0.0 dan 1.0")
        return value

    @field_validator("vix_state")
    @classmethod
    def validate_vix(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        cleaned = value.strip().lower()
        if not cleaned:
            raise ValueError("vix_state tidak boleh kosong jika diisi")
        return cleaned


__all__ = [
    "DatasetValidationRequest",
    "DatasetValidationResponse",
    "DatasetResult",
    "ReflectiveLogEvent",
]
