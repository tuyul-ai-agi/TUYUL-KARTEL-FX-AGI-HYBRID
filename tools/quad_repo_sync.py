from modules.tuyul_bots_reflective_sync import ReflectiveBridgeSync


def sync_quad_repo() -> None:
    """Sinkronisasi penuh Quad Repo."""
    sync = ReflectiveBridgeSync().run_full_sync()
    print(
        "✅ Sync OK — "
        f"Hybrid→Vault={sync['hybrid_to_vault']} | "
        f"Vault→Kartel={sync['vault_to_kartel']} | "
        f"Kartel→Journal={sync['kartel_to_journal']}"
    )


if __name__ == "__main__":
    sync_quad_repo()
