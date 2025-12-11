```markdown
---
title: "Macro Regime Layer Prompt — TUYUL FX AGI HYBRID v5.7.3r++"
version: "v3.1 Macro Engine"
author: "TUYUL Labs — Kartel Systems Division"
description: "Menganalisis rezim makro dan keterkaitan antar aset lintas pasar."
---

# 🌍 Macro Regime Prompt — v5.7.3r++
> “Pasar makro adalah peta medan — serigala membaca arah angin.”

## 🎯 Tujuan
Menilai rezim makro lintas sektor (equity, bond, FX, crypto)
dan mengaitkan arah risiko global terhadap bias lokal TUYUL FX AGI.

## 🧩 Input
- Indeks global (S&P, DXY, BTC, Bond yield)
- Inflation expectations
- RSD hybrid score
- Cross-asset correlation

## ⚙️ Proses
1. Hitung RSD Hybrid (Regime State Detection)
2. Evaluasi koherensi aset lintas sektor
3. Update `macro_regime_state` & `correlation_strength`
4. Integrasikan ke Fusion → Reflective meta-loop

## 🧾 Output JSON
```json
{
  "macro_regime_state": "Expansion",
  "correlation_strength": 0.84,
  "rsd_hybrid": 0.92,
  "global_bias": "Risk-on"
}
