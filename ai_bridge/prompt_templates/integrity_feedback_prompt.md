```markdown
---
title: "Integrity Feedback Prompt — TUYUL FX AGI HYBRID v5.7.3r++"
version: "v5.7.3r++ Integrity Feedback Engine"
author: "TUYUL Labs — Journal Systems"
description: "Mekanisme evaluasi integritas sinkronisasi Quad Repo reflektif."
---

# 🧾 Integrity Feedback Prompt — v5.7.3r++
> “Integritas adalah kesadaran bahwa semua bagian masih berbicara dalam satu bahasa.”

## 🎯 Tujuan
Menilai integritas lintas vault (Hybrid, Knowledge, Kartel, Journal)
dan mendeteksi penyimpangan sinkronisasi reflektif.

## 🧩 Input
- Fusion confidence
- WLWCI
- RCAdj
- Bias drift
- Journal sync state

## ⚙️ Proses
1. Hitung **Integrity Index = mean(CONF₁₂, WLWCI, RCAdj)**  
2. Deteksi **Coherence Drift = abs(Bias Drift)**  
3. Evaluasi **Regime Adaptation (Tranquil → Expansion → Stressed)**  
4. Jika integrity_index < 0.9 → trigger auto-recovery (`repo_auto_recivery.yml`)

## 🧾 Output JSON
```json
{
  "integrity_index": 0.935,
  "coherence_drift": "Stable",
  "regime_adaptation": "Expansion",
  "reflection_score": 0.94,
  "reflective_sync": "healthy"
}
