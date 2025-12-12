# 💰 Adaptive Risk System (v5.7.3r++)

## Fungsi
Menentukan ukuran lot dan risk% dinamis berdasarkan refleksi harga dan volatilitas global.

---

## Input Utama
- `balance`
- `sl_pips`
- `pair`
- `VIX`, `RVI`
- `CONF₁₂`, `WLWCI`

---

## Rumus


risk_pct = dynamic(0.7–1.0%)
lot = (balance × risk_pct) / (sl_pips × pip_value)


---

## Integrasi Sistem
- **Fusion Analyzer** → Memberikan CONF₁₂  
- **VIX Engine** → Memberikan volatilitas global  
- **Reflective MCP** → Modul kalkulasi via `adaptive_risk_mcp`

---

## Output
| Field | Deskripsi |
|--------|------------|
| `lot` | Ukuran posisi optimal |
| `risk_pct` | Risiko adaptif |
| `rr_ratio` | Risk–Reward final |
| `integrity` | Validasi koherensi hasil |

---

## Refleksi
> “Risiko bukan musuh — ia cermin kedisiplinan algoritmik.” ⚡