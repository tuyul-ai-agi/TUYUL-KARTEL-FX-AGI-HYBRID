from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import vaultSync


def sync_quad_repo() -> None:
    """Sinkronisasi penuh Quad Repo."""
    sync = vaultSync()
    print(
        f"✅ Sync OK — Hybrid→Vault={sync['hybrid_to_vault']} | "
        f"Vault→Journal={sync['vault_to_journal']}"
    )


if __name__ == "__main__":
    sync_quad_repo()
