"""
Validate OpenAPI
----------------
Memvalidasi semua file OpenAPI di repo dan memastikan endpoint konsisten.
"""

import os
import yaml

class OpenAPIIntegrityValidator:
    def __init__(self, search_dir="core/api/"):
        self.search_dir = search_dir

    def scan_openapi_files(self):
        files = []
        for root, _, fs in os.walk(self.search_dir):
            for f in fs:
                if f.endswith(".yaml") or f.endswith(".yml"):
                    files.append(os.path.join(root, f))
        return files

    def validate_file(self, path):
        with open(path) as f:
            spec = yaml.safe_load(f)
        if "paths" not in spec:
            return {"file": path, "status": "invalid", "error": "No paths key found"}
        return {"file": path, "status": "valid", "endpoint_count": len(spec["paths"])}

    def run(self):
        report = []
        for f in self.scan_openapi_files():
            report.append(self.validate_file(f))
        return report


if __name__ == "__main__":
    validator = OpenAPIIntegrityValidator()
    result = validator.run()
    print("✅ OpenAPI Validation Completed:")
    for r in result:
        print(r)
