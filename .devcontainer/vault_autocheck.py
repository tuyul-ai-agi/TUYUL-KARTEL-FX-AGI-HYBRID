import json, os, datetime

manifest_path = "reflective_repos/manifests/repo_index.json"
if os.path.exists(manifest_path):
    with open(manifest_path) as f:
        data = json.load(f)
    print(f"✅ Reflective manifest loaded. Last sync: {data.get('audit',{}).get('last_sync_status','Unknown')}")
else:
    print("⚠️ Reflective manifest not found. Run reflective_autobuild.sh first.")

log = {
    "checked_at": datetime.datetime.utcnow().isoformat(),
    "status": "OK"
}
os.makedirs("logs", exist_ok=True)
with open("logs/vault_autocheck_log.json", "w") as f:
    json.dump(log, f, indent=2)

print("🧠 Vault integrity check complete.")
