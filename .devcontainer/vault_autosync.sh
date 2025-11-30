#!/usr/bin/env bash
echo "🔄 Starting Multi-Vault AutoSync..."

FX_VAULT_REPO="https://github.com/tjx578/TUYUL-FX-KNOWLEDGE-VAULT-AGI.git"
KARTEL_VAULT_REPO="https://github.com/tjx578/TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI.git"
JOURNAL_VAULT_REPO="https://github.com/tjx578/TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI.git"

VAULT_DIR="/workspaces/TUYUL-KARTEL-FX-AGI-HYBRID/vaults"
mkdir -p $VAULT_DIR && cd $VAULT_DIR

for VAULT in "fx_vault $FX_VAULT_REPO" "kartel_vault $KARTEL_VAULT_REPO" "journal_vault $JOURNAL_VAULT_REPO"; do
  set -- $VAULT
  NAME=$1
  REPO=$2
  if [ ! -d "$NAME" ]; then
    git clone $REPO $NAME
  else
    echo "🟡 $NAME sudah ada, melakukan update..."
    cd $NAME && git pull && cd ..
  fi
done

echo "✅ Semua Vault tersinkronisasi."
