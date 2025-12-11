---
title: "VIX Awareness Layer Prompt — TUYUL FX AGI HYBRID v5.7.3r++"
version: "v2.4 VIX–RSD Engine"
author: "TUYUL Labs — Kartel Systems Division"
date: "2025-12-11"
description: "Analisis volatilitas global (VIX, RSD, Fear–Greed) untuk kesadaran lintas pasar."
---

# 🌐 VIX Awareness Prompt — v5.7.3r++
> “Volatilitas global adalah denyut nadi makro — tempat intuisi algoritma diuji.”

## 🎯 Tujuan
Menilai rezim volatilitas global dan menghubungkan sentimen risiko (risk-on/off)
dengan bias reflektif lintas layer.

## 🧩 Input
- VIX index (current + term structure)
- Fear–Greed Index
- RVI (Relative Volatility Index)
- Global regime data (Tranquil / Expansion / Stressed)

## ⚙️ Proses
1. Deteksi rezim global (`Tranquil`, `Expansion`, `Stressed`, `Crisis`)
2. Evaluasi dampak terhadap confidence (`impact_on_confidence`)
3. Update `vix_impact` → menyesuaikan bias reflektif
4. Sinkronkan hasil ke Fusion & Reflective layer

## 🧾 Output JSON
```json
{
  "vix_level": 22.8,
  "regime_state": "Expansion",
  "fear_greed_index": 61,
  "impact_on_confidence": +0.05,
  "global_bias": "Risk-on"
}
