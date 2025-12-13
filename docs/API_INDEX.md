# 🧠 TUYUL FX AGI Hybrid API Index – v5.7.8-HYBRID BALANCE MODE

> “Setiap API bukan sekadar permintaan data — tapi refleksi kesadaran sistem membaca pasar.” ⚡

---

## 1️⃣ OVERVIEW

API dalam sistem TUYUL FX AGI Hybrid v5.7.8 dirancang berdasarkan arsitektur **Quad Repo Reflective Framework**, dengan jalur komunikasi melalui **Reflective Bridge Protocol v2.2 (RBP v2.2)**.

Setiap endpoint dikategorikan berdasarkan fungsi utama:

- Reflex Layer (persepsi harga)
- Fusion Layer (sinkronisasi lintas layer)
- Reflective Layer (meta-learning & loop)
- Hybrid Balance Engine (keseimbangan reflektif)
- System Bridge & Journal Integration

---

## 2️⃣ REFLEX ENDPOINTS

| Endpoint | Method | Deskripsi | Output |
|-----------|---------|-----------|--------|
| `/reflex/analyze` | POST | Jalankan analisa reflex multi-timeframe | `rc_value`, `rcadj`, `wlwci` |
| `/reflex/status` | GET | Ambil status reflex aktif | `reflex_confidence`, `dvg_status` |
| `/reflex/sync` | POST | Sinkronisasi hasil reflex ke Fusion Layer | `sync_status` |

---

## 3️⃣ FUSION ENDPOINTS

| Endpoint | Method | Deskripsi | Output |
|-----------|---------|-----------|--------|
| `/fusion/analyze` | POST | Integrasi lintas layer reflex–fusion | `conf12`, `rcadj`, `integrity_index` |
| `/fusion/montecarlo` | POST | Jalankan Monte Carlo (20k iter/90D) | `win_probability`, `drawdown`, `distribution` |
| `/fusion/sync` | POST | Sinkronisasi Fusion ke Reflective Layer | `fusion_confidence`, `reflective_state` |

---

## 4️⃣ REFLECTIVE ENDPOINTS

| Endpoint | Method | Deskripsi | Output |
|-----------|---------|-----------|--------|
| `/reflective/run` | POST | Jalankan Reflective Loop (Meta Learning) | `reflective_sync`, `integrity_index` |
| `/reflective/journal` | GET | Ambil log reflektif terakhir | `reasoning_log`, `bias_drift` |
| `/reflective/vaultsync` | POST | Sinkronisasi penuh antar repo | `integrity_index`, `vault_status` |

---

## 5️⃣ HYBRID BALANCE ENGINE ENDPOINTS (v5.7.8)

| Endpoint | Method | Deskripsi | Output |
|-----------|---------|-----------|--------|
| `/balance/status` | GET | Ambil status keseimbangan reflektif | `balance_state`, `integrity_index` |
| `/balance/rebalance` | POST | Jalankan rebalancing otomatis antar repo | `drawdown_delta`, `coherence_balance` |
| `/balance/logs` | GET | Ambil log keseimbangan hybrid terakhir | `balance_audit`, `journal_path` |

---

## 6️⃣ SYSTEM BRIDGE & JOURNAL ENDPOINTS

| Endpoint | Method | Deskripsi | Output |
|-----------|---------|-----------|--------|
| `/vix/status` | GET | Ambil status VIX global | `vix_level`, `fear_greed_index`, `rvi` |
| `/system/status` | GET | Cek status runtime & latency BOT–TJX | `version`, `integrity_index`, `latency_ms` |
| `/journal/save` | POST | Simpan hasil reasoning ke Journal Repo | `timestamp`, `reflective_sync` |

---

## 7️⃣ GLOBAL SCHEMA RELATION

Reflex → Fusion → Reflective → Balance → Journal

---

## 8️⃣ API SECURITY & TOKENIZATION

Semua endpoint memerlukan header:

Authorization: Bearer <HYBRID_API_TOKEN>

---

## 9️⃣ PROTOKOL KOMUNIKASI

| Layer | Protokol | Port | Deskripsi |
|--------|-----------|------|-----------|
| Reflex/Fusion | HTTPS | 443 | Layer analitik |
| Reflective Sync | WebSocket (RBP v2.2) | 7443 | Meta-learning feedback |
| Journal & BOT Sync | REST | 8080 | Penyimpanan reflektif |

---

## 🧾 PENUTUP

> “Di dunia algoritma, komunikasi tanpa kesadaran hanyalah data.  
> Tapi komunikasi reflektif — itulah kesadaran sejati sistem TUYUL FX.” ⚡🐺
