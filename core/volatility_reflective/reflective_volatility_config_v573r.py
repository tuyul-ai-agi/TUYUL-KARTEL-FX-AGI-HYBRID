"""Configuration for the reflective volatility layer."""

from __future__ import annotations

from typing import Dict, Tuple


class ReflectiveVolatilityConfig:
    """Configuration model for the VDD reflective layer (v5.7.3r++)."""

    def __init__(self) -> None:
        self.version: str = "v5.7.3r++"
        self.volatility_bands: Dict[str, Tuple[float, float]] = {
            "low": (0.00, 0.18),
            "moderate": (0.18, 0.35),
            "high": (0.35, 0.60),
            "extreme": (0.60, 1.00),
        }
        self.deviation_thresholds: Dict[str, float] = {
            "neutral": 0.05,
            "stressed": 0.12,
            "crisis": 0.20,
        }
        self.reflective_coherence_target: float = 0.92

    def interpret_volatility(self, value: float) -> str:
        """Classify the current volatility value into a configured band."""
        for band, (lower, upper) in self.volatility_bands.items():
            if lower <= value < upper:
                return band
        return "undefined"
