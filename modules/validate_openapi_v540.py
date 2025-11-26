from __future__ import annotations

import argparse
import importlib
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Dict, Iterable, Mapping, MutableMapping, Sequence

# ===============================================
# 🐺 TUYUL FX AGI HYBRID – OpenAPI Validator v5.4.0
# Precision = Survival
# ===============================================

REQUIRED_SECTIONS: tuple[str, ...] = ("openapi", "info", "paths", "components")

GROUP_PREFIXES: Mapping[str, tuple[str, ...]] = {
    "Fusion": ("/fusion", "/hybrid/runFullFusion", "/hybrid/getFusionLayer12"),
    "Reflex": ("/reflex", "/hybrid/runReflexCoherence", "/hybrid/getReflexCoherence"),
    "Risk": ("/risk", "/analytics/getRiskEfficiencyStats", "/analytics/getDrawdownStats"),
    "Vault Sync": ("/vault", "/vault/sync", "/vault/status"),
    "Reflective": ("/reflective", "/analytics/getReflectiveProgress"),
    "GPT Bridge": ("/gpt", "/gpt/bridge"),
    "System": ("/system",),
}


def ensure_yaml_loader() -> ModuleType:
    spec = importlib.util.find_spec("yaml")
    if spec is None:
        raise ImportError("PyYAML is required. Install with `pip install pyyaml`.")
    return importlib.import_module("yaml")


def load_openapi_document(path: Path) -> MutableMapping[str, object]:
    yaml = ensure_yaml_loader()
    with path.open("r", encoding="utf-8") as handle:
        document = yaml.safe_load(handle)
    if not isinstance(document, MutableMapping):
        raise ValueError("OpenAPI document must be a mapping at the root level.")
    return document


def validate_required_sections(document: Mapping[str, object]) -> list[str]:
    return [section for section in REQUIRED_SECTIONS if section not in document]


def extract_paths(document: Mapping[str, object]) -> Dict[str, object]:
    paths = document.get("paths", {})
    if not isinstance(paths, MutableMapping):
        raise ValueError("`paths` must be a mapping of endpoint definitions.")
    return dict(paths)


def categorize_endpoint(path: str) -> str | None:
    for group, prefixes in GROUP_PREFIXES.items():
        if any(path.startswith(prefix) for prefix in prefixes):
            return group
    return None


def group_endpoints(paths: Iterable[str]) -> tuple[Dict[str, int], list[str]]:
    grouped: Dict[str, int] = {group: 0 for group in GROUP_PREFIXES}
    ungrouped: list[str] = []
    for path in paths:
        category = categorize_endpoint(path)
        if category is not None:
            grouped[category] += 1
        else:
            ungrouped.append(path)
    return grouped, ungrouped


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate TUYUL FX AGI v5.4.0 OpenAPI spec.")
    parser.add_argument(
        "--openapi-file",
        type=Path,
        default=Path("modules/openapi_spec_v540.yaml"),
        help="Path to the OpenAPI YAML file.",
    )
    parser.add_argument(
        "--expected-count",
        type=int,
        default=46,
        help="Expected number of endpoints inside `paths`.",
    )

    args = parser.parse_args(argv)
    openapi_path = args.openapi_file

    if not openapi_path.exists():
        print(f"❌ File not found: {openapi_path}")
        return 1

    try:
        document = load_openapi_document(openapi_path)
    except Exception as exc:
        print(f"❌ Failed to load OpenAPI document: {exc}")
        return 1

    missing_sections = validate_required_sections(document)
    if missing_sections:
        print(f"❌ Missing required sections: {', '.join(missing_sections)}")
        return 1

    try:
        paths = extract_paths(document)
    except Exception as exc:
        print(f"❌ Invalid `paths` definition: {exc}")
        return 1

    endpoint_count = len(paths)
    grouped, ungrouped = group_endpoints(paths.keys())
    missing_groups = [group for group, count in grouped.items() if count == 0]

    print("🐺 === TUYUL FX AGI Hybrid OpenAPI Validator v5.4.0 ===")
    print(f"📄 File          : {openapi_path}")
    print(f"🔢 Endpoints     : {endpoint_count} detected")
    print("───────────────────────────────────────────────")

    for group, count in grouped.items():
        status = "✅" if count else "❌"
        print(f"{status} {group:<12} → {count} endpoints")

    if ungrouped:
        print("⚠️  Ungrouped endpoints detected:")
        for path in sorted(ungrouped):
            print(f"   - {path}")

    if missing_groups:
        print(f"❌ Missing endpoint groups: {', '.join(missing_groups)}")

    if endpoint_count != args.expected_count:
        print(
            f"❌ Endpoint count mismatch: expected {args.expected_count}, found {endpoint_count}."
        )
        return 1

    if missing_groups:
        return 1

    print("✅ OpenAPI spec validated successfully — ready for AGI Hybrid pipeline 🧠⚡")
    print("───────────────────────────────────────────────")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
