# ============================================================
# 🧠 TUYUL FX AGI v5.8.2-HYBRID
# File: /core/reflective/vault_writer.py
# ------------------------------------------------------------
# Reflective VaultWriter v2.1 — dengan Auto Integrity Rebalance
# ============================================================

import json
import os
import statistics
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List

VAULT_PATH = "vaults/journal_vault_reflective.json"
META_PATH = "vaults/vault_meta_integrity.json"


class VaultWriter:
    """
    Menulis hasil reasoning reflektif dan menjaga konsistensi integritas Vault.
    """

    def __init__(self):
        os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)

    # ------------------------------------------------------------
    # 🧩 Menulis entri reflektif
    # ------------------------------------------------------------
    def write_entry(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        timestamp = datetime.utcnow().isoformat() + "Z"
        entry_record = {
            "timestamp": timestamp,
            "pair": entry.get("pair"),
            "timeframe": entry.get("timeframe"),
            "bias": entry.get("bias", "neutral"),
            "Fusion_Confidence": entry.get("Fusion_Confidence", 0.0),
            "WLWCI": entry.get("WLWCI", 0.0),
            "RCAdj": entry.get("RCAdj", 0.0),
            "IntegrityIndex": entry.get("IntegrityIndex", 0.0),
            "Pattern": entry.get("Pattern", "-"),
            "reflective_sync": "done",
            "meta": {
                "source": entry.get("source", "AGI-HYBRID"),
                "comment": entry.get("comment", "Auto journal sync"),
            },
        }

        with open(VAULT_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry_record, indent=2) + ",\n")

        print(f"🧾 [VAULT SYNC] {entry_record['pair']} | "
              f"{entry_record['bias']} | CONF={entry_record['Fusion_Confidence']} "
              f"| Integrity={entry_record['IntegrityIndex']}")
        return entry_record

    # ------------------------------------------------------------
    # 🧩 Membaca isi Vault
    # ------------------------------------------------------------
    def _read_vault_entries(self) -> List[Dict[str, Any]]:
        if not os.path.exists(VAULT_PATH):
            return []
        entries = []
        with open(VAULT_PATH, "r", encoding="utf-8") as f:
            raw = f.read().split("},")
            for r in raw:
                try:
                    j = json.loads(r + "}")
                    entries.append(j)
                except Exception:
                    continue
        return entries

    # ------------------------------------------------------------
    # 🧮 Auto Integrity Rebalance
    # ------------------------------------------------------------
    def auto_integrity_rebalance(self, interval_hours: int = 12):
        """
        Melakukan evaluasi ulang setiap interval_hours:
        - Menghitung rata-rata integritas
        - Mendeteksi bias drift antar entri
        - Menyimpan meta hasil reflektif ke file meta
        """
        print(f"\n🧠 [Reflective Vault] Starting Auto Integrity Rebalance... "
              f"(interval={interval_hours}h)")

        while True:
            entries = self._read_vault_entries()
            if not entries:
                print("⚠️ Vault kosong, menunggu data baru...")
                time.sleep(interval_hours * 3600)
                continue

            # Ambil semua nilai numerik
            integrity_vals = [e.get("IntegrityIndex", 0) for e in entries if isinstance(e.get("IntegrityIndex"), (int, float))]
            conf_vals = [e.get("Fusion_Confidence", 0) for e in entries if isinstance(e.get("Fusion_Confidence"), (int, float))]

            # Hitung rata-rata & deviasi
            avg_integrity = round(statistics.mean(integrity_vals), 3) if integrity_vals else 0
            avg_conf = round(statistics.mean(conf_vals), 3) if conf_vals else 0
            drift = round(statistics.pstdev(conf_vals), 3) if conf_vals else 0

            # Deteksi arah bias terakhir
            last_bias = entries[-1].get("bias", "neutral")
            bias_counts = {}
            for e in entries:
                bias = e.get("bias", "neutral")
                bias_counts[bias] = bias_counts.get(bias, 0) + 1

            # Hitung dominasi bias
            dominant_bias = max(bias_counts, key=bias_counts.get)
            bias_coherence = round(bias_counts[dominant_bias] / len(entries), 3)

            # Simpan hasil reflektif ke meta file
            meta_data = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "entries": len(entries),
                "avg_integrity": avg_integrity,
                "avg_confidence": avg_conf,
                "bias_drift": drift,
                "bias_coherence": bias_coherence,
                "dominant_bias": dominant_bias,
                "last_bias": last_bias,
                "integrity_status": "stable" if avg_integrity >= 0.85 else "degraded",
            }

            with open(META_PATH, "w", encoding="utf-8") as f:
                json.dump(meta_data, f, indent=2)

            print(f"✅ [Rebalance Complete] Entries={len(entries)} | "
                  f"Integrity={avg_integrity} | Drift={drift} | Bias={dominant_bias} "
                  f"({bias_coherence*100:.1f}%)")

            # Tunggu siklus berikutnya
            time.sleep(interval_hours * 3600)

    # ------------------------------------------------------------
    # 🧩 Ringkasan cepat Vault
    # ------------------------------------------------------------
    def summarize_vault(self) -> Dict[str, Any]:
        entries = self._read_vault_entries()
        return {
            "entries": len(entries),
            "last_entry": entries[-1] if entries else None,
            "summary_generated": datetime.utcnow().isoformat() + "Z",
        }


# ============================================================
# 🧪 DEMO RUNTIME
# ============================================================
if __name__ == "__main__":
    vw = VaultWriter()

    # Tambahkan entri simulasi
    sam
