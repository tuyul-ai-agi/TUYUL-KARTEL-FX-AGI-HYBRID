# 🧠 ContextInterpreter — TUYUL FX AGI HYBRID v5.7.3r++
# Menerjemahkan data reflektif menjadi konteks visual dan naratif
import json, datetime

class ContextInterpreter:
    def __init__(self, diagnostics_path="logs/reflective_diagnostics.json"):
        self.path = diagnostics_path

    def load_context(self):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
            return data[-1] if data else None
        except Exception as e:
            print(f"⚠️ Failed to load diagnostics: {e}")
            return None

    def interpret_context(self):
        ctx = self.load_context()
        if not ctx:
            return "❌ No reflective data available."
        state = ctx["reflective_state"]
        reflection = ctx["reflection_score"]
        bias = round(ctx["fusion_confidence"], 3)
        integrity = ctx["avg_integrity"]
        drift = ctx["drift"]

        summary = f"""
🧠 REFLECTIVE CONTEXT ANALYSIS ({ctx['timestamp']})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Reflection Score : {reflection} ({state})
• Integrity Index   : {integrity}
• Fusion Confidence : {bias}
• Bias Drift        : {drift}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        return summary
