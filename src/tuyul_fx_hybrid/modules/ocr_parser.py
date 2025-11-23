"""
OCR Parser - Offline OCR Feed Parsing
Extracts text from images and documents using Tesseract OCR.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import io

try:
    import pytesseract
    from PIL import Image
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False

from ..core.config import settings
from ..core.logger import logger


class OCRParser:
    """
    OCR Parser for extracting text from images and documents.
    Supports offline processing with Tesseract.
    """
    
    def __init__(self):
        """Initialize OCR Parser."""
        if OCR_AVAILABLE:
            if settings.tesseract_path:
                pytesseract.pytesseract.tesseract_cmd = settings.tesseract_path
            self.lang = settings.ocr_lang
            logger.info(f"OCR Parser initialized with language: {self.lang}")
        else:
            logger.warning("OCR libraries not available. Install pytesseract and Pillow.")
        
        self.parsed_feeds: List[Dict[str, Any]] = []
        self.feed_cache: Dict[str, Any] = {}
    
    async def parse_image(
        self, 
        image_path: str, 
        config: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Parse text from an image file.
        
        Args:
            image_path: Path to image file
            config: Optional Tesseract config string
            
        Returns:
            Parsed text and metadata
        """
        if not OCR_AVAILABLE:
            return {
                "error": "OCR libraries not available",
                "timestamp": datetime.utcnow().isoformat()
            }
        
        try:
            # Open image
            image = Image.open(image_path)
            
            # Perform OCR
            if config:
                text = pytesseract.image_to_string(image, lang=self.lang, config=config)
            else:
                text = pytesseract.image_to_string(image, lang=self.lang)
            
            # Extract additional data
            data = pytesseract.image_to_data(image, lang=self.lang, output_type=pytesseract.Output.DICT)
            
            result = {
                "text": text.strip(),
                "confidence": self._calculate_confidence(data),
                "word_count": len(text.split()),
                "char_count": len(text),
                "source": image_path,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            self.parsed_feeds.append(result)
            
            logger.info(f"Parsed image: {image_path} ({result['word_count']} words)")
            return result
            
        except Exception as e:
            logger.error(f"OCR parsing failed for {image_path}: {e}")
            return {
                "error": str(e),
                "source": image_path,
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def parse_image_bytes(
        self, 
        image_bytes: bytes, 
        source_id: str = "bytes",
        config: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Parse text from image bytes.
        
        Args:
            image_bytes: Image data as bytes
            source_id: Identifier for the image source
            config: Optional Tesseract config string
            
        Returns:
            Parsed text and metadata
        """
        if not OCR_AVAILABLE:
            return {
                "error": "OCR libraries not available",
                "timestamp": datetime.utcnow().isoformat()
            }
        
        try:
            # Open image from bytes
            image = Image.open(io.BytesIO(image_bytes))
            
            # Perform OCR
            if config:
                text = pytesseract.image_to_string(image, lang=self.lang, config=config)
            else:
                text = pytesseract.image_to_string(image, lang=self.lang)
            
            # Extract additional data
            data = pytesseract.image_to_data(image, lang=self.lang, output_type=pytesseract.Output.DICT)
            
            result = {
                "text": text.strip(),
                "confidence": self._calculate_confidence(data),
                "word_count": len(text.split()),
                "char_count": len(text),
                "source": source_id,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            self.parsed_feeds.append(result)
            
            logger.info(f"Parsed image bytes: {source_id} ({result['word_count']} words)")
            return result
            
        except Exception as e:
            logger.error(f"OCR parsing failed for bytes: {e}")
            return {
                "error": str(e),
                "source": source_id,
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def _calculate_confidence(self, ocr_data: Dict[str, Any]) -> float:
        """Calculate average confidence from OCR data."""
        confidences = [
            float(conf) for conf in ocr_data.get('conf', []) 
            if conf != '-1' and conf != -1
        ]
        
        if confidences:
            return sum(confidences) / len(confidences) / 100.0
        return 0.0
    
    async def parse_batch(
        self, 
        image_paths: List[str],
        config: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Parse multiple images in batch.
        
        Args:
            image_paths: List of image file paths
            config: Optional Tesseract config string
            
        Returns:
            List of parsed results
        """
        results = []
        
        for image_path in image_paths:
            result = await self.parse_image(image_path, config)
            results.append(result)
        
        logger.info(f"Batch parsed {len(image_paths)} images")
        return results
    
    async def extract_structured_data(
        self, 
        text: str, 
        data_type: str = "general"
    ) -> Dict[str, Any]:
        """
        Extract structured data from OCR text.
        
        Args:
            text: OCR extracted text
            data_type: Type of data to extract (general, invoice, receipt, etc.)
            
        Returns:
            Structured data
        """
        try:
            structured = {
                "type": data_type,
                "raw_text": text,
                "extracted_data": {},
                "timestamp": datetime.utcnow().isoformat()
            }
            
            if data_type == "invoice":
                structured["extracted_data"] = self._extract_invoice_data(text)
            elif data_type == "receipt":
                structured["extracted_data"] = self._extract_receipt_data(text)
            elif data_type == "document":
                structured["extracted_data"] = self._extract_document_data(text)
            else:
                structured["extracted_data"] = {
                    "text": text,
                    "lines": text.split('\n'),
                    "words": text.split()
                }
            
            return structured
            
        except Exception as e:
            logger.error(f"Structured data extraction failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def _extract_invoice_data(self, text: str) -> Dict[str, Any]:
        """Extract invoice-specific data (simplified)."""
        import re
        
        data = {
            "invoice_number": None,
            "date": None,
            "total": None,
            "vendor": None
        }
        
        # Simple regex patterns (would need refinement for production)
        invoice_pattern = r'invoice[:\s#]+(\w+)'
        date_pattern = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})'
        total_pattern = r'total[:\s]+\$?(\d+\.?\d*)'
        
        invoice_match = re.search(invoice_pattern, text, re.IGNORECASE)
        if invoice_match:
            data["invoice_number"] = invoice_match.group(1)
        
        date_match = re.search(date_pattern, text)
        if date_match:
            data["date"] = date_match.group(1)
        
        total_match = re.search(total_pattern, text, re.IGNORECASE)
        if total_match:
            data["total"] = total_match.group(1)
        
        return data
    
    def _extract_receipt_data(self, text: str) -> Dict[str, Any]:
        """Extract receipt-specific data (simplified)."""
        import re
        
        data = {
            "items": [],
            "total": None,
            "date": None
        }
        
        # Simple patterns
        total_pattern = r'total[:\s]+\$?(\d+\.?\d*)'
        date_pattern = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})'
        
        total_match = re.search(total_pattern, text, re.IGNORECASE)
        if total_match:
            data["total"] = total_match.group(1)
        
        date_match = re.search(date_pattern, text)
        if date_match:
            data["date"] = date_match.group(1)
        
        return data
    
    def _extract_document_data(self, text: str) -> Dict[str, Any]:
        """Extract general document data."""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        return {
            "title": lines[0] if lines else "",
            "lines": lines,
            "paragraph_count": len(text.split('\n\n')),
            "word_count": len(text.split())
        }
    
    async def get_feed_history(
        self, 
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Get recent OCR feed parsing history.
        
        Args:
            limit: Maximum number of results
            
        Returns:
            List of recent parses
        """
        return self.parsed_feeds[-limit:]
    
    async def get_ocr_status(self) -> Dict[str, Any]:
        """Get current status of OCR Parser."""
        return {
            "ocr_available": OCR_AVAILABLE,
            "language": self.lang if OCR_AVAILABLE else None,
            "total_parsed": len(self.parsed_feeds),
            "cache_size": len(self.feed_cache),
            "status": "operational" if OCR_AVAILABLE else "unavailable"
        }
