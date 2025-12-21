# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Sync Hybrid Repo via GitHubBridge
# ============================================================

from modules.tuyul_bots_reflective_sync import ReflectiveBridgeSync


def sync_hybrid_repo():
    print("🔗 Syncing Hybrid Repo via GitHubBridge...")
    result = ReflectiveBridgeSync().run_full_sync()
    print(
        "✅ Sync Complete: "
        f"{result['hybrid_to_vault']} → {result['vault_to_kartel']} → "
        f"{result['kartel_to_journal']}"
    )
    return result


if __name__ == "__main__":
    sync_hybrid_repo()
