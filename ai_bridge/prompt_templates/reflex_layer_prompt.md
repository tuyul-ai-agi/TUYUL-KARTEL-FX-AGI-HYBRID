
---
title: "Reflex Layer Prompt — TUYUL FX AGI HYBRID v5.7.3r++"
version: "v2.4 Reflex Engine"
author: "TUYUL Labs — Reflective Systems Division"
date: "2025-12-11"
license: "TUYUL LABS INTERNAL USE ONLY"
description: "Layer 1–6 Reflex Engine Prompt — membaca impuls harga mikro secara reflektif"
---

# 🧠 Reflex Layer Prompt — v5.7.3r++
> “Refleks adalah kesadaran instingtif algoritma membaca impuls harga.”

## 🎯 Tujuan
Mendeteksi struktur mikro pasar (price impulse, micro trend, RSI, EMA, VWAP alignment)  
dan menilai kesesuaian arah terhadap bias makro.

## 🧩 Input
- Data harga H1–M15  
- EMA20 / EMA50 / EMA100  
- RSI / MFI / Volume Delta  
- VWAP positioning  
- Reflex integrity state  

## ⚙️ Proses
1. Identifikasi struktur dominan (flag, break, retrace).  
2. Validasi RSI (momentum > 50 → bullish impulse).  
3. Hitung **Reflex Coherence Index (RCI)**.  
4. Hitung **Impulse Strength Factor (ISF)**.  
5. Kirim hasil ke Fusion Layer (bridge_signal: `sync_fusion`).  

## 🧾 Output JSON
```json
{
  "rci": 0.872,
  "isf": 0.911,
  "bias": "Bullish impulse",
  "confidence": 0.894,
  "bridge_signal": "sync_fusion"
}
