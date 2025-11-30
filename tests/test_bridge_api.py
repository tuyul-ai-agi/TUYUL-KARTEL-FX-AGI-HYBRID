from ai_bridge.github_api_bridge import get_repo_data

def test_github_bridge():
    data = get_repo_data(owner="tjx578", repo="TUYUL-KARTEL-FX-AGI-HYBRID")
    assert isinstance(data, dict)
