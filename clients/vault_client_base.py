"""
vault_client_base.py
====================

Interface Standar untuk Semua Vault Client di Ekosistem TUYUL AGI Hybrid 🧠⚡

Digunakan oleh:
- FXVaultClient        (repo: TUYUL-FX-KNOWLEDGE-VAULT-AGI)
- KartelVaultClient    (repo: TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI)
- JournalVaultClient   (repo: TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI)

Desain oleh: 🐺 TUYUL KARTEL FX ULTRA WOLF AGI-HYBRID v5.4.4
Fungsi:
---------
- Menyediakan *kontrak* generik untuk setiap Vault Client
- Mengatur lifecycle, CRUD, dan query semantik antar Vault
- Memastikan semua vault sinkron, sehat, dan terukur (statistik + integritas)

"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable


# =====================================================================
# 🧩 BaseVaultClient Interface
# =====================================================================

@runtime_checkable
class BaseVaultClient(Protocol):
    """
    Interface generik yang wajib diimplementasikan tiap Vault Client.

    Kontrak minimum:
    ----------------
    - lifecycle: connect, health_check
    - CRUD dokumen: load_document, save_document, list_documents
    - query semantik: semantic_search
    - monitoring: get_stats
    """

    # ---- lifecycle ----
    def connect(self) -> None:
        """Inisialisasi koneksi ke vault (misal via REST, WebSocket, atau Local I/O)."""
        ...

    def health_check(self) -> bool:
        """Cek status koneksi dan kredensial ke Vault."""
        ...

    # ---- CRUD utama ----
    def load_document(self, doc_id: str) -> Dict[str, Any]:
        """Ambil satu dokumen berdasarkan ID."""
        ...

    def save_document(self, payload: Dict[str, Any]) -> str:
        """Simpan dokumen baru ke Vault dan kembalikan ID-nya."""
        ...

    def list_documents(
        self,
        *,
        limit: int = 50,
        cursor: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Ambil daftar dokumen dengan pagination dan optional filter."""
        ...

    # ---- Query semantik / metadata ----
    def semantic_search(
        self,
        query: str,
        *,
        top_k: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Cari dokumen dengan query semantik atau metadata tertentu."""
        ...

    # ---- Monitoring ----
    def get_stats(self) -> Dict[str, Any]:
        """Ambil statistik Vault (jumlah dokumen, integritas, dsb)."""
        ...


# =====================================================================
# 💾 VaultSyncResult DataClass
# =====================================================================

@dataclass
class VaultSyncResult:
    """
    Hasil operasi sinkronisasi lintas-vault.

    Contoh isi:
    -----------
    {
        "synced_count": 12,
        "skipped_count": 2,
        "errors": ["journal_vault timeout"],
        "details": [
            {"doc_id": "fusion_2025_11_29", "status": "synced"},
            {"doc_id": "bias_audit_2025_11_28", "status": "skipped"}
        ]
    }

    Digunakan oleh:
    - TriVaultSyncLoop (pipeline/tri_vault_sync_loop.py)
    - VaultDiffSync (core/vaults/vault_diff_sync.py)
    - vault_integrity_audit.yml (GitHub Action CI/CD)
    """

    synced_count: int
    skipped_count: int = 0
    errors: Optional[List[str]] = None
    details: Optional[List[Dict[str, Any]]] = None

    def __post_init__(self) -> None:
        if self.errors is None:
            self.errors = []
        if self.details is None:
            self.details = []

    def summary(self) -> Dict[str, Any]:
        """Ringkasan hasil sinkronisasi dalam format JSON-ready."""
        return {
            "synced": self.synced_count,
            "skipped": self.skipped_count,
            "error_count": len(self.errors),
            "details_count": len(self.details),
        }
