"""
Chart OCR Adapter
-----------------
Membaca pola grafik dari gambar chart dan mengubah ke data angka.
"""

import pytesseract
from PIL import Image


class ChartOCRAdapter:
    def __init__(self, tesseract_path=None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def extract_text(self, image_path: str) -> str:
        """Membaca teks dari chart (harga, timeframe, label)"""
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()

    def detect_pattern(self, image_path: str) -> str:
        """Deteksi pola seperti head-shoulder, triangle, dll (mock)"""
        text = self.extract_text(image_path)
        if "triangle" in text.lower():
            return "Symmetrical Triangle"
        elif "double" in text.lower():
            return "Double Top/Bottom"
        return "Unknown Pattern"
