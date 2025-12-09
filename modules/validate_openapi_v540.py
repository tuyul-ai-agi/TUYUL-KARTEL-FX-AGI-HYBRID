# ============================================================
# 🧩 Validate OpenAPI Schema — TUYUL FX AGI HYBRID v5.7.3r++
# ------------------------------------------------------------
# Memvalidasi endpoint AGI Hybrid agar sesuai dengan v5.7.3r++ API spec.
# ============================================================

import yaml
import json
from pathlib import Path


SCHEMA_PATH = Path("configs/openapi_v573r.yml")


def validate_schema(schema_path=SCHEMA_PATH):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    required_fields = ["info", "paths", "components"]

    for field in required_fields:
        if field not in schema:
            raise ValueError(f"[❌] Field '{field}' hilang dari OpenAPI schema")

    version = schema["info"].get("version", "")
    if not version.startswith("5.7.3"):
        raise ValueError(f"[⚠️] Schema version mismatch: {version} (expected 5.7.3r++)")

    print(f"[✅] Schema valid — OpenAPI {version}")
    return True


if __name__ == "__main__":
    validate_schema()
