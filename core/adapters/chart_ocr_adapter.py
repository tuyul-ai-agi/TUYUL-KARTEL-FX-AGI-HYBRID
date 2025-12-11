# Chart OCR Reflective Adapter — v5.7.3r++
# Konversi chart image → dataset reflektif terstruktur
import cv2
import numpy as np
from pytesseract import image_to_string
import json, datetime

class ChartOCRReflectiveAdapter:
    def __init__(self):
        self.integrity_index = 0.0
        self.last_reflection = None

    def process_chart(self, image_path):
        """Ekstraksi data chart dengan validasi reflektif"""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = image_to_string(gray)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        price_data = self._parse_prices(text)
        integrity = self._calculate_integrity(price_data)

        reflective_context = {
            "timestamp": now,
            "integrity_index": integrity,
            "data_points": len(price_data),
            "reflection_state": "stable" if integrity > 0.9 else "adaptive"
        }

        self.last_reflection = reflective_context
        print(f"🧠 OCR Reflective Integrity: {integrity}")
        return reflective_context

    def _parse_prices(self, text):
        lines = [l for l in text.split("\n") if l.strip()]
        prices = [float(x) for x in lines if x.replace(".", "", 1).isdigit()]
        return prices or [1.0]

    def _calculate_integrity(self, prices):
        if not prices: return 0.0
        mean = np.mean(prices)
        deviation = np.std(prices) / mean
        return round(1 - deviation, 3)
