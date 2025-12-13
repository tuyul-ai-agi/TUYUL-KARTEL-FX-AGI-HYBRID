import numpy as np


def adaptive_rgo(
    mean_energy, conf12, coherence_index=0.9, prev_weights=(0.4, 0.3, 0.3)
):
    """
    Menyesuaikan bobot reflektif adaptif berdasarkan energi, koherensi, dan CONF₁₂.
    α = Price Weight, β = Volume Weight, γ = Macro Influence

    Args:
        mean_energy (float): rata-rata energi reflektif dari TRQ 3D
        conf12 (float): nilai Fusion Confidence sementara
        coherence_index (float): nilai koherensi reflektif antar dimensi
        prev_weights (tuple): bobot reflektif sebelumnya (α, β, γ)
    Returns:
        dict: berisi bobot reflektif baru, gradien, dan integrity metric
    """
    alpha, beta, gamma = prev_weights

    # 🔹 Hitung deviasi energi vs CONF₁₂ → arah gradien adaptif
    deviation = (mean_energy - conf12) * coherence_index
    gradient = np.tanh(deviation * 0.8)

    # 🔹 Update reflektif: keseimbangan α, β, γ berdasarkan koherensi
    alpha += gradient * 0.6
    beta += gradient * 0.4
    gamma -= gradient * 0.3

    # 🔹 Normalisasi bobot agar total = 1
    norm_factor = alpha + beta + gamma
    weights = [round(x / norm_factor, 3) for x in (alpha, beta, gamma)]

    # 🔹 Hitung integrity: stabilitas reflektif sistem
    integrity = 1 - abs(np.mean(weights) - coherence_index)
    integrity = round(float(np.clip(integrity, 0, 1)), 3)

    # 🔹 Regime adaptif reflektif
    regime = (
        "Expansion"
        if integrity > 0.9
        else "Neutral"
        if integrity > 0.7
        else "Stressed"
    )

    return {
        "weights": weights,
        "gradient": round(float(gradient), 4),
        "integrity": integrity,
        "regime": regime,
    }

