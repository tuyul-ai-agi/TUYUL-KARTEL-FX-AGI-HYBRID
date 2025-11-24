# Tuyul Data Adapter

**Module:** `core/adapters/tuyul_data_adapter.py`

## Functions

### `__init__(self)`

No description available.

### `fetch_live_data(self, pair, interval)`

Return simulated OHLC feed data for a symbol.

Args:
    pair: Trading pair to fetch.
    interval: Timeframe for the feed.

Returns:
    Dictionary with OHLC and volume values.

### `save_feed(self, data)`

Persist feed data to the live feed vault.

---
*Generated: 2025-11-24T05:49:57.154856+00:00*