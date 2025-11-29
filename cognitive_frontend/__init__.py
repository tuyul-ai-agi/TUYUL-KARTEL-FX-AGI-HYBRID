"""
cognitive_frontend package
--------------------------
Lapisan antarmuka manusia ↔ AGI Hybrid.
Menyediakan Reflex Console (CLI) dan Web Dashboard untuk memantau reasoning, sync vault, dan refleksi AGI.

Version: v5.4.4
"""

__version__ = "5.4.4"
__author__ = "Tuyul Kartel FX Hybrid Team"

from .context_interpreter import ContextInterpreter
from .reflex_console import ReflexConsole

__all__ = ["ContextInterpreter", "ReflexConsole"]
