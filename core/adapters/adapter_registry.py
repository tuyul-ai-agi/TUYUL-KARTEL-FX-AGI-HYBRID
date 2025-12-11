# Reflective Adapter Registry — v5.7.3r++
# Mendaftarkan semua adapter aktif dan memastikan sinkronisasi versi
import importlib, datetime

class AdapterRegistry:
    def __init__(self):
        self.adapters = {}
        self.timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    def register(self, name, adapter_class):
        self.adapters[name] = adapter_class
        print(f"✅ Registered Reflective Adapter: {name}")

    def list_adapters(self):
        return list(self.adapters.keys())

    def load_all(self):
        print("🧠 Loading all reflective adapters...")
        modules = ["chart_ocr_reflective_adapter", "tuyul_data_reflective_adapter"]
        for m in modules:
            importlib.import_module(f"core.adapters.{m}")
        print(f"🕒 Registry initialized at {self.timestamp}")
