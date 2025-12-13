# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Generate OpenAPI Reflective Docs
# ============================================================

import datetime
import os

import yaml

OPENAPI_FILE = "docs/openapi_tuyul_agi_hybrid_v5.7.8.yml"


def generate_openapi():
    schema = {
        "info": {
            "title": "TUYUL FX AGI Reflective API",
            "version": "5.7.8",
            "description": "Reflective Quad Repo API documentation (RBP_v2.2).",
        },
        "reflective_schema": [
            "conf12",
            "wlwci",
            "rcadj",
            "integrity_index",
            "reflective_sync",
        ],
        "generated": datetime.datetime.utcnow().isoformat() + "Z",
    }
    os.makedirs("docs", exist_ok=True)
    with open(OPENAPI_FILE, "w", encoding="utf-8") as f:
        yaml.dump(schema, f)
    print(f"✅ Reflective OpenAPI file generated → {OPENAPI_FILE}")


if __name__ == "__main__":
    generate_openapi()
