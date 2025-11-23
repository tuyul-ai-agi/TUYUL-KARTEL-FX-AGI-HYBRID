"""
Fusion Layer - Data Integration & Multi-Source Processing
Handles merging of data from multiple sources, normalization, and feature extraction.
"""

from typing import Dict, List, Any, Optional
import numpy as np
from datetime import datetime

from ..core.logger import logger


class FusionLayer:
    """
    Fusion Layer for integrating and processing data from multiple sources.
    Provides data normalization, feature extraction, and multi-modal integration.
    """
    
    def __init__(self):
        """Initialize Fusion Layer."""
        self.data_sources: Dict[str, Any] = {}
        self.fusion_cache: Dict[str, Any] = {}
        logger.info("Fusion Layer initialized")
    
    async def register_source(self, source_id: str, source_type: str, metadata: Dict[str, Any]) -> bool:
        """
        Register a new data source.
        
        Args:
            source_id: Unique identifier for the source
            source_type: Type of data source (e.g., 'ocr', 'api', 'database')
            metadata: Additional metadata about the source
            
        Returns:
            Success status
        """
        try:
            self.data_sources[source_id] = {
                "type": source_type,
                "metadata": metadata,
                "registered_at": datetime.utcnow().isoformat(),
                "status": "active"
            }
            logger.info(f"Registered data source: {source_id} ({source_type})")
            return True
        except Exception as e:
            logger.error(f"Failed to register source {source_id}: {e}")
            return False
    
    async def fuse_data(self, data_streams: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Fuse multiple data streams into a unified representation.
        
        Args:
            data_streams: List of data streams to fuse
            
        Returns:
            Fused data representation
        """
        try:
            fused_result = {
                "timestamp": datetime.utcnow().isoformat(),
                "sources": [],
                "features": {},
                "confidence": 0.0,
                "data": {}
            }
            
            total_confidence = 0.0
            for stream in data_streams:
                source_id = stream.get("source_id", "unknown")
                confidence = stream.get("confidence", 0.5)
                data = stream.get("data", {})
                
                fused_result["sources"].append(source_id)
                fused_result["data"][source_id] = data
                total_confidence += confidence
                
                # Extract features from each stream
                features = self._extract_features(data, source_id)
                fused_result["features"].update(features)
            
            # Calculate average confidence
            if data_streams:
                fused_result["confidence"] = total_confidence / len(data_streams)
            
            logger.info(f"Fused {len(data_streams)} data streams with confidence {fused_result['confidence']:.2f}")
            return fused_result
            
        except Exception as e:
            logger.error(f"Failed to fuse data: {e}")
            return {"error": str(e), "timestamp": datetime.utcnow().isoformat()}
    
    def _extract_features(self, data: Any, source_id: str) -> Dict[str, Any]:
        """
        Extract features from data.
        
        Args:
            data: Input data
            source_id: Source identifier
            
        Returns:
            Extracted features
        """
        features = {}
        
        if isinstance(data, dict):
            features[f"{source_id}_keys"] = list(data.keys())
            features[f"{source_id}_size"] = len(data)
        elif isinstance(data, (list, tuple)):
            features[f"{source_id}_length"] = len(data)
            if data and isinstance(data[0], (int, float)):
                features[f"{source_id}_mean"] = float(np.mean(data))
                features[f"{source_id}_std"] = float(np.std(data))
        elif isinstance(data, str):
            features[f"{source_id}_text_length"] = len(data)
            features[f"{source_id}_word_count"] = len(data.split())
        
        return features
    
    async def normalize_data(self, data: Any, source_type: str) -> Any:
        """
        Normalize data from different sources to a common format.
        
        Args:
            data: Input data
            source_type: Type of data source
            
        Returns:
            Normalized data
        """
        try:
            if source_type == "ocr":
                return self._normalize_ocr(data)
            elif source_type == "api":
                return self._normalize_api(data)
            elif source_type == "database":
                return self._normalize_database(data)
            else:
                return data
        except Exception as e:
            logger.error(f"Failed to normalize data from {source_type}: {e}")
            return data
    
    def _normalize_ocr(self, data: Any) -> Dict[str, Any]:
        """Normalize OCR data."""
        return {
            "type": "ocr",
            "text": str(data),
            "processed_at": datetime.utcnow().isoformat()
        }
    
    def _normalize_api(self, data: Any) -> Dict[str, Any]:
        """Normalize API data."""
        return {
            "type": "api",
            "payload": data,
            "processed_at": datetime.utcnow().isoformat()
        }
    
    def _normalize_database(self, data: Any) -> Dict[str, Any]:
        """Normalize database data."""
        return {
            "type": "database",
            "records": data,
            "processed_at": datetime.utcnow().isoformat()
        }
    
    async def get_fusion_status(self) -> Dict[str, Any]:
        """Get current status of Fusion Layer."""
        return {
            "active_sources": len(self.data_sources),
            "sources": list(self.data_sources.keys()),
            "cache_size": len(self.fusion_cache),
            "status": "operational"
        }
