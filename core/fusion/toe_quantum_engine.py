"""
Quantum Reflective Engine utilities for mapping inter-pair coherence.
"""

from datetime import datetime
from typing import Dict, Iterable, Union

import numpy as np

Number = Union[float, int]
SeriesInput = Union[Number, Iterable[Number]]
StrengthMap = Dict[str, Dict[str, float]]
QuantumMap = Dict[str, Union[float, str, StrengthMap]]


def _coerce_series(value: SeriesInput) -> np.ndarray:
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
        array = np.asarray(list(value), dtype=float)
    else:
        array = np.asarray(value, dtype=float)

    array = np.atleast_1d(array).ravel()
    if array.size == 0:
        array = np.array([0.0])
    return array


def _normalize_series(pairs_data: Dict[str, SeriesInput]) -> np.ndarray:
    series_list = [_coerce_series(value) for value in pairs_data.values()]

    min_len = min(series.size for series in series_list)
    if min_len < 2:
        return np.eye(len(series_list))

    aligned = np.stack([series[:min_len] for series in series_list])
    matrix = np.corrcoef(aligned)
    if np.isscalar(matrix):
        matrix = np.ones((len(series_list), len(series_list)))
    return np.nan_to_num(matrix, nan=0.0)


def quantum_entanglement_map(pairs_data: Dict[str, SeriesInput]) -> QuantumMap:
    """
    Build a reflective resonance map across instrument pairs.

    Args:
        pairs_data: Mapping of pair symbol to mean energy (scalar or iterable).

    Returns:
        Mapping with timestamp, pairwise strength map, Reflective Coherence Index (RCI),
        and regime alignment classification.
    """
    if not pairs_data or len(pairs_data) < 2:
        return {
            "timestamp": f"{datetime.utcnow().isoformat()}Z",
            "strength_map": {},
            "rci": 0.0,
            "regime_alignment": "Undefined",
        }

    pairs = list(pairs_data.keys())
    corr_matrix = _normalize_series(pairs_data)

    strength_map = {
        pairs[i]: {pairs[j]: round(float(corr_matrix[i][j]), 3) for j in range(len(pairs))}
        for i in range(len(pairs))
    }

    upper_indices = np.triu_indices(len(pairs), k=1)
    upper_values = np.abs(corr_matrix[upper_indices])
    rci_value = float(np.mean(upper_values)) if upper_values.size else 0.0
    rci = round(rci_value, 3)

    if rci > 0.8:
        regime_alignment = "Synchronous"
    elif rci < 0.5:
        regime_alignment = "Divergent"
    else:
        regime_alignment = "Partial Sync"

    return {
        "timestamp": f"{datetime.utcnow().isoformat()}Z",
        "strength_map": strength_map,
        "rci": rci,
        "regime_alignment": regime_alignment,
    }
