"""Reflective Layer – TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0."""

from core.reflective.meta_reflector_dispatch import run_meta_reflection
from core.reflective.reflective_cycle_core_v540 import ReflectiveCycleCore, ReflectiveCycleCoreV540
from core.reflective.reflective_reasoner_v540 import ReflectiveReasoner
from core.reflective.relearning_cycle import RelearningCycle
from core.reflective.reflection_trainer import ReflectionTrainer

__all__ = [
    "run_meta_reflection",
    "ReflectiveCycleCore",
    "ReflectiveCycleCoreV540",
    "ReflectiveReasoner",
    "RelearningCycle",
    "ReflectionTrainer",
]
__version__ = "5.4.0"
