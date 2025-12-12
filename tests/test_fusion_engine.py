import pytest

from core.fusion.fusion_confidence_core import FusionConfidenceCore


def test_confidence_metrics_structure():
    core = FusionConfidenceCore()
    metrics = core.compute([0.92, 0.9, 0.08])

    assert 0 <= metrics["conf12"] <= 1
    assert "reflective_state" in metrics
    assert metrics["wlwci"] >= 0
    assert metrics["timestamp"].endswith("+00:00")
