"""
Run Sync Vault
--------------
Manual sync antar vaults (FX ↔ Kartel ↔ Journal).
"""

from pipeline.tri_vault_sync_loop import TriVaultSyncLoop

if __name__ == "__main__":
    sync = TriVaultSyncLoop()
    result = sync.run()
    print("[SYNC RESULT]")
    print(result)
