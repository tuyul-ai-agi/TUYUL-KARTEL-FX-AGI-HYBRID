# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Sync Hybrid Repo via GitHubBridge
# ============================================================

from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import vaultSync


def sync_hybrid_repo():
    print("🔗 Syncing Hybrid Repo via GitHubBridge...")
    result = vaultSync()
    print(f"✅ Sync Complete: {result['hybrid_to_vault']} → {result['vault_to_journal']}")
    return result


if __name__ == "__main__":
    sync_hybrid_repo()
