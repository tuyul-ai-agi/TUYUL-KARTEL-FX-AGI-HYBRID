import random


def compute_confidence_factors(pair, timeframe):
    """Menghitung variabel dasar fusion (EMA, VWAP, RC, DVG)."""
    ema = round(random.uniform(0.6, 0.95), 3)
    vwap = round(random.uniform(0.7, 1.0), 3)
    rc = round(random.uniform(0.65, 0.9), 3)
    dvg = round(random.uniform(0.1, 0.35), 3)
    return {"ema": ema, "vwap": vwap, "rc": rc, "dvg": dvg}
