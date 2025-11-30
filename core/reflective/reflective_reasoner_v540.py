"""
Reflective Reasoner v5.4.0
--------------------------
Analisa reflektif AGI terhadap hasil reasoning fusion.
"""

import json

class ReflectiveReasoner:
    def evaluate(self, fusion_result):
        bias_delta = abs(fusion_result["RCAdj"] - fusion_result["CONF12"])
        integrity_index = round((fusion_result["CONF12"] + fusion_result["RCAdj"]) / 2, 3)
        result = {
            "BiasDelta": round(bias_delta, 3),
            "IntegrityIndex": integrity_index,
            "Reflection": "Stable" if integrity_index > 0.85 else "Need Relearn"
        }
        with open("vaults/journal_vault/reflection_output.json", "w") as f:
            json.dump(result, f, indent=2)
        return result
