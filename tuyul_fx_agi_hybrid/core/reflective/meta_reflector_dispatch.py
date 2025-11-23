from .reflective_reasoner_v540 import analyze_reflection


def run_meta_reflection(fusion_output):
    """Jalankan refleksi otomatis terhadap hasil reasoning terakhir."""
    try:
        last_conf12 = 0.75
        report = analyze_reflection(last_conf12, fusion_output.conf12)
        return {"reflection_status": "ok", "report": report}
    except Exception as e:
        return {"reflection_status": "error", "detail": str(e)}
