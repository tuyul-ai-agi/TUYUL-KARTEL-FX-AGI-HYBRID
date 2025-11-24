#!/usr/bin/env python3
"""Auto-generate documentation from code modules.

Scans core modules and generates markdown documentation with function signatures,
docstrings, and module descriptions.
"""

from __future__ import annotations

import ast
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


def extract_docstring(node: Any) -> str:
    """Extract docstring from an AST node."""
    return ast.get_docstring(node) or "No description available."


def extract_functions(module_path: Path) -> List[Dict[str, Any]]:
    """Extract function definitions from a Python module.
    
    Args:
        module_path: Path to the Python module file.
        
    Returns:
        List of dictionaries containing function information.
    """
    try:
        with module_path.open("r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except Exception as e:
        print(f"⚠️ Error parsing {module_path}: {e}")
        return []
    
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Get function signature
            args = [arg.arg for arg in node.args.args]
            signature = f"{node.name}({', '.join(args)})"
            
            functions.append({
                "name": node.name,
                "signature": signature,
                "docstring": extract_docstring(node),
            })
    
    return functions


def generate_module_docs(module_path: Path, output_dir: Path) -> None:
    """Generate documentation for a single module.
    
    Args:
        module_path: Path to the Python module.
        output_dir: Directory where documentation will be saved.
    """
    module_name = module_path.stem
    functions = extract_functions(module_path)
    
    if not functions:
        return
    
    # Create markdown content
    md_content = [
        f"# {module_name.replace('_', ' ').title()}",
        "",
        f"**Module:** `{module_path.relative_to(module_path.parents[2])}`",
        "",
        "## Functions",
        "",
    ]
    
    for func in functions:
        md_content.extend([
            f"### `{func['signature']}`",
            "",
            func['docstring'],
            "",
        ])
    
    # Add timestamp
    md_content.extend([
        "---",
        f"*Generated: {datetime.now(tz=timezone.utc).isoformat()}*",
    ])
    
    # Write to file
    output_file = output_dir / f"{module_name}.md"
    output_file.write_text("\n".join(md_content), encoding="utf-8")
    print(f"✅ Generated: {output_file.name}")


def main() -> None:
    """Main entry point for documentation generation."""
    print("📚 Generating documentation...")
    
    # Set up paths
    base_path = Path(__file__).resolve().parents[1]
    core_path = base_path / "core"
    docs_path = base_path / "docs"
    
    if not core_path.exists():
        print(f"❌ Core directory not found: {core_path}")
        sys.exit(1)
    
    # Create docs directory
    docs_path.mkdir(parents=True, exist_ok=True)
    
    # Find all Python modules in core
    python_files = list(core_path.rglob("*.py"))
    python_files = [f for f in python_files if not f.name.startswith("__")]
    
    print(f"📁 Found {len(python_files)} Python modules")
    
    # Generate documentation for each module
    generated_count = 0
    for py_file in python_files:
        try:
            generate_module_docs(py_file, docs_path)
            generated_count += 1
        except Exception as e:
            print(f"⚠️ Failed to generate docs for {py_file.name}: {e}")
    
    # Create index
    index_content = [
        "# TUYUL FX AGI Hybrid - API Documentation",
        "",
        f"**Last Updated:** {datetime.now(tz=timezone.utc).isoformat()}",
        "",
        "## Modules",
        "",
    ]
    
    for py_file in sorted(python_files):
        relative_path = py_file.relative_to(core_path)
        module_name = py_file.stem
        index_content.append(f"- [{module_name}]({module_name}.md)")
    
    index_file = docs_path / "API_INDEX.md"
    index_file.write_text("\n".join(index_content), encoding="utf-8")
    
    print(f"✅ Documentation generation complete: {generated_count} modules documented")
    print(f"📄 Index created: {index_file.name}")


if __name__ == "__main__":
    main()
