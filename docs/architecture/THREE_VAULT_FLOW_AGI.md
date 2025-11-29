# TUYUL AGI – THREE VAULT FLOW (FX, KARTEL, JOURNAL)

Dokumen ini menjelaskan **alur data dan peran 3 vault utama** dalam ekosistem TUYUL AGI:

- **FX Knowledge Vault**  
  Repo: `TUYUL-FX-KNOWLEDGE-VAULT-AGI`
- **Kartel Knowledge Vault (Reflective Memory)**  
  Repo: `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI`
- **Journal Vault (Empirical Experience Layer)**  
  Repo: `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI`
- **AGI Hybrid (Otak Tengah / Orchestrator)**  
  Repo: `TUYUL-KARTEL-FX-AGI-HYBRID`

---

## 1. Peran Tiap Komponen

### 1.1 FX Knowledge Vault (`TUYUL-FX-KNOWLEDGE-VAULT-AGI`)

- **Fungsi utama:**
  - Menyimpan **pengetahuan objektif**:
    - Blueprint strategi
    - SOP trading
    - Algoritma psikologi trading
    - Simulasi Monte Carlo
    - Integrasi TWMS
- **Karakter:**
  - Konten cenderung **stabil** dan “textbook”.
  - Menjadi **ground truth teori** bagi seluruh sistem.

> Pertanyaan yang dijawab FX Vault:  
> “Menurut sistem & teori, bagaimana seharusnya kita bertindak?”

---

### 1.2 Kartel Knowledge Vault (`TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI`)

- **Fungsi utama:**
  - Menyimpan **memori reflektif AGI**:
    - Refleksi dari banyak sesi reasoning
    - Heuristic yang sudah distabilkan
    - Meta-knowledge tentang bias, kesalahan, dan perbaikan
- **Karakter:**
  - Berisi **pengetahuan hasil pembelajaran internal AGI**, bukan teori murni.
  - Struktur rapi dalam bentuk:
    - Markdown
    - JSON manifest
    - FAISS / vector store reflektif

> Pertanyaan yang dijawab Kartel Vault:  
> “Apa yang sudah kupelajari dari pengalaman sebelumnya, dan heuristic apa yang biasanya bekerja?”

---

### 1.3 Journal Vault (`TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI`)

- **Fungsi utama:**
  - Menjadi **lapisan pengalaman empiris**:
    - Jurnal harian
    - Catatan sesi reasoning
    - Log eksperimen (backtest/forwardtest/live)
    - Notebook analisis
- **Karakter:**
  - Data cenderung **mentah / semi-mentah**:
    - CSV trades
    - Log reasoning
    - Jupyter Notebook
  - Digunakan sebagai **bahan baku** untuk:
    - Refleksi (yang masuk ke Kartel Vault),
    - Evaluasi heuristic & strategi.

> Pertanyaan yang dijawab Journal Vault:  
> “Apa saja yang benar-benar sudah terjadi di lapangan? Bagaimana performa sebenarnya?”

---

### 1.4 AGI Hybrid (`TUYUL-KARTEL-FX-AGI-HYBRID`)

- **Fungsi utama:**
  - **Orchestrator reasoning** yang menggabungkan:
    - Teori dari FX Vault
    - Refleksi & heuristic dari Kartel Vault
    - Data empiris dari Journal Vault
- **Karakter:**
  - Mengambil keputusan / menghasilkan reasoning baru.
  - Mengirim kembali:
    - Pengalaman baru ke Journal Vault,
    - Refleksi terstruktur ke Kartel Vault (secara langsung atau via pipeline).

---

## 2. Diagram Alur Tingkat Tinggi (High-Level Flow)

Secara konseptual, alur data 3-vault + Hybrid adalah:

