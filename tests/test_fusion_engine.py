import pytest
from core.fushion.fusion_confidence_core import calculate_confidence

def test_confidence_range():
    conf = calculate_confidence(rlsi=0.85, rcadj=0.88)
    assert 0 <= conf <= 1, "Confidence harus di antara 0 dan 1"
