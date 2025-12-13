"""
VDDHybrid Modules v5.4.0 (archived)
------------------------
Menyatukan semua submodul VDD Hybrid menjadi satu sistem.
"""

from modules.vdd_hybrid.vdd_data_stream import VDDDataStream
from modules.vdd_hybrid.vdd_feature_engine import VDDFeatureEngine
from modules.vdd_hybrid.vdd_regime_model import VDDRegimeModel
from modules.vdd_hybrid.vdd_signal_broadcat import VDDSignalBroadcaster


class VDDHybridModules:
    def __init__(self):
        self.stream = VDDDataStream()
        self.engine = VDDFeatureEngine()
        self.model = VDDRegimeModel()
        self.broadcaster = VDDSignalBroadcaster()

    def run(self, vault_path: str):
        df = self.stream.load_from_vault(vault_path)
        df = self.stream.preprocess(df)
        features = self.engine.extract_features(df)
        state = self.model.classify(features)
        self.broadcaster.broadcast(state)
        return {"features": features, "state": state}