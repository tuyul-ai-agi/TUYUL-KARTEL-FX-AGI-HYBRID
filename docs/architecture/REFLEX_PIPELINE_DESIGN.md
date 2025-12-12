# ⚙️ Reflex Pipeline Design (v5.7.3r++)

## Fungsi
Pipeline Reflex mendeteksi intensitas mikro dan bias harga sebelum konfirmasi makro.
Ia membaca impuls pasar awal — “refleks” dari pergerakan institusional.

---

## Komponen Pipeline

| Layer | Fungsi | Output |
|--------|---------|--------|
| **TWMS** | Trend–Wave–Momentum Scan | Arah tren dominan |
| **EMA/VWAP–EMC** | Struktur median dinamis | Bias struktural |
| **Reflex Coherence** | Integrasi antar TF (multi-frame) | RCAdj |
| **WLWCI** | Weighted Layer Coherence Index | Koherensi reflektif |

---

## Output Kunci
- `RCAdj ≥ 0.8` → Reflex stabil  
- `WLWCI ≥ 0.9` → Koherensi lintas layer kuat  

---

## Refleksi
> “Reflex membaca niat sebelum data berbicara.”
- WLWCI segment

- Divergence info
