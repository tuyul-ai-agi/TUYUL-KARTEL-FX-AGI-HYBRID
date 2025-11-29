"""
RLSI Module v5.4.0
------------------
Reflex Layer Smart Index — deteksi momentum mikro jangka pendek.
"""

from __future__ import annotations

import pandas as pd


class RLSIModule:
    """Hitung RLSI berbasis perubahan harga penutupan."""

    def calculate(self, df: pd.DataFrame, period: int = 14) -> float:
        """Hitung nilai RLSI terakhir.

        Args:
            df: DataFrame dengan kolom "close".
            period: Jumlah periode rolling untuk rata-rata gain/loss.

        Returns:
            Nilai RLSI pada bar terakhir dibulatkan 2 desimal.
        """

        delta = df["close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rlsi = 100 - (100 / (1 + rs))
        return round(rlsi.iloc[-1], 2)