```text
        (1) Teori & Algoritma
  ┌────────────────────────────────┐
  │  TUYUL-FX-KNOWLEDGE-VAULT-AGI │
  │          (FX Vault)           │
  └────────────────────────────────┘
                 ▲
                 │  query_knowledge()
                 │
                 │
                 │
┌────────────────▼────────────────┐
│    TUYUL-KARTEL-FX-AGI-HYBRID   │
│           (AGI Hybrid)          │
│   - Orchestrator reasoning      │
│   - Decision engine             │
└────────────────▲────────────────┘
                 │
                 │  query_memory()                (2) Refleksi & Heuristic Stabil
                 │
  ┌────────────────────────────────┐
  │ TUYUL-KARTEL-FX-KNOWLEDGE-    │
  │        VAULT-AGI              │
  │   (Kartel Reflective Vault)   │
  └────────────────────────────────┘

                 │
                 │  log_decision(), log_experiment()
                 ▼
  ┌────────────────────────────────┐
  │ TUYUL-KARTEL-FX-JOURNAL-       │
  │        VAULT-AGI               │
  │   (Journal / Empirical Layer)  │
  └────────────────────────────────┘
                 ▲
                 │  (batch analysis, notebooks)
                 │  generate_reflection_candidates()
                 │
                 └───────────────►
            Kartel Vault (write_reflection(), update_heuristic())
```

Ringkasan:

1. **AGI Hybrid** meminta teori ke **FX Vault**.
2. AGI Hybrid membaca memori reflektif & heuristic dari **Kartel Vault**.
3. AGI Hybrid membuat keputusan / reasoning baru.
4. Hasil keputusan & konteksnya dicatat ke **Journal Vault**.
5. Notebook / pipeline di Journal Vault menganalisis data, menghasilkan kandidat refleksi / heuristic baru.
6. Kandidat refleksi tersebut disaring, lalu dipromosikan ke **Kartel Vault** sebagai memori reflektif yang terstruktur.

---

## 3. Alur Detail Per-Request (Decision Cycle)

Pada setiap siklus pengambilan keputusan (misalnya user meminta rekomendasi trading):

1. **Input Masuk ke AGI Hybrid**
   - Query user / kondisi market / state portofolio.

2. **AGI Hybrid → FX Vault**
   - Memanggil endpoint seperti:
     - `GET /knowledge/search`
     - `GET /strategy/{id}`
   - Tujuan:
     - Mengambil **teori & aturan baku** terkait konteks saat ini.

3. **AGI Hybrid → Kartel Vault**
   - Memanggil endpoint seperti:
     - `POST /memory/query` (dengan query & konteks)
   - Tujuan:
     - Mengambil **refleksi lampau, heuristic, dan pattern** yang relevan dengan situasi sekarang.

4. **AGI Hybrid → Journal Vault (opsional, saat online)**
   - Mengambil data empiris terbaru, misalnya:
     - Performa strategi X minggu terakhir,
     - Pola drawdown terakhir.
   - Endpoint contoh:
     - `GET /journal/daily?date=...`
     - `GET /experiments/summary?strategy=...`

5. **AGI Hybrid – LLM Reasoning**
   - Menyatukan tiga konteks:
     - `theory_context`    ← dari FX Vault
     - `reflective_context`← dari Kartel Vault
     - `empirical_context` ← dari Journal Vault
   - Menggunakan LLM (GPT) dengan prompt yang memadukan:
     - aturan teoritis,
     - heuristic,
     - data empiris terkini.

6. **Keputusan & Logging**
   - AGI Hybrid menghasilkan:
     - rekomendasi / aksi,
     - reasoning trace (penjelasan langkah demi langkah),
     - confidence level.
   - Hasil ini disimpan ke **Journal Vault**:
     - `POST /journal/entry`
       - berisi query, keputusan, outcome (jika sudah ada), dan reasoning trace.

---

## 4. Alur Refleksi Berkala (Batch Reflection Cycle)

Secara terpisah, ada proses berkala (harian/mingguan) untuk memperbarui pengetahuan reflektif:

1. **Journal Vault – Analisis & Notebook**
   - Notebook/pipeline membaca:
     - `data/raw/` dan `data/processed/`,
     - `journals/daily/`,
     - `journals/sessions/`,
     - hasil eksperimen.
   - Mencari:
     - pola keberhasilan/kegagalan strategi,
     - perubahan behaviour setelah drawdown,
     - bias psikologis berulang.

2. **Generate Kandidat Refleksi & Heuristic**
   - Script (misalnya `generate_reflection_candidates.py`) membuat:
     - ringkasan refleksi,
     - calon aturan heuristic,
     - laporan performa per strategi.
   - Disimpan ke:
     - `data/exports/to_kartel/*.json`.

3. **Export ke Kartel Vault**
   - Workflow (misal `summarize_journal_to_kartel.yml`) atau AGI Hybrid memanggil:
     - `POST /memory/reflect_batch` di Kartel Vault.
   - Payload berisi:
     - kandidat refleksi,
     - evidensi dari jurnal (link / id entry),
     - saran update heuristic.

4. **Kartel Vault Memperbarui Memori**
   - Kartel Vault:
     - menulis file baru di `reflections/`,
     - memperbarui `knowledge/heuristics/*.md`,
     - mengupdate `vector_store/reflective/`.
   - Manifest & index (`kartel_vault_manifest_vX.json`, `knowledge_index_kartel.json`) ikut diperbarui.

---

## 5. Kontrak Minimal antar Komponen

Agar 3 vault + Hybrid dapat bekerja bersama dengan baik, hal-hal berikut sebaiknya distandarkan:

### 5.1. ID & Referensi Silang

- Setiap **sesi reasoning** yang dicatat di Journal:
  - punya `session_id` unik.
- Kartel Vault menyimpan:
  - referensi ke `session_id` asal refleksi.
- Dengan ini, dari satu refleksi di Kartel, bisa:
  - “zoom in” ke detail sesi / jurnal lengkap di Journal Vault.

### 5.2. Tagging & Metadata

Minimal metadata konsisten di 3 tempat:

- `symbol` (e.g. EURUSD, XAUUSD)
- `strategy_id` atau `strategy_name`
- `timeframe` (M5, H1, H4, dsb.)
- `market_regime` (trending, ranging, volatile, dsb.)
- `bias_type` (jika ada: FOMO, revenge trade, dsb.)

Ini memudahkan:

- Query silang dari AGI Hybrid,
- Pencarian refleksi,
- Evaluasi heuristic berdasarkan jurnal.

### 5.3. Format Ringkasan untuk Kartel Vault

Saat Journal Vault mengekspor ke Kartel Vault:

- Format minimal (konseptual):

```jsonc
{
  "session_id": "2025-01-01_session_0001",
  "time_range": ["2025-01-01T09:00:00Z", "2025-01-01T12:00:00Z"],
  "symbols": ["EURUSD"],
  "strategies": ["EMA_DIVERGENCE_V5"],
  "key_events": [
    "3 consecutive losses after news event",
    "overtrading detected after drawdown"
  ],
  "reflection_summary": "Pada sesi ini, AGI cenderung overtrade setelah 3 kali loss beruntun...",
  "candidate_heuristics": [
    "Jika drawdown harian > 3R, hentikan trading selama minimal 2 jam.",
    "Kurangi size posisi 50% setelah 2 loss beruntun."
  ],
  "evidence_links": [
    "journal://sessions/2025-01-01_session_0001",
    "journal://daily/2025-01-01"
  ]
}
```

- Kartel Vault kemudian:
  - Menyimpan `reflection_summary` di `reflections/sessions/`.
  - Menyatukan `candidate_heuristics` ke `knowledge/heuristics/*.md`.
  - Mengupdate vector store reflektif.

---

## 6. Posisi Dokumen Ini dalam Repo

File ini berada di:

```text
TUYUL-KARTEL-FX-AGI-HYBRID/
└─ docs/
   └─ architecture/
      └─ THREE_VAULT_FLOW_AGI.md
```

**Tujuan:**

- Menjadi rujukan tunggal arsitektur alur data 3-vault.
- Menjamin bahwa perubahan di satu vault (FX / Kartel / Journal) tetap selaras dengan:
  - Cara AGI Hybrid melakukan reasoning,
  - Cara memori reflektif dibentuk & diperbarui.
