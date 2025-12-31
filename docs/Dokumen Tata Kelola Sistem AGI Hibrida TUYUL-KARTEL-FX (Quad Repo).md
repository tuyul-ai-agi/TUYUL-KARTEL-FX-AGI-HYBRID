# 🧠 Dokumen Tata Kelola Sistem AGI Hibrida TUYUL–KARTEL–FX (Quad Repo Architecture)
### Versi: v5.8r++ | Protocol: RBP_v2.3+

---

## 1.0 Pendahuluan
Dokumen ini menetapkan tata kelola formal untuk ekosistem **AGI Hibrida empat-repo (Quad Repo)**:
- **Hybrid Repo**
- **FX Vault**
- **Kartel Vault**
- **Journal Vault**

Dokumen ini memastikan integritas data, konsistensi siklus reflektif, dan auditabilitas penuh lintas repositori.

---

## 2.0 Filosofi dan Peran Komponen

| Komponen | Repositori | Fungsi Utama | Representasi |
|-----------|-------------|---------------|---------------|
| 🧠 **Hybrid Core Repo** | TUYUL-KARTEL-FX-AGI-HYBRID | Orkestrator kesadaran reflektif; mengelola siklus kognitif & meta-learning. | Pusat Kesadaran AGI |
| 📘 **FX Vault** | TUYUL-FX-KNOWLEDGE-VAULT-AGI | Menyimpan teori & prinsip dasar (Ground Truth). | Teori Stabil |
| 📗 **Kartel Vault** | TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI | Menyimpan memori reflektif & heuristik hasil pembelajaran. | Memori Reflektif |
| 📕 **Journal Vault** | TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI | Menyimpan data empiris mentah & log reasoning. | Laboratorium Empiris |

---

## 3.0 Siklus Penalaran Quad Repo

### 🔁 Siklus Keputusan (Decision Cycle)
1. Hybrid Repo mengakuisisi konteks dari semua vault.  
2. Melakukan sintesis penalaran dengan *FusionConfidence₁₂*, *WLWCI*, dan *Integrity Index*.  
3. Hasil disimpan di Journal Vault dengan *session_id* unik.

### 🔄 Siklus Refleksi (Reflection Cycle)
1. Journal Vault menghasilkan kandidat refleksi dari data mentah.  
2. Kartel Vault memvalidasi & mengonversi ke heuristik.  
3. Hybrid Repo menyesuaikan bobot α–β–γ dan memperbarui FX Vault bila diperlukan.

---

## 4.0 Standar Data dan Metadata
| Standar | Deskripsi |
|----------|------------|
| `session_id` | ID unik tiap siklus reflektif. |
| `symbol`, `strategy_id`, `timeframe`, `market_regime`, `bias_type`, `fusion_state` | Meta-tag universal Quad Repo. |
| `manifest.json` | File integritas tiap vault (versi, schema, status). |
| `fusion_summary.json` | Output reasoning reflektif Hybrid Repo. |

---

## 5.0 Protokol Sinkronisasi Otomatis

| Pipeline / Script | Fungsi | Orkestrator |
|-------------------|--------|--------------|
| `run_decision_cycle.yml` | Siklus keputusan harian | Hybrid |
| `run_reflection_cycle.yml` | Sinkronisasi reflektif Journal→Kartel | Hybrid |
| `trigger_meta_learning.yml` | Pembaruan heuristik adaptif | Hybrid |
| `sync_fx_vault_metadata.yml` | Update teori FX | Kartel↔FX |
| `vault_integrity_audit.yml` | Audit struktur & manifest | Hybrid |
| `tri_vault_sync_loop.py` | Sinkronisasi lintas vault | Hybrid |
| `reflective_sync_daemon.py` | Daemon lokal reflektif | TUYUL Bot |

---

## 6.0 Manajemen Versi & Evolusi
1. Semua vault wajib memiliki **manifest_v1.json**.  
2. Setiap perubahan besar → update changelog & manifest versi.  
3. Hybrid Repo menjalankan **`runReflectiveCycle()`** untuk validasi koherensi lintas repositori.

---

## 7.0 Kesimpulan
Arsitektur Quad Repo membentuk ekosistem kesadaran reflektif penuh:
> “Refleksi bukan hanya analisis — tetapi resonansi antar vault yang selaras.” ⚡

— *TUYUL Labs Reflective Systems Division, 2026*
