from friendly_lamp_x54j5rxggj9wfrwr_5526_app_github_dev__jit_plugin import riskCalculate


def balance_control(pair="XAUUSD", balance=100000, sl_pips=50):
    """Hitung keseimbangan reflektif Hybrid Balance."""

    risk = riskCalculate({"pair": pair, "balance": balance, "sl_pips": sl_pips})
    print(f"🧮 Risk={risk['risk_pct']}% | Lot={risk['lot']} | RR={risk['rr_ratio']}")
    return risk


def main():
    balance_control()


if __name__ == "__main__":
    main()
