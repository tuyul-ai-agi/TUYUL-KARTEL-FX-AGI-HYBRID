# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Reflective OpenAPI Validator
# ------------------------------------------------------------
# Validasi endpoint API reflektif untuk memastikan kompatibilitas
# dengan protokol RBP_v2.2 dan struktur JSON yang benar.
# ============================================================

from pathlib import Path
from typing import Any, Iterable

import yaml


SCHEMA_PATH = Path("docs/openapi_tuyul_agi_hybrid_v5.7.3r++.yml")
REQUIRED_REFLECTIVE_FIELDS = ["conf12", "wlwci", "rcadj", "integrity_index", "reflective_sync"]


def _gather_missing_fields(doc: Any, required: Iterable[str]) -> list[str]:
    found = set()

    def walk(node: Any):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in required:
                    found.add(k)
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(doc)
    return [f for f in required if f not in found]


def validate_reflective_schema(openapi_doc: dict) -> bool:
    """Validasi field-field reflektif penting di OpenAPI (RBP_v2.2)."""
    missing = _gather_missing_fields(openapi_doc, REQUIRED_REFLECTIVE_FIELDS)
    if missing:
        print(f"❌ Missing Reflective Fields: {missing}")
        return False
    print("✅ Reflective OpenAPI Schema Validation PASSED.")
    return True


def validate_openapi_file(path: Path = SCHEMA_PATH) -> bool:
    """Validasi file OpenAPI utama sistem reflektif."""
    if not path.exists():
        print(f"❌ File OpenAPI tidak ditemukan: {path}")
        return False

    with open(path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    if not isinstance(schema, dict):
        print("❌ Struktur OpenAPI tidak valid (bukan dict).")
        return False

    for field in ("info", "paths", "components"):
        if field not in schema:
            print(f"❌ Field '{field}' hilang dari OpenAPI schema")
            return False

    version = str(schema.get("info", {}).get("version", ""))
    if not version.startswith("5.7.8"):
        print(f"⚠️ Schema version mismatch: {version} (expected 5.7.8*)")

    reflective_ok = validate_reflective_schema(schema)
    if reflective_ok:
        print(f"✅ OpenAPI file valid dan kompatibel dengan RBP_v2.2 — {path}")
    return reflective_ok


if __name__ == "__main__":
    validate_openapi_file()
