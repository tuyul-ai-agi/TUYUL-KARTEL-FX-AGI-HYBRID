from ..vaults.reflection_output import save_reflection_report


def analyze_reflection(last_conf12, current_conf12):
    delta = round(current_conf12 - last_conf12, 3)
    bias = "positive" if delta > 0 else "negative"
    report = {"delta_conf12": delta, "bias": bias}
    save_reflection_report(report)
    return report
