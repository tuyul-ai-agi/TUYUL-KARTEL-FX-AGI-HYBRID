"""
RLSI Module v5.4.0
------------------
Reflex Layer Smart Index — deteksi momentum mikro jangka pendek.
"""

import pandas as pd


@dataclass
class ReflexLiquidityShiftIndex:
    """Compute and interpret the Reflex Liquidity Shift Index.

    Attributes:
        macd_hist: MACD histogram series.
        cci50: Commodity Channel Index (50-period) series.
        mfi: Money Flow Index series.
        equilibrium_zone_width: Width of the equilibrium band used to scale the shift.
    """

    macd_hist: pd.Series
    cci50: pd.Series
    mfi: pd.Series
    equilibrium_zone_width: pd.Series

    def calculate_rlsi(self) -> pd.Series:
        """Calculate normalized RLSI values between -1.0 and +1.0."""

        delta_macd = np.gradient(self.macd_hist)
        distance = np.abs(self.cci50 - self.mfi)
        raw_rlsi = (delta_macd * distance) / (self.equilibrium_zone_width + 1)
        return np.tanh(raw_rlsi)

    @staticmethod
    def interpret_rlsi(rlsi_value: float) -> str:
        """Provide a textual interpretation for an RLSI reading."""

        if rlsi_value > 0.75:
            return "Smart Money Accumulation (BUY Bias)"
        if rlsi_value < -0.75:
            return "Smart Money Distribution (SELL Bias)"
        if abs(rlsi_value) < 0.4:
            return "Equilibrium / Neutral Zone"
        return "Transition Phase"

    def integrate_with_pipeline(self, df: pd.DataFrame) -> pd.DataFrame:
        """Append RLSI metrics and statuses to the provided DataFrame."""

        df = df.copy()
        df["RLSI"] = ReflexLiquidityShiftIndex(
            df["MACD_Hist"], df["CCI50"], df["MFI"], df["EZ_Width"]
        ).calculate_rlsi()

        df["RLSI_Interpretation"] = df["RLSI"].apply(self.interpret_rlsi)
        df["RLSI_Status"] = np.where(
            df["RLSI"] > 0.75,
            "BUY",
            np.where(df["RLSI"] < -0.75, "SELL", "WAIT"),
        )
        return df


def _seed_from_pair_timeframe(pair: str, timeframe: str) -> int:
    """Generate a deterministic seed from the pair and timeframe for reproducibility."""

    return (sum(ord(ch) for ch in f"{pair}-{timeframe}") % 10000) + 1


def generate_rlsi_demo_frame(pair: str, timeframe: str, length: int = 96) -> pd.DataFrame:
    """Create a synthetic market frame used to illustrate RLSI integration."""

    rng = np.random.default_rng(_seed_from_pair_timeframe(pair, timeframe))
    phase = np.linspace(0, np.pi * 2.2, length)

    macd_hist = np.sin(phase) * 0.8 + rng.normal(0, 0.05, length)
    cci50 = 100 + np.cos(phase * 0.5) * 60 + rng.normal(0, 8, length)
    mfi = 85 + np.sin(phase * 0.7) * 50 + rng.normal(0, 7, length)
    equilibrium_width = rng.uniform(1.0, 4.0, length)

    return pd.DataFrame(
        {
            "MACD_Hist": macd_hist,
            "CCI50": cci50,
            "MFI": mfi,
            "EZ_Width": equilibrium_width,
        }
    )


def tuyul_rlsi_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Integrate RLSI metrics into the Tuyul Hybrid pipeline frame."""

    rlsi_engine = ReflexLiquidityShiftIndex(
        df["MACD_Hist"], df["CCI50"], df["MFI"], df["EZ_Width"]
    )
    return rlsi_engine.integrate_with_pipeline(df)


def latest_rlsi_signal(df: pd.DataFrame) -> Tuple[float, str, str]:
    """Return the latest RLSI value, interpretation, and status."""

    latest_row = df.iloc[-1]
    latest_value = float(latest_row["RLSI"])
    interpretation = str(latest_row["RLSI_Interpretation"])
    status = str(latest_row["RLSI_Status"])
    return latest_value, interpretation, status


class RLSIModule:
    """RLSI helper with simple RSI-style calculation for reflex layer."""

    def calculate(self, df: pd.DataFrame) -> float:
        closes = df.get("close")
        if closes is None or len(closes) < 2:
            return 50.0

        delta = closes.diff().dropna()
        up = delta.clip(lower=0).rolling(window=14, min_periods=1).mean()
        down = (-delta.clip(upper=0)).rolling(window=14, min_periods=1).mean()
        rs = up / (down.replace(0, np.nan)).fillna(0.0001)
        rsi = 100 - (100 / (1 + rs))
        return float(rsi.iloc[-1])
class RLSIModule:
    def calculate(self, df: pd.DataFrame, period: int = 14):
        delta = df["close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rlsi = 100 - (100 / (1 + rs))
        return round(rlsi.iloc[-1], 2)
