"""
📡 TUYUL FX v5.4.0 — Vault Sync Bridge (Legacy)
===============================================
Modul sinkronisasi manual sebelum AutoSync v5.4.1 diterapkan.
"""

from tuyul_fx_agi_hybrid.core.bridge.vault_autosync_v541 import scan_and_sync

def sync_all_vaults():
    print("🔄 Manual vault synchronization (v5.4.0)")
    scan_and_sync("/mnt/data")
    print("✅ Vault sync complete.")

if __name__ == "__main__":
    sync_all_vaults()
