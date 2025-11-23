from .volatility_regressor_v540 import estimate_volatility


def calculate_risk(equity: float, stop_loss_pips: float, risk_percent: float = 1.0):
    volatility_factor = estimate_volatility("XAUUSD", "H1")
    risk_amount = round(equity * (risk_percent / 100), 2)
    pip_value = 10  # placeholder per standard lot
    position_size = round((risk_amount / (stop_loss_pips * pip_value)) * volatility_factor, 3)
    return {
        "risk_amount": risk_amount,
        "position_size": position_size,
        "volatility_factor": volatility_factor,
    }
