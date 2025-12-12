from core.reflective.reflective_cycle_core import ReflectiveCycleCore

def test_reflective_cycle_run():
    rc_core = ReflectiveCycleCore()
    result = rc_core.execute()
    assert "integrity_index" in result
    assert "reflective_state" in result
