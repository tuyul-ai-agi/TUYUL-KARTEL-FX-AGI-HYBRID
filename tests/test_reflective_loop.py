from core.reflective.reflective_cycle_core import ReflectiveCycleCore

def test_reflective_cycle_run():
    rc = ReflectiveCycleCore()
    result = rc.execute()

    assert "integrity_index" in result
    assert "reflective_state" in result
    assert result.get("reflective_sync") == "complete"
