import pandas as pd
import numpy as np

class VDDFE:
    """
    VDD Feature Extraction Engine
    """
    def __init__(self, lookback_z=21, lookback_corr=90):
        self.lookback_z = lookback_z
        self.lookback_corr = lookback_corr

    def zscore(self, series: pd.Series):
        return (series - series.rolling(self.lookback_z).mean()) / series.rolling(self.lookback_z).std()

    def build_features(self, vix: pd.DataFrame, dxy: pd.DataFrame, vix3m: pd.DataFrame):
        df = pd.DataFrame(index=vix['datetime'])
        df['VIX'] = vix['close'].astype(float)
        df['DXY'] = dxy['close'].astype(float)
        df['VIX3M'] = vix3m['close'].astype(float)

        df['VIX_Z1M'] = self.zscore(df['VIX'])
        df['DXY_Z1M'] = self.zscore(df['DXY'])
        df['VIX_DXY_CORR'] = df['VIX'].rolling(self.lookback_corr).corr(df['DXY'])
        df['VIX_TERM'] = df['VIX'] / df['VIX3M']

        return df.dropna()
