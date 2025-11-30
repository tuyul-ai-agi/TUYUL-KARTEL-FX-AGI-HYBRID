from core.reflective.reflective_cycle_core_v540 import ReflectiveCycle

def test_reflective_cycle_run():
    rc = ReflectiveCycle()
    result = rc.run_cycle()
    assert "reflection_score" in result
