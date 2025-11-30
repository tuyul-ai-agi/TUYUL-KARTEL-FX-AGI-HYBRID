#!/usr/bin/env bash
echo "🐺 Post-create setup untuk TUYUL AGI Hybrid..."

bash .devcontainer/submodule_init.sh
bash .devcontainer/vault_autosync.sh
python .devcontainer/vault_healthcheck.py

pip install -r requirements.txt --quiet

echo "🔐 Membuat VAULT_API_KEY otomatis..."
python .devcontainer/generate_vault_token.py

