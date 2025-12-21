"""Unit tests for the reflective data bridge helpers."""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "core" / "reflective" / "reflective_data_bridge.py"
SPEC = importlib.util.spec_from_file_location("reflective_data_bridge", MODULE_PATH)
_module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(_module)

VixSnapshot = _module.VixSnapshot
fetch_vix_snapshot = _module.fetch_vix_snapshot
normalize_snapshot = _module.normalize_snapshot


def test_fetch_vix_snapshot_defaults():
    snapshot = fetch_vix_snapshot()
    assert snapshot["source"] == "api_twelvedata_com__jit_plugin"
    assert snapshot["vix"] > 0
    assert snapshot["rvi"] > 0
    assert snapshot["term_structure"] == "Contango"
    assert "T" in snapshot["timestamp"]


def test_normalize_snapshot_coercion_and_defaults():
    raw_snapshot = {"vix": "21.1", "term_structure": "Backwardation"}

    normalized: VixSnapshot = normalize_snapshot(raw_snapshot)

    assert normalized["vix"] == 21.1
    assert normalized["rvi"] == 0.0
    assert normalized["term_structure"] == "Backwardation"
    assert normalized["source"] == "api_twelvedata_com__jit_plugin"
    assert normalized["timestamp"]
