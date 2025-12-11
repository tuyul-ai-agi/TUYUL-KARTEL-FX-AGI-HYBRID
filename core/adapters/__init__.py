# TUYUL FX AGI HYBRID v5.7.3r++
# Reflective Adapter Package Loader — RBP v2.2
from .chart_ocr_reflective_adapter import ChartOCRReflectiveAdapter
from .tuyul_data_reflective_adapter import TuyulDataReflectiveAdapter
from .adapter_registry import AdapterRegistry

__version__ = "v5.7.3r++"
__protocol__ = "RBP v2.2"
__all__ = [
    "ChartOCRReflectiveAdapter",
    "TuyulDataReflectiveAdapter",
    "AdapterRegistry"
]

print("🧩 Reflective Adapters Initialized — TUYUL v5.7.3r++ RBP v2.2 Active")
