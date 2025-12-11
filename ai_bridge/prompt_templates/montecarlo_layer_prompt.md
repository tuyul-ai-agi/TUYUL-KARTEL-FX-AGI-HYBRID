```markdown
---
title: "Monte Carlo Simulation Prompt — TUYUL FX AGI HYBRID v5.7.3r++"
version: "v2.2 Monte Carlo Engine"
author: "TUYUL Labs — Hybrid Simulation Group"
description: "Simulasi probabilitas tren reflektif dengan 20.000 iterasi / 90 hari."
---

# 🎲 Monte Carlo Simulation Prompt — v5.7.3r++
> “Refleksi sejati diuji bukan pada satu momen — tapi pada 20.000 kemungkinan.”

## 🎯 Tujuan
Menjalankan simulasi reflektif lintas layer untuk mengukur probabilitas tren, drawdown,
dan stabilitas bias reflektif.

## 🧩 Input
- Fusion metrics (`conf12`, `wlwci`, `rcadj`)
- Price history (D1, W1)
- Volatility factor
- Integrity index baseline

## ⚙️ Proses
1. Jalankan simulasi Monte Carlo 20.000 iterasi / 90 hari  
2. Hitung win, TP1, TP2, SL probabilities  
3. Evaluasi max drawdown dan confidence interval  
4. Validasi koherensi distribusi bias reflektif  

## 🧾 Output JSON
```json
{
  "iterations": 20000,
  "period_days": 90,
  "win_probability": 91.8,
  "tp1_probability": 92.3,
  "tp2_probability": 90.9,
  "sl_probability": 8.7,
  "max_drawdown": -1.7,
  "distribution_result": "Bullish Extension",
  "confidence_interval": 0.89
}
