"""
Validate OpenAPI v5.4.0
-----------------------
Validasi struktur OpenAPI Hybrid untuk integritas endpoint.
"""

import yaml
import os

class OpenAPIValidator:
    def __init__(self, spec_path="modules/openapi_spec_46_endpoints.yaml"):
        self.spec_path = spec_path

    def validate(self):
        if not os.path.exists(self.spec_path):
            raise FileNotFoundError("OpenAPI spec not found.")
        with open(self.spec_path) as f:
            spec = yaml.safe_load(f)
        endpoints = spec.get("paths", {})
        if not endpoints:
            raise ValueError("No endpoints found in OpenAPI spec.")
        return {"status": "valid", "endpoint_count": len(endpoints)}
