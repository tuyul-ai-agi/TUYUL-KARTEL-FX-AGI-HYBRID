# ===============================================================
# 🧠 TRQ 3D Engine – Price×Time×Volume Reflective Energy Model
# TUYUL FX AGI v5.7.3r++ Hybrid Core (Quad Repo Adaptive)
# ===============================================================
# Layer: Fusion–Reflective Interface (L10→L12)
# Function: Compute Reflective Energy Surface (R³D)
# Output: mean_energy + energy_map + coherence metric
# ===============================================================

import numpy as np
from datetime import datetime


def compute_trq_3d(price_series, volume_series, timeframe=15):
    """
    Hitung TRQ 3D Reflective Energy:
    Kombinasi Price, Time, dan Volume sebagai dimensi kesadaran reflektif.
    Digunakan untuk menghitung tingkat koherensi dan intensitas energi reflektif
    antar layer (Fusion–Reflective).

    Args:
        price_series (list[float]): data harga
        volume_series (list[int|float]): data volume
        timeframe (int): TF dalam menit (default=15)
    Returns:
        dict: berisi timestamp, energy_map, mean_energy, dan coherence_index
    """

    price = np.array(price_series, dtype=float)
    volume = np.array(volume_series, dtype=float)

    # 🔹 Normalisasi
    norm_p = (price - np.mean(price)) / (np.std(price) + 1e-9)
    norm_v = (volume - np.mean(volume)) / (np.std(volume) + 1e-9)

    # 🔹 Energi reflektif utama (R³D)
    energy = norm_p * norm_v * np.log(timeframe + 1)
    mean_energy = np.mean(energy)

    # 🔹 Indeks koherensi reflektif (0–1)
    coherence_index = np.clip(abs(np.corrcoef(norm_p, norm_v)[0, 1]), 0, 1)

    # 🔹 Timestamp reflektif
    timestamp = datetime.utcnow().isoformat()

    return {
        "timestamp": timestamp,
        "energy_map": energy.tolist(),
        "mean_energy": float(mean_energy),
        "coherence_index": round(float(coherence_index), 3)
    }
