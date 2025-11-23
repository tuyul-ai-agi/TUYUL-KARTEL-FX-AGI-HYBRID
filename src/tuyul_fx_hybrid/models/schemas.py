"""Pydantic schemas for API requests and responses."""

from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum


class HealthStatus(str, Enum):
    """Health check status."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


class HealthResponse(BaseModel):
    """Health check response."""
    status: HealthStatus
    version: str
    timestamp: str
    components: Dict[str, str]


class DataSourceRequest(BaseModel):
    """Request to register a data source."""
    source_id: str = Field(..., description="Unique source identifier")
    source_type: str = Field(..., description="Type of data source")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class DataStream(BaseModel):
    """Data stream for fusion."""
    source_id: str
    data: Any
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)


class FusionRequest(BaseModel):
    """Request to fuse data streams."""
    data_streams: List[DataStream]


class DecisionRequest(BaseModel):
    """Request for decision making."""
    context: Dict[str, Any]
    options: List[Dict[str, Any]]
    mode: str = Field(default="fast", pattern="^(fast|deliberate)$")


class ReflexRuleRequest(BaseModel):
    """Request to add a reflex rule."""
    name: str
    conditions: Dict[str, Any]
    action: Any
    confidence: float = Field(default=0.8, ge=0.0, le=1.0)


class FeedbackRequest(BaseModel):
    """Feedback on a decision."""
    decision_id: str
    outcome: Dict[str, Any]
    feedback: Dict[str, Any]


class RiskAssessmentRequest(BaseModel):
    """Request for risk assessment."""
    action: Dict[str, Any]
    context: Dict[str, Any]
    category: Optional[str] = None


class MitigationStrategyRequest(BaseModel):
    """Request to add mitigation strategy."""
    risk_category: str
    strategy: Dict[str, Any]


class GPTRequest(BaseModel):
    """Request for GPT generation."""
    prompt: str
    context: Optional[Dict[str, Any]] = None
    system_message: Optional[str] = None


class TextAnalysisRequest(BaseModel):
    """Request for text analysis."""
    text: str
    analysis_type: str = Field(default="sentiment", pattern="^(sentiment|entities|summary|keywords|intent)$")


class SemanticSearchRequest(BaseModel):
    """Request for semantic search."""
    query: str
    documents: List[str]


class LearningExperienceRequest(BaseModel):
    """Request to log learning experience."""
    state: Dict[str, Any]
    action: Dict[str, Any]
    reward: float
    next_state: Optional[Dict[str, Any]] = None


class RewardPredictionRequest(BaseModel):
    """Request for reward prediction."""
    state: Dict[str, Any]
    action: Dict[str, Any]


class ActionSuggestionRequest(BaseModel):
    """Request for action suggestion."""
    state: Dict[str, Any]
    available_actions: List[Dict[str, Any]]


class ReflectionRequest(BaseModel):
    """Request for semantic reflection."""
    decision: Dict[str, Any]
    outcome: Dict[str, Any]
    context: Dict[str, Any]


class InsightsRequest(BaseModel):
    """Request for context-based insights."""
    context: Dict[str, Any]


class OCRImageRequest(BaseModel):
    """Request for OCR parsing (base64 encoded)."""
    image_base64: str
    source_id: str = "api_upload"
    config: Optional[str] = None


class OCRBatchRequest(BaseModel):
    """Request for batch OCR parsing."""
    image_paths: List[str]
    config: Optional[str] = None


class StructuredDataRequest(BaseModel):
    """Request to extract structured data."""
    text: str
    data_type: str = Field(default="general", pattern="^(general|invoice|receipt|document)$")


class KnowledgeSyncRequest(BaseModel):
    """Request to sync knowledge."""
    knowledge_data: Dict[str, Any]
    category: str = "general"


class PatternSyncRequest(BaseModel):
    """Request to sync pattern."""
    pattern_data: Dict[str, Any]
    pattern_type: str = "general"


class InsightSyncRequest(BaseModel):
    """Request to sync insight."""
    insight_data: Dict[str, Any]


class DecisionSyncRequest(BaseModel):
    """Request to sync decision."""
    decision_data: Dict[str, Any]


class ReflectionSyncRequest(BaseModel):
    """Request to sync reflection."""
    reflection_data: Dict[str, Any]


class ActivitySyncRequest(BaseModel):
    """Request to sync activity."""
    activity_data: Dict[str, Any]
    activity_type: str = "general"


class VaultReadRequest(BaseModel):
    """Request to read from vault."""
    file_path: str


class VaultListRequest(BaseModel):
    """Request to list vault files."""
    directory: str = ""


class GenericResponse(BaseModel):
    """Generic API response."""
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class StatusResponse(BaseModel):
    """Status response."""
    status: str
    data: Dict[str, Any]
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
