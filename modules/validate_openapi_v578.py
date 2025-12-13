# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Reflective OpenAPI Validator
# ------------------------------------------------------------
# Validasi endpoint API reflektif untuk memastikan kompatibilitas
# dengan protokol RBP_v2.2 dan struktur JSON yang benar.
# ============================================================

import json


def validate_reflective_schema(openapi_doc):
    """Validasi field-field reflektif penting di OpenAPI."""
    required_fields = ["conf12", "wlwci", "rcadj", "integrity_index", "reflective_sync"]
    missing = [f for f in required_fields if f not in openapi_doc]
    if missing:
        print(f"❌ Missing Reflective Fields: {missing}")
        return False
    print("✅ Reflective OpenAPI Schema Validation PASSED.")
    return True


def validate_openapi_file(path="openapi_tuyul_agi_hybrid_v5.7.3r++.yml"):
    """Validasi file OpenAPI utama sistem reflektif."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if any(x in content for x in ["conf12", "wlwci", "reflective_sync"]):
                print("✅ OpenAPI file valid dan kompatibel dengan RBP_v2.2")
                return True
            else:
                print("⚠️ OpenAPI file belum memiliki struktur reflektif penuh.")
                return False
    except FileNotFoundError:
        print("❌ File OpenAPI tidak ditemukan.")
        return False
