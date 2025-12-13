import yaml


def validate_openapi(file: str = "docs/openapi_tuyul_agi_hybrid_v5.7.8.yml") -> None:
    with open(file, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    assert "info" in schema, "❌ Field 'info' tidak ditemukan!"
    assert schema["info"]["version"] == "5.7.8", "❌ Versi OpenAPI tidak sesuai!"
    print(f"✅ OpenAPI schema valid untuk TUYUL FX AGI v{schema['info']['version']}")


if __name__ == "__main__":
    validate_openapi()
