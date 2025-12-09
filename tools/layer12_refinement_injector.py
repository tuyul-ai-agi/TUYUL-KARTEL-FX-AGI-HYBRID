```python name=tools/layer12_refinement_injector.py
from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional, TypedDict, Literal

import yaml  # type: ignore[import-untyped]


# =========================
# Logging Setup
# =========================

LOGGER = logging.getLogger("layer12_refinement_injector")
LOGGER.setLevel(logging.INFO)

_LOG_HANDLER = logging.StreamHandler()
_LOG_FORMATTER = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [trade_id=%(trade_id)s] %(message)s"
)
_LOG_HANDLER.setFormatter(_LOG_FORMATTER)
LOGGER.addHandler(_LOG_HANDLER)


class LogAdapter(logging.LoggerAdapter):
    """Attach contextual fields to log records."""

    def process(self, msg: str, kwargs: Dict) -> tuple[str, Dict]:
        extra = kwargs.setdefault("extra", {})
        extra.setdefault("trade_id", self.extra.get("trade_id", "-"))
        return msg, kwargs


# =========================
# Domain Exceptions
# =========================

class TradingError(Exception):
    """Base exception for trading-related errors."""


class ConfigLoadError(TradingError):
    """Raised when the bridge configuration cannot be loaded or parsed."""


class SchemaValidationError(TradingError):
    """Raised when the JSON payload does not match the expected schema."""


class JournalWriteError(TradingError):
    """Raised when writing the journal JSON file fails."""


# =========================
# Config Types
# =========================

class JournalFieldsConfig(TypedDict, total=False):
    pair: str
    bias: str
    entry_zone_refined: str
    sl: str
    tp1: str
    tp2: str
    refinement_layer: Dict[str, str]
    fusion_confidence: str
    wlwci: str
    rcadj: str
    monte_carlo_confidence: str
    integrity_index: str
    reflective_sync: str


class JournalSchemaConfig(TypedDict):
    version: str
    path_pattern: str
    fields: JournalFieldsConfig


class RefinementOutputConfig(TypedDict):
    rr_ratio_refined: bool
    fusion_confidence_refined: bool
    reflective_coherence_refined: bool


class RefinementLayerJournalMappingConfig(TypedDict):
    target_repo: str
    schema_version: str
    use_as_single_source_of_truth: bool


class RefinementLayerConfig(TypedDict):
    enabled: bool
    version: str
    components: Dict[str, Dict]
    output: RefinementOutputConfig
    journal_mapping: RefinementLayerJournalMappingConfig


class MonitoringConfig(TypedDict, total=False):
    telemetry_log: str
    reflective_sync_interval: int
    log_level: str
    emit_metrics: bool
    metrics_namespace: str


class BridgeConfig(TypedDict, total=False):
    version: str
    mode: str
    pipeline: list[str]
    refinement_layer: RefinementLayerConfig
    journal_schema: JournalSchemaConfig
    monitoring: MonitoringConfig


# =========================
# Domain Models
# =========================

@dataclass(frozen=True)
class RefinementLayerSnapshot:
    """Refinement layer (8.5) output snapshot."""

    fibonacci_overlap: str
    vwap: float
    delta_cluster: float
    liquidity_type: str
    rr_ratio_refined: str
    fusion_confidence_refined: float
    reflective_coherence_refined: float


@dataclass(frozen=True)
class Layer12Result:
    """Final Layer-12 output envelope used to emit JSON to Journal repo."""

    pair: str
    bias: str
    entry_zone_refined: str
    sl: float
    tp1: float
    tp2: float
    refinement_layer: RefinementLayerSnapshot
    fusion_confidence: float
    wlwci: float
    rcadj: float
    monte_carlo_confidence: float
    integrity_index: float
    reflective_sync: str
    timeframe: str
    as_of: datetime

    @property
    def trade_id(self) -> str:
        """Deterministic trade id based on pair/timeframe/timestamp."""
        ts = self.as_of.strftime("%Y%m%d%H%M%S")
        return f"{self.pair}-{self.timeframe}-{ts}"


# =========================
# Config Loader
# =========================

def load_bridge_config(path: str | Path) -> BridgeConfig:
    """Load AGI Hybrid bridge config from YAML.

    Args:
        path: Path to the YAML configuration file.

    Raises:
        ConfigLoadError: If config file does not exist or parsing fails.

    Returns:
        Parsed bridge configuration as dictionary.
    """
    config_path = Path(path)
    if not config_path.is_file():
        raise ConfigLoadError(f"Bridge config not found at: {config_path}")

    try:
        with config_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as exc:
        raise ConfigLoadError(f"Failed to load bridge config: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigLoadError("Bridge config must be a YAML mapping at root.")

    # We do a shallow type cast; deep validation happens later.
    return data  # type: ignore[return-value]


# =========================
# Schema Validation
# =========================

def _validate_required_field(
    payload: Dict,
    field_name: str,
    expected_type: type,
) -> None:
    if field_name not in payload:
        raise SchemaValidationError(f"Missing required field: {field_name}")
    if not isinstance(payload[field_name], expected_type):
        raise SchemaValidationError(
            f"Field '{field_name}' must be of type {expected_type.__name__}, "
            f"got {type(payload[field_name]).__name__}"
        )


def validate_layer12_result_against_schema(
    result: Layer12Result,
    schema: JournalSchemaConfig,
) -> None:
    """Validate Layer12Result matches the journal schema definition.

    We enforce presence & basic type expectations according to the spec.
    """
    fields = schema.get("fields", {})
    payload = _layer12_result_to_dict(result)

    # Top-level scalar fields
    scalar_field_types: Dict[str, type] = {
        "pair": str,
        "bias": str,
        "entry_zone_refined": str,
        "sl": (int | float),
        "tp1": (int | float),
        "tp2": (int | float),
        "fusion_confidence": (int | float),
        "wlwci": (int | float),
        "rcadj": (int | float),
        "monte_carlo_confidence": (int | float),
        "integrity_index": (int | float),
        "reflective_sync": str,
    }

    for field_name, expected_python_type in scalar_field_types.items():
        if field_name not in fields:
            raise SchemaValidationError(
                f"Schema does not define field '{field_name}' "
                "but Layer12Result provides it."
            )
        _validate_required_field(payload, field_name, expected_python_type)

    # Nested refinement_layer
    refinement_def = fields.get("refinement_layer")
    if not isinstance(refinement_def, dict):
        raise SchemaValidationError(
            "Schema refinement_layer must be a nested mapping."
        )

    if "refinement_layer" not in payload:
        raise SchemaValidationError("Missing 'refinement_layer' in payload.")

    refinement_payload = payload["refinement_layer"]
    if not isinstance(refinement_payload, dict):
        raise SchemaValidationError("'refinement_layer' must be an object.")

    refinement_expected_types: Dict[str, type] = {
        "fibonacci_overlap": str,
        "vwap": (int | float),
        "delta_cluster": (int | float),
        "liquidity_type": str,
        "rr_ratio_refined": str,
        "fusion_confidence_refined": (int | float),
        "reflective_coherence_refined": (int | float),
    }

    for field_name, expected_python_type in refinement_expected_types.items():
        if field_name not in refinement_def:
            raise SchemaValidationError(
                f"Schema.refinement_layer does not define '{field_name}'."
            )
        _validate_required_field(
            refinement_payload, field_name, expected_python_type
        )


# =========================
# Serialization Helpers
# =========================

def _layer12_result_to_dict(result: Layer12Result) -> Dict:
    """Convert Layer12Result to a JSON-ready dict (matching schema)."""
    base = asdict(result)
    # Remove fields not present in schema
    base.pop("timeframe", None)
    base.pop("as_of", None)

    # Convert datetime into ISO8601 if needed for logging, but schema
    # does not explicitly require it, so we keep it internal only.
    return base


def _resolve_journal_path(
    schema: JournalSchemaConfig,
    result: Layer12Result,
    base_dir: str | Path = ".",
) -> Path:
    """Resolve journal JSON output path from schema pattern and result.

    pattern example: "journal/{date}/{pair}-{timeframe}.json"
    """
    pattern = schema["path_pattern"]
    date_str = result.as_of.strftime("%Y-%m-%d")
    variables: Dict[str, str] = {
        "date": date_str,
        "pair": result.pair,
        "timeframe": result.timeframe,
    }
    rel_path = pattern.format(**variables)
    return Path(base_dir).joinpath(rel_path)


# =========================
# Journal Writer
# =========================

def write_journal_entry(
    result: Layer12Result,
    schema: JournalSchemaConfig,
    base_dir: str | Path = ".",
) -> Path:
    """Write Layer12Result as JSON file into Journal repo.

    Args:
        result: Final Layer-12 result.
        schema: Journal schema configuration.
        base_dir: Base directory (root of Hybrid/Journal checked-out tree).

    Raises:
        SchemaValidationError: If result does not match schema.
        JournalWriteError: If writing the JSON file fails.

    Returns:
        Path of the written JSON file.
    """
    validate_layer12_result_against_schema(result, schema)
    payload = _layer12_result_to_dict(result)
    output_path = _resolve_journal_path(schema, result, base_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        raise JournalWriteError(f"Failed to write journal file: {exc}") from exc

    return output_path


# =========================
# High-level Injector API
# =========================

def inject_layer12_to_journal(
    bridge_config_path: str | Path,
    layer12_result: Layer12Result,
    base_dir: str | Path = ".",
) -> Path:
    """High-level entrypoint used by BOT / workflow to emit Journal JSON.

    This function:
    - Loads bridge config
    - Verifies Refinement Layer is enabled
    - Validates Layer12Result against schema
    - Writes JSON to proper path
    - Logs context-aware events

    Args:
        bridge_config_path: Path to `configs/agi_hybrid_bridge.yml`.
        layer12_result: Final Layer-12 result object.
        base_dir: Base directory for output path resolution.

    Returns:
        Path to the written JSON file.
    """
    adapter = LogAdapter(LOGGER, {"trade_id": layer12_result.trade_id})
    adapter.info("Loading bridge configuration...", extra={})

    config = load_bridge_config(bridge_config_path)

    refinement_cfg_raw = config.get("refinement_layer")
    journal_schema_raw = config.get("journal_schema")

    if not isinstance(refinement_cfg_raw, dict):
        raise ConfigLoadError("Missing or invalid 'refinement_layer' config.")
    if not isinstance(journal_schema_raw, dict):
        raise ConfigLoadError("Missing or invalid 'journal_schema' config.")

    refinement_cfg: RefinementLayerConfig = refinement_cfg_raw  # type: ignore[assignment]
    journal_schema: JournalSchemaConfig = journal_schema_raw  # type: ignore[assignment]

    if not refinement_cfg.get("enabled", False):
        raise TradingError(
            "Refinement layer is disabled in configuration. "
            "Journal injection is not allowed."
        )

    adapter.info("Refinement layer enabled. Validating schema...", extra={})

    output_path = write_journal_entry(
        result=layer12_result,
        schema=journal_schema,
        base_dir=base_dir,
    )

    adapter.info(
        "Journal entry written.",
        extra={"journal_path": str(output_path)},
    )

    return output_path


# =========================
# Example CLI Entrypoint
# (Optional, used by GitHub Actions / manual runs)
# =========================

def _parse_bool_env(value: Optional[str], default: bool = False) -> bool:
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "y"}


def main() -> None:
    """CLI entrypoint.

    Designed for:
    - GitHub Actions step (workflow calls `python tools/layer12_refinement_injector.py`)
    - Manual local debugging

    It expects environment variables to provide Layer12Result fields.
    In a real system, these would usually come from an upstream pipeline artifact.
    """
    # NOTE: In production you probably load these from a pipeline artifact,
    # not from environment. This is a pragmatic default for workflows.

    bridge_config_path = os.getenv(
        "AGI_HYBRID_BRIDGE_CONFIG", "configs/agi_hybrid_bridge.yml"
    )
    base_dir = os.getenv("AGI_HYBRID_BASE_DIR", ".")

    # Minimal required fields - upstream pipeline MUST set these correctly.
    try:
        pair = os.environ["L12_PAIR"]
        bias = os.environ["L12_BIAS"]
        entry_zone_refined = os.environ["L12_ENTRY_ZONE_REFINED"]
        timeframe = os.environ["L12_TIMEFRAME"]

        sl = float(os.environ["L12_SL"])
        tp1 = float(os.environ["L12_TP1"])
        tp2 = float(os.environ["L12_TP2"])

        fusion_confidence = float(os.environ["L12_FUSION_CONFIDENCE"])
        wlwci = float(os.environ["L12_WLWCI"])
        rcadj = float(os.environ["L12_RCADJ"])
        monte_carlo_confidence = float(os.environ["L12_MONTE_CARLO_CONFIDENCE"])
        integrity_index = float(os.environ["L12_INTEGRITY_INDEX"])
        reflective_sync = os.environ.get("L12_REFLECTIVE_SYNC", "PENDING")

        # Refinement 8.5 outputs
        fibonacci_overlap = os.environ["L12_REF_FIBONACCI_OVERLAP"]
        vwap = float(os.environ["L12_REF_VWAP"])
        delta_cluster = float(os.environ["L12_REF_DELTA_CLUSTER"])
        liquidity_type = os.environ["L12_REF_LIQUIDITY_TYPE"]
        rr_ratio_refined = os.environ["L12_REF_RR_RATIO_REFINED"]
        fusion_confidence_refined = float(
            os.environ["L12_REF_FUSION_CONFIDENCE_REFINED"]
        )
        reflective_coherence_refined = float(
            os.environ["L12_REF_REFLECTIVE_COHERENCE_REFINED"]
        )

    except KeyError as exc:
        raise TradingError(
            f"Missing required environment variable for Layer12Result: {exc}"
        ) from exc
    except ValueError as exc:
        raise TradingError(
            f"Invalid numeric environment value for Layer12Result: {exc}"
        ) from exc

    as_of = datetime.now(timezone.utc)

    refinement_snapshot = RefinementLayerSnapshot(
        fibonacci_overlap=fibonacci_overlap,
        vwap=vwap,
        delta_cluster=delta_cluster,
        liquidity_type=liquidity_type,
        rr_ratio_refined=rr_ratio_refined,
        fusion_confidence_refined=fusion_confidence_refined,
        reflective_coherence_refined=reflective_coherence_refined,
    )

    result = Layer12Result(
        pair=pair,
        bias=bias,
        entry_zone_refined=entry_zone_refined,
        sl=sl,
        tp1=tp1,
        tp2=tp2,
        refinement_layer=refinement_snapshot,
        fusion_confidence=fusion_confidence,
        wlwci=wlwci,
        rcadj=rcadj,
        monte_carlo_confidence=monte_carlo_confidence,
        integrity_index=integrity_index,
        reflective_sync=reflective_sync,
        timeframe=timeframe,
        as_of=as_of,
    )

    adapter = LogAdapter(LOGGER, {"trade_id": result.trade_id})
    adapter.info("Starting Layer-12 refinement injection.", extra={})

    try:
        output_path = inject_layer12_to_journal(
            bridge_config_path=bridge_config_path,
            layer12_result=result,
            base_dir=base_dir,
        )
    except (ConfigLoadError, SchemaValidationError, JournalWriteError, TradingError) as exc:
        adapter.error(f"Layer-12 injection failed: {exc}", extra={})
        raise SystemExit(1) from exc

    adapter.info(
        f"Layer-12 injection completed successfully: {output_path}", extra={}
    )


if __name__ == "__main__":
    main()
```
