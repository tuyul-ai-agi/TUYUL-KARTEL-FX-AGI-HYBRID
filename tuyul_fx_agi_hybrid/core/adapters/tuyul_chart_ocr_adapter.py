"""Adapter for converting OCR text into OHLC feed JSON."""

import re
from typing import Dict, List

from .manual_data_loader_v2 import parse_text_to_json


def convert_ocr_to_ohlc(ocr_text: str) -> Dict[str, List[Dict[str, float]]]:
    """Convert OCR chart text into OHLC JSON feed."""

    clean_text = re.sub(r"[^0-9,\.\n]", "", ocr_text)
    parsed = parse_text_to_json(clean_text)
    return parsed
