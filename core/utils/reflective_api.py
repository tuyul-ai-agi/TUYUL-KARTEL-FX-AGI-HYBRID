"""
Reflective Validator API (FastAPI) — TUYUL FX AGI HYBRID v5.7.3r++
Exposes dataset validation endpoints with Prometheus metrics.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

from core.utils.sample_data_validator import SampleDataValidator
from core.utils.schemas import (
    DatasetValidationRequest,
        DatasetValidationResponse,
            DatasetResult,
            )
            
            app = FastAPI(title="TUYUL FX Reflective Validator API", version="5.7.3r++")
            
            VALIDATION_COUNT = Counter(
                "reflective_validation_total", "Total validations executed"
                )
                VALIDATION_LATENCY = Histogram(
                    "reflective_validation_latency_seconds", "Latency per validation"
                    )
                    
                    
                    @app.post(
                        "/reflective/validate-datasets",
                            response_model=DatasetValidationResponse,
                                summary="Validate datasets with reflective metrics",
                                )
                                def validate_datasets(request: DatasetValidationRequest):
                                    VALIDATION_COUNT.inc()
                                        start = datetime.utcnow()
                                            validator = SampleDataValidator(threshold=request.threshold)
                                            
                                                results: List[DatasetResult] = []
                                                    try:
                                                            for pair in request.pairs:
                                                                        result = validator.validate_pair(pair)
                                                                                    results.append(DatasetResult(**result))
                                                                                        except FileNotFoundError as exc:  # surface friendly error
                                                                                                raise HTTPException(status_code=404, detail=str(exc))
                                                                                                    except Exception as exc:  # pragma: no cover - runtime safety
                                                                                                            raise HTTPException(status_code=500, detail=f"Validation failed: {exc}")
                                                                                                            
                                                                                                                latency = (datetime.utcnow() - start).total_seconds()
                                                                                                                    VALIDATION_LATENCY.observe(latency)
                                                                                                                    
                                                                                                                        return DatasetValidationResponse(
                                                                                                                                status="completed",
                                                                                                                                        results=results,
                                                                                                                                                meta={
                                                                                                                                                            "reflective_protocol": "RBP v2.2",
                                                                                                                                                                        "system_version": "5.7.3r++",
                                                                                                                                                                                    "validator": "SampleDataValidator",
                                                                                                                                                                                                "latency_seconds": latency,
                                                                                                                                                                                                            "validation_mode": request.validation_mode,
                                                                                                                                                                                                                    },
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        @app.get("/metrics", summary="Prometheus metrics endpoint")
                                                                                                                                                                                                                        def metrics():
                                                                                                                                                                                                                            return Response(generate_latest(), media_type="text/plain; version=0.0.4")
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
                                                                                                                                                                                                                            @app.get("/health", summary="Liveness probe")
                                                                                                                                                                                                                            def health():
                                                                                                                                                                                                                                return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}
                                                                                                                                                                                                                                """