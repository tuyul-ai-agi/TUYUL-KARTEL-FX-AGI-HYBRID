# Adaptive Risk Calculator V540

**Module:** `core/risk/adaptive_risk_calculator_v540.py`

## Functions

### `_clamp(value, lower, upper)`

No description available.

### `select_reflexive_risk(wlwci, rlsi, conf12, rc_adj)`

Select the reflexive risk level (percentage) based on system coherence metrics.

### `calculate_lot_size(balance, risk_percent, sl_pips, pip_value=10.0)`

Calculate lot size using a provided risk percentage and stop-loss distance.

### `calculate_risk(balance, sl_pips)`

Calculate position sizing using an adaptive 0.7–1% risk window.

---
*Generated: 2025-11-24T05:53:34.028581+00:00*
