import os, json, secrets, time

token = secrets.token_hex(32)
vault_token_path = "/workspace/configs/vault_token.json"

os.makedirs(os.path.dirname(vault_token_path), exist_ok=True)

data = {
    "token": token,
    "issued_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "issuer": "tuyul_fx_v6.0_autogen"
}

with open(vault_token_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"🔐 Vault token generated → {vault_token_path}")
