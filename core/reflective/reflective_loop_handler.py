"""
Reflective loop handler for adaptive reflective cycle.
"""

from datetime import datetime
from typing import Any, Dict, Iterable

from core.analytics.trq_3d_engine import compute_trq_3d
from core.fusion.fusion_confidence import fusion_confidence
from core.fusion.rgo_optimizer import adaptive_rgo
from core.journal.reflective_journal_sync import sync_to_journal
from core.repo.kartel_macro_bridge import get_macro_context


def run_reflective_cycle(
    price_series: Iterable[float], volume_series: Iterable[float], pair: str = "XAUUSD"
) -> Dict[str, Any]:
    """
    Jalankan satu siklus reflektif penuh.

    Menggabungkan TRQ 3D, RGO, Fusion Confidence, dan Macro Bridge untuk menghasilkan
    entri jurnal reflektif lengkap.

    Args:
        price_series: Deret harga.
        volume_series: Deret volume transaksi.
        pair: Pasangan mata uang/aset yang dianalisis.

    Returns:
        Hasil reflektif lengkap untuk satu siklus.
    """
    print(f"\n🧠 [REFLECTIVE LOOP] Starting reflective cycle for {pair} ...")

    trq = compute_trq_3d(price_series, volume_series)
    print(f"   → TRQ_3D mean_energy: {round(trq['mean_energy'], 4)}")

    macro = get_macro_context()
    print(
        "   → Macro context: "
        f"VIX={macro['VIX']}, RVI={macro['RVI']}, Regime={macro['GlobalRegime']}"
    )

    rgo = adaptive_rgo(trq["mean_energy"], conf12=0.9)
    print(f"   → Updated Reflective Weights: {rgo['weights']} (grad={rgo['gradient']})")

    fusion = fusion_confidence(trq["mean_energy"], rgo["weights"], macro["RVI"])
    print(f"   → FusionConfidence={fusion['conf12']}, RCAdj={fusion['rcadj']}")

    entry = {
        "pair": pair,
        "timestamp": datetime.utcnow().isoformat(),
        "TRQ_mean_energy": trq["mean_energy"],
        "FusionConfidence": fusion["conf12"],
        "RCAdj": fusion["rcadj"],
        "weights": rgo["weights"],
        "VIX": macro["VIX"],
        "RVI": macro["RVI"],
        "GlobalRegime": macro["GlobalRegime"],
        "integrity_index": macro["integrity_index"],
    }

    sync_to_journal(entry)

    print(f"✅ [DONE] Reflective cycle complete for {pair}\n")

    return {
        "pair": pair,
        "trq": trq,
        "macro": macro,
        "rgo": rgo,
        "fusion": fusion,
        "entry": entry,
    }
