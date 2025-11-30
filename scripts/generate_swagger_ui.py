"""
generate_swagger_ui.py
======================

Build Swagger UI (HTML + JSON) from OpenAPI spec.
Didesain untuk TUYUL-KARTEL-FX-AGI-HYBRID (v5.4.4-ULTRA)
Berjalan di Codespace / CI tanpa akses publik.
"""

import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPENAPI_FILE = ROOT / "docs" / "openapi_tuyul_agi_hybrid_v5.4.4-ultra.yml"
OUTPUT_DIR = ROOT / "docs" / "swagger"
SWAGGER_JSON = OUTPUT_DIR / "swagger.json"
SWAGGER_HTML = OUTPUT_DIR / "swagger.html"

SWAGGER_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>🐺 TUYUL HYBRID API (v5.4.4-ULTRA)</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
    <script>
      window.onload = () => {{
        const ui = SwaggerUIBundle({{
          url: './swagger.json',
          dom_id: '#swagger-ui',
          presets: [SwaggerUIBundle.presets.apis],
          layout: "BaseLayout",
          deepLinking: true,
        }});
        window.ui = ui;
      }};
    </script>
  </body>
</html>
"""

def main():
    print("🧠 Building Swagger UI for TUYUL-KARTEL-FX-AGI-HYBRID...")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load OpenAPI YAML
    with OPENAPI_FILE.open("r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    # Dump JSON version
    with SWAGGER_JSON.open("w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)

    # Write HTML UI
    with SWAGGER_HTML.open("w", encoding="utf-8") as f:
        f.write(SWAGGER_HTML_TEMPLATE)

    print(f"✅ Swagger UI built successfully!")
    print(f"📄 JSON: {SWAGGER_JSON}")
    print(f"🌐 HTML: {SWAGGER_HTML}")

if __name__ == "__main__":
    main()
