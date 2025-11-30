import os, json

VAULT_PATHS = {
    "FX Vault": "vaults/fx_vault/fusion_journal.json",
    "Kartel Vault": "vaults/kartel_vault/fusion_output.json",
    "Journal Vault": "vaults/journal_vault/reflection_output.json",
}

def check_vaults():
    print("🔍 Memeriksa kesehatan Vaults...")
    all_ok = True
    for name, path in VAULT_PATHS.items():
        if not os.path.exists(path):
            print(f"❌ {name}: File {path} tidak ditemukan.")
            all_ok = False
        else:
            try:
                with open(path) as f:
                    json.load(f)
                print(f"✅ {name}: Data valid.")
            except json.JSONDecodeError:
                print(f"⚠️ {name}: JSON rusak atau kosong.")
                all_ok = False
    return all_ok

if __name__ == "__main__":
    print("🧠 Vault Health Check mulai...")
    if check_vaults():
        print("✅ Semua Vault sehat.")
    else:
        print("🚨 Beberapa Vault bermasalah.")
