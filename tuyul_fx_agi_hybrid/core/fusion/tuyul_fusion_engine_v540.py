from .fusion_confidence_core import compute_confidence_factors


class FusionResult:
    def __init__(self, conf12, wlwci, rcadj):
        self.conf12 = conf12
        self.wlwci = wlwci
        self.rcadj = rcadj


def run_fusion_layer12(pair: str, timeframe: str):
    factors = compute_confidence_factors(pair, timeframe)
    conf12 = round(factors["ema"] * factors["rc"] * (1 - factors["dvg"]), 3)
    wlwci = round((factors["vwap"] + conf12) / 2, 3)
    rcadj = round((factors["rc"] + wlwci) / 2, 3)
    return FusionResult(conf12, wlwci, rcadj)
