"""
GPT Command Parser v5.7.3r++
----------------------------
Parser untuk perintah reflektif TUYUL GPT:
`gas kan analisa`, `reflective cycle`, `fusion analyze`, dll.
"""

def parse_command(text: str):
    text = text.lower()
    if "reflective cycle" in text:
        return {"command": "REFLECTIVE_CYCLE", "action": "run_meta_learning"}
    if "fusion analyze" in text:
        return {"command": "FUSION_ANALYZE", "action": "analyze_fusion_layers"}
    if "gas kan analisa" in text:
        return {"command": "ANALYZE", "action": "run_reflex_pipeline"}
    return {"command": "UNKNOWN", "action": None}
