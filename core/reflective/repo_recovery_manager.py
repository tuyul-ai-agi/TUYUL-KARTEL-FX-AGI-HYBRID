# ============================================================
# 🧩 Reflective Repo Recovery Manager — TUYUL FX AGI HYBRID v5.7.3r++
# ------------------------------------------------------------
# Bertugas melakukan pemulihan otomatis (auto-recovery)
# bila salah satu vault gagal sinkronisasi.
# ============================================================

import os
import json
from datetime import datetime
from bots.tuyulagibot_tjx import log_event

RECOVERY_LOG = "logs/repo_recovery.log"


class ReflectiveRepoRecovery:
    """
    Menjalankan mekanisme pemulihan repositori reflektif otomatis.
    Terpanggil saat BOT mendeteksi integritas < 0.8 atau error sinkronisasi.
    """

    def __init__(self):
        self.vault_paths = [
            "vaults/fx_vault",
            "vaults/kartel_vault",
            "vaults/journal_vault"
        ]

    def check_integrity(self, path):
        """Cek keberadaan dan ukuran direktori"""
        if not os.path.exists(path):
            return 0.0
        total_size = sum(
            os.path.getsize(os.path.join(dp, f))
            for dp, dn, filenames in os.walk(path)
            for f in filenames
        )
        return 1.0 if total_size > 1024 else 0.5

    def recover(self):
        """Lakukan pemulihan vault yang rusak"""
        report = {"timestamp": datetime.utcnow().isoformat(), "recovered": []}
        for vault in self.vault_paths:
            integrity = self.check_integrity(vault)
            if integrity < 0.8:
                log_event(f"⚠️ Vault {vault} rusak, menjalankan recovery.")
                os.makedirs(vault, exist_ok=True)
                open(os.path.join(vault, ".recovered"), "w").write("Auto-recovered\n")
                report["recovered"].append(vault)
        with open(RECOVERY_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(report, indent=2) + "\n")
        log_event("✅ Reflective Repo Recovery selesai.")


if __name__ == "__main__":
    r = ReflectiveRepoRecovery()
    r.recover()
