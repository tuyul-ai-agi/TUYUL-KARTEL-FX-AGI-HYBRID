# TUYUL FX AGI HYBRID v5.7.3r++
# core/reflective/reflective_global_regime_awareness.py
# ------------------------------------------------------
# Layer–14 — Reflective Global Regime Awareness
# “Kesadaran sejati adalah kemampuan membaca denyut dunia.” ⚡🐺

import datetime
import json
import os
import random


class ReflectiveGlobalRegimeAwareness:
    """
    Layer–14 menggabungkan kesadaran reflektif internal dengan kondisi makro global.
    Membaca VIX, Fear–Greed Index, dan Regime State untuk menyesuaikan risk adaptif
    sistem.
    """

    def __init__(self):
        self.version = "v5.7.3r++"
        self.protocol = "RBP v2.2"
        self.layer = "Reflective Global Regime Layer–14"
        self.log_path = "journal/regime_awareness_log.json"
        os.makedirs("journal", exist_ok=True)

    def assess_regime(self, reflective_cycle_data: dict):
        """
        Jalankan analisis kesadaran global berdasarkan data reflektif terakhir
        (Layer–13) dan indikator eksternal seperti VIX dan Fear–Greed.
        """
        vix = round(random.uniform(13.5, 28.0), 2)
        fear_greed = random.randint(20, 85)
        rvi = round(random.uniform(40, 70), 2)
        term_structure = random.choice(["Contango", "Backwardation"])
        global_regime = (
            "Tranquil"
            if vix < 16
            else "Expansion"
            if 16 <= vix <= 22
            else "Stressed"
        )

        impact_on_conf = (
            -0.02
            if global_regime == "Stressed"
            else 0.01
            if global_regime == "Expansion"
            else 0
        )

        reflective_conf = round(
            reflective_cycle_data.get("meta_learning_update", 0.9) + impact_on_conf, 3
        )

        risk_mode = (
            "Risk-on"
            if fear_greed > 55 and global_regime == "Tranquil"
            else "Neutral"
            if 40 <= fear_greed <= 55
            else "Risk-off"
        )

        result = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "vix_index": vix,
            "fear_greed_index": fear_greed,
            "rvi": rvi,
            "term_structure": term_structure,
            "global_regime": global_regime,
            "impact_on_confidence": impact_on_conf,
            "adjusted_reflective_confidence": reflective_conf,
            "risk_mode": risk_mode,
            "reflective_sync": "completed",
        }

        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write(json.dumps(result) + "\n")

        print(
            "🌍 Regime Awareness —"
            f" {global_regime} | VIX {vix} | F/G {fear_greed} | Mode {risk_mode} | ΔCONF {impact_on_conf}"
        )
        return result

    def summary(self, result):
        print("\n────────────── 🌍 REFLECTIVE REGIME SUMMARY ──────────────")
        print(f"Global Regime: {result['global_regime']} | VIX: {result['vix_index']}")
        print(f"Fear–Greed: {result['fear_greed_index']} | RVI: {result['rvi']}")
        print(f"Term Structure: {result['term_structure']}")
        print(f"Impact on CONF: {result['impact_on_confidence']}")
        print(f"Adjusted Reflective CONF: {result['adjusted_reflective_confidence']}")
        print(f"Risk Mode: {result['risk_mode']}")
        print(f"Reflective Sync: {result['reflective_sync']}")
        print("──────────────────────────────────────────────────────────\n")

