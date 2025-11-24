"""Runner for executing a full hybrid analysis cycle via GPTBridgeHandler."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CORE_PATH = PROJECT_ROOT / "core"
if str(CORE_PATH) not in sys.path:
    sys.path.insert(0, str(CORE_PATH))

from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler


def main() -> None:
    """Initialize the bridge and execute a sample analysis run."""
    bridge = GPTBridgeHandler()
    print("TUYUL AGI Hybrid Bridge Initialized")
    print("Status:", bridge.get_status())

    result = bridge.run_analysis("XAU/USD", "H1")
    print("\n=== HYBRID ANALYSIS RESULT ===")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
