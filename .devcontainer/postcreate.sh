#!/bin/bash
echo "🧠 [TUYUL FX v6.0 Quantum] Post-create initialization..."

python3 .devcontainer/generate_vault_token.py

echo "🔄 Running initial reflective sync..."
python3 core_reflective/main_reflective_loop.py --init || true

echo "🪞 Checking repo integrity..."
python3 .devcontainer/vault_autocheck.py

echo "✅ Environment ready."
