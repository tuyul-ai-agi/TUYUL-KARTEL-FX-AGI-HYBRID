"""
TUYUL-FX-HYBRID v5.4.0 AGI Orchestrator Main Application
FastAPI application with 46 OpenAPI endpoints
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict, Any
import base64

from .core.config import settings
from .core.logger import logger
from .layers import FusionLayer, ReflexLayer, RiskLayer
from .modules import (
    GPTBridge, 
    AdaptiveLearning, 
    SemanticReflection, 
    OCRParser,
    KnowledgeVaultSync,
    JournalVaultSync
)
from .models.schemas import *

# Initialize FastAPI app
app = FastAPI(
    title="TUYUL-FX-HYBRID AGI Orchestrator",
    description="AGI orchestrator with Fusion, Reflex, and Risk layers",
    version=settings.api_version,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
fusion_layer = FusionLayer()
reflex_layer = ReflexLayer()
risk_layer = RiskLayer()
gpt_bridge = GPTBridge()
adaptive_learning = AdaptiveLearning()
semantic_reflection = SemanticReflection()
ocr_parser = OCRParser()
knowledge_vault = KnowledgeVaultSync()
journal_vault = JournalVaultSync()

logger.info("TUYUL-FX-HYBRID v5.4.0 AGI Orchestrator initialized")


# ============================================================================
# Health & System Endpoints (5)
# ============================================================================

@app.get("/", response_model=GenericResponse)
async def root():
    """Root endpoint."""
    return GenericResponse(
        success=True,
        data={
            "name": "TUYUL-FX-HYBRID AGI Orchestrator",
            "version": settings.api_version,
            "status": "operational"
        }
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status=HealthStatus.HEALTHY,
        version=settings.api_version,
        timestamp=datetime.utcnow().isoformat(),
        components={
            "fusion_layer": "operational",
            "reflex_layer": "operational",
            "risk_layer": "operational",
            "gpt_bridge": "operational",
            "adaptive_learning": "operational",
            "semantic_reflection": "operational",
            "ocr_parser": "operational"
        }
    )


@app.get("/status", response_model=StatusResponse)
async def system_status():
    """Get comprehensive system status."""
    return StatusResponse(
        status="operational",
        data={
            "fusion": await fusion_layer.get_fusion_status(),
            "reflex": await reflex_layer.get_reflex_status(),
            "risk": await risk_layer.get_risk_status(),
            "gpt": await gpt_bridge.get_status(),
            "learning": await adaptive_learning.get_learning_status(),
            "reflection": await semantic_reflection.get_reflection_status(),
            "ocr": await ocr_parser.get_ocr_status(),
            "knowledge_vault": await knowledge_vault.get_sync_status(),
            "journal_vault": await journal_vault.get_sync_status()
        }
    )


@app.get("/version")
async def get_version():
    """Get API version."""
    return {"version": settings.api_version, "name": "TUYUL-FX-HYBRID"}


@app.get("/config")
async def get_config():
    """Get public configuration (non-sensitive)."""
    return {
        "api_version": settings.api_version,
        "gpt_model": settings.gpt_model,
        "learning_rate": settings.learning_rate,
        "batch_size": settings.batch_size
    }


# ============================================================================
# Fusion Layer Endpoints (5)
# ============================================================================

@app.post("/fusion/register-source", response_model=GenericResponse)
async def register_data_source(request: DataSourceRequest):
    """Register a new data source."""
    success = await fusion_layer.register_source(
        request.source_id,
        request.source_type,
        request.metadata
    )
    return GenericResponse(success=success, data={"source_id": request.source_id})


@app.post("/fusion/fuse", response_model=GenericResponse)
async def fuse_data(request: FusionRequest):
    """Fuse multiple data streams."""
    data_streams = [stream.dict() for stream in request.data_streams]
    result = await fusion_layer.fuse_data(data_streams)
    return GenericResponse(success=True, data=result)


@app.post("/fusion/normalize")
async def normalize_data(source_type: str, data: Any):
    """Normalize data from a specific source type."""
    result = await fusion_layer.normalize_data(data, source_type)
    return GenericResponse(success=True, data=result)


@app.get("/fusion/status", response_model=StatusResponse)
async def get_fusion_status():
    """Get Fusion Layer status."""
    status_data = await fusion_layer.get_fusion_status()
    return StatusResponse(status="operational", data=status_data)


@app.get("/fusion/sources")
async def list_data_sources():
    """List all registered data sources."""
    return GenericResponse(
        success=True,
        data={"sources": list(fusion_layer.data_sources.keys())}
    )


# ============================================================================
# Reflex Layer Endpoints (7)
# ============================================================================

@app.post("/reflex/decide", response_model=GenericResponse)
async def make_decision(request: DecisionRequest):
    """Make a decision based on context."""
    result = await reflex_layer.make_decision(
        request.context,
        request.options,
        request.mode
    )
    return GenericResponse(success=True, data=result)


@app.post("/reflex/add-rule", response_model=GenericResponse)
async def add_reflex_rule(request: ReflexRuleRequest):
    """Add a new reflex rule."""
    success = await reflex_layer.add_reflex_rule(
        request.name,
        request.conditions,
        request.action,
        request.confidence
    )
    return GenericResponse(success=success, data={"rule_name": request.name})


@app.post("/reflex/feedback", response_model=GenericResponse)
async def submit_feedback(request: FeedbackRequest):
    """Submit feedback on a decision."""
    success = await reflex_layer.learn_from_feedback(
        request.decision_id,
        request.outcome,
        request.feedback
    )
    return GenericResponse(success=success, data={"decision_id": request.decision_id})


@app.get("/reflex/status", response_model=StatusResponse)
async def get_reflex_status():
    """Get Reflex Layer status."""
    status_data = await reflex_layer.get_reflex_status()
    return StatusResponse(status="operational", data=status_data)


@app.get("/reflex/rules")
async def list_reflex_rules():
    """List all reflex rules."""
    return GenericResponse(
        success=True,
        data={"rules": reflex_layer.reflex_rules}
    )


@app.get("/reflex/patterns")
async def list_learning_patterns():
    """List learned patterns."""
    return GenericResponse(
        success=True,
        data={"patterns": reflex_layer.learning_patterns}
    )


@app.get("/reflex/history")
async def get_decision_history(limit: int = 10):
    """Get recent decision history."""
    return GenericResponse(
        success=True,
        data={"history": reflex_layer.decision_history[-limit:]}
    )


# ============================================================================
# Risk Layer Endpoints (6)
# ============================================================================

@app.post("/risk/assess", response_model=GenericResponse)
async def assess_risk(request: RiskAssessmentRequest):
    """Assess risk for an action."""
    result = await risk_layer.assess_risk(
        request.action,
        request.context,
        request.category
    )
    return GenericResponse(success=True, data=result)


@app.post("/risk/mitigation", response_model=GenericResponse)
async def add_mitigation_strategy(request: MitigationStrategyRequest):
    """Add a mitigation strategy."""
    from .layers.risk import RiskCategory
    category = RiskCategory(request.risk_category)
    success = await risk_layer.add_mitigation_strategy(category, request.strategy)
    return GenericResponse(success=success, data={"category": request.risk_category})


@app.get("/risk/profile", response_model=GenericResponse)
async def get_risk_profile():
    """Get overall risk profile."""
    profile = await risk_layer.get_risk_profile()
    return GenericResponse(success=True, data=profile)


@app.get("/risk/status", response_model=StatusResponse)
async def get_risk_status():
    """Get Risk Layer status."""
    status_data = await risk_layer.get_risk_status()
    return StatusResponse(status="operational", data=status_data)


@app.get("/risk/assessments")
async def list_risk_assessments(limit: int = 10):
    """List recent risk assessments."""
    return GenericResponse(
        success=True,
        data={"assessments": risk_layer.risk_assessments[-limit:]}
    )


@app.get("/risk/strategies")
async def list_mitigation_strategies():
    """List mitigation strategies."""
    return GenericResponse(
        success=True,
        data={"strategies": risk_layer.mitigation_strategies}
    )


# ============================================================================
# GPT Bridge Endpoints (6)
# ============================================================================

@app.post("/gpt/generate", response_model=GenericResponse)
async def generate_gpt_response(request: GPTRequest):
    """Generate response using GPT."""
    result = await gpt_bridge.generate_response(
        request.prompt,
        request.context,
        request.system_message
    )
    return GenericResponse(success=result.get("response") is not None, data=result)


@app.post("/gpt/analyze", response_model=GenericResponse)
async def analyze_text(request: TextAnalysisRequest):
    """Analyze text using GPT."""
    result = await gpt_bridge.analyze_text(request.text, request.analysis_type)
    return GenericResponse(success=True, data=result)


@app.post("/gpt/search", response_model=GenericResponse)
async def semantic_search(request: SemanticSearchRequest):
    """Perform semantic search."""
    result = await gpt_bridge.semantic_search(request.query, request.documents)
    return GenericResponse(success=True, data={"results": result})


@app.post("/gpt/insights", response_model=GenericResponse)
async def generate_insights(data: Dict[str, Any]):
    """Generate insights from data."""
    result = await gpt_bridge.generate_insights(data)
    return GenericResponse(success=True, data=result)


@app.post("/gpt/clear-history")
async def clear_conversation_history():
    """Clear GPT conversation history."""
    gpt_bridge.clear_history()
    return GenericResponse(success=True, data={"message": "History cleared"})


@app.get("/gpt/status", response_model=StatusResponse)
async def get_gpt_status():
    """Get GPT Bridge status."""
    status_data = await gpt_bridge.get_status()
    return StatusResponse(status="operational", data=status_data)


# ============================================================================
# Adaptive Learning Endpoints (5)
# ============================================================================

@app.post("/learning/experience", response_model=GenericResponse)
async def log_learning_experience(request: LearningExperienceRequest):
    """Log a learning experience."""
    success = await adaptive_learning.learn_from_experience(
        request.state,
        request.action,
        request.reward,
        request.next_state
    )
    return GenericResponse(success=success, data={"message": "Experience logged"})


@app.post("/learning/predict-reward", response_model=GenericResponse)
async def predict_reward(request: RewardPredictionRequest):
    """Predict reward for state-action pair."""
    reward, confidence = await adaptive_learning.predict_reward(
        request.state,
        request.action
    )
    return GenericResponse(
        success=True,
        data={"expected_reward": reward, "confidence": confidence}
    )


@app.post("/learning/suggest-action", response_model=GenericResponse)
async def suggest_action(request: ActionSuggestionRequest):
    """Suggest best action for a state."""
    action = await adaptive_learning.suggest_action(
        request.state,
        request.available_actions
    )
    return GenericResponse(success=action is not None, data={"suggested_action": action})


@app.get("/learning/performance", response_model=GenericResponse)
async def get_performance_trend():
    """Get performance trend analysis."""
    trend = await adaptive_learning.get_performance_trend()
    return GenericResponse(success=True, data=trend)


@app.get("/learning/status", response_model=StatusResponse)
async def get_learning_status():
    """Get Adaptive Learning status."""
    status_data = await adaptive_learning.get_learning_status()
    return StatusResponse(status="operational", data=status_data)


# ============================================================================
# Semantic Reflection Endpoints (5)
# ============================================================================

@app.post("/reflection/reflect", response_model=GenericResponse)
async def reflect_on_decision(request: ReflectionRequest):
    """Reflect on a past decision."""
    result = await semantic_reflection.reflect_on_decision(
        request.decision,
        request.outcome,
        request.context
    )
    return GenericResponse(success=True, data=result)


@app.post("/reflection/insights", response_model=GenericResponse)
async def get_contextual_insights(request: InsightsRequest):
    """Get insights for a context."""
    insights = await semantic_reflection.get_insights_for_context(request.context)
    return GenericResponse(success=True, data={"insights": insights})


@app.get("/reflection/effectiveness", response_model=GenericResponse)
async def analyze_reasoning_effectiveness():
    """Analyze reasoning effectiveness."""
    analysis = await semantic_reflection.analyze_reasoning_effectiveness()
    return GenericResponse(success=True, data=analysis)


@app.get("/reflection/report", response_model=GenericResponse)
async def generate_reflection_report():
    """Generate reflection report."""
    report = await semantic_reflection.generate_reflection_report()
    return GenericResponse(success=True, data=report)


@app.get("/reflection/status", response_model=StatusResponse)
async def get_reflection_status():
    """Get Semantic Reflection status."""
    status_data = await semantic_reflection.get_reflection_status()
    return StatusResponse(status="operational", data=status_data)


# ============================================================================
# OCR Parser Endpoints (5)
# ============================================================================

@app.post("/ocr/parse-image", response_model=GenericResponse)
async def parse_ocr_image(request: OCRImageRequest):
    """Parse text from base64 encoded image."""
    try:
        image_bytes = base64.b64decode(request.image_base64)
        result = await ocr_parser.parse_image_bytes(
            image_bytes,
            request.source_id,
            request.config
        )
        return GenericResponse(success="error" not in result, data=result)
    except Exception as e:
        return GenericResponse(success=False, error=str(e))


@app.post("/ocr/parse-batch", response_model=GenericResponse)
async def parse_ocr_batch(request: OCRBatchRequest):
    """Parse multiple images in batch."""
    results = await ocr_parser.parse_batch(request.image_paths, request.config)
    return GenericResponse(success=True, data={"results": results})


@app.post("/ocr/extract-structured", response_model=GenericResponse)
async def extract_structured_data(request: StructuredDataRequest):
    """Extract structured data from OCR text."""
    result = await ocr_parser.extract_structured_data(request.text, request.data_type)
    return GenericResponse(success=True, data=result)


@app.get("/ocr/history")
async def get_ocr_history(limit: int = 10):
    """Get OCR parsing history."""
    history = await ocr_parser.get_feed_history(limit)
    return GenericResponse(success=True, data={"history": history})


@app.get("/ocr/status", response_model=StatusResponse)
async def get_ocr_status():
    """Get OCR Parser status."""
    status_data = await ocr_parser.get_ocr_status()
    return StatusResponse(status="operational", data=status_data)


# ============================================================================
# Knowledge Vault Sync Endpoints (7)
# ============================================================================

@app.post("/vault/knowledge/sync", response_model=GenericResponse)
async def sync_knowledge(request: KnowledgeSyncRequest):
    """Sync knowledge to vault."""
    result = await knowledge_vault.sync_knowledge(
        request.knowledge_data,
        request.category
    )
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/knowledge/pattern", response_model=GenericResponse)
async def sync_pattern(request: PatternSyncRequest):
    """Sync pattern to vault."""
    result = await knowledge_vault.sync_pattern(
        request.pattern_data,
        request.pattern_type
    )
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/knowledge/insight", response_model=GenericResponse)
async def sync_insight(request: InsightSyncRequest):
    """Sync insight to vault."""
    result = await knowledge_vault.sync_insight(request.insight_data)
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/knowledge/read", response_model=GenericResponse)
async def read_knowledge(request: VaultReadRequest):
    """Read from Knowledge Vault."""
    data = await knowledge_vault.read_data(request.file_path)
    return GenericResponse(success="error" not in data, data=data)


@app.post("/vault/knowledge/list", response_model=GenericResponse)
async def list_knowledge_files(request: VaultListRequest):
    """List Knowledge Vault files."""
    files = await knowledge_vault.list_files(request.directory)
    return GenericResponse(success=True, data={"files": files})


@app.get("/vault/knowledge/status", response_model=StatusResponse)
async def get_knowledge_vault_status():
    """Get Knowledge Vault status."""
    status_data = await knowledge_vault.get_sync_status()
    return StatusResponse(status="operational", data=status_data)


@app.get("/vault/knowledge/history")
async def get_knowledge_sync_history(limit: int = 10):
    """Get Knowledge Vault sync history."""
    return GenericResponse(
        success=True,
        data={"history": knowledge_vault.sync_history[-limit:]}
    )


# ============================================================================
# Journal Vault Sync Endpoints (6)
# ============================================================================

@app.post("/vault/journal/decision", response_model=GenericResponse)
async def sync_decision(request: DecisionSyncRequest):
    """Sync decision to journal."""
    result = await journal_vault.sync_decision(request.decision_data)
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/journal/reflection", response_model=GenericResponse)
async def sync_reflection(request: ReflectionSyncRequest):
    """Sync reflection to journal."""
    result = await journal_vault.sync_reflection(request.reflection_data)
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/journal/activity", response_model=GenericResponse)
async def sync_activity(request: ActivitySyncRequest):
    """Sync activity to journal."""
    result = await journal_vault.sync_activity(
        request.activity_data,
        request.activity_type
    )
    return GenericResponse(success=result.get("success", False), data=result)


@app.post("/vault/journal/read", response_model=GenericResponse)
async def read_journal(request: VaultReadRequest):
    """Read from Journal Vault."""
    data = await journal_vault.read_data(request.file_path)
    return GenericResponse(success="error" not in data, data=data)


@app.post("/vault/journal/list", response_model=GenericResponse)
async def list_journal_files(request: VaultListRequest):
    """List Journal Vault files."""
    files = await journal_vault.list_files(request.directory)
    return GenericResponse(success=True, data={"files": files})


@app.get("/vault/journal/status", response_model=StatusResponse)
async def get_journal_vault_status():
    """Get Journal Vault status."""
    status_data = await journal_vault.get_sync_status()
    return StatusResponse(status="operational", data=status_data)


# Exception handlers
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    """Handle generic exceptions."""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": str(exc), "type": type(exc).__name__}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        log_level=settings.log_level.lower()
    )
