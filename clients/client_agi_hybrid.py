import os
import httpx

class AgiHybridClient:
    """
    Client dasar AGI HYBRID FX ULTRA WOLF API.
    Default: semua endpoint ke base_url utama.
    Bisa override per-method jika perlu.
    """

    def __init__(self, base_url=None, token=None):
        self.base_url = base_url or "https://api.hybridcore.tuyulkartel.ai/v1"
        self.session = httpx.Client(timeout=30)
        self.token = token or os.getenv("HYBRID_API_TOKEN", "")

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    # ------- FUSION EXAMPLE -------
    def fusion_analyze(self, pair: str, timeframe: str):
        url = f"{self.base_url}/fusion/analyze"
        response = self.session.post(url, headers=self._headers(), json={
            "pair": pair,
            "timeframe": timeframe
        })
        response.raise_for_status()
        return response.json()

    # ------- VAULT SYNC EXAMPLE -------
    def vault_sync(self):
        url = f"{self.base_url}/vault/sync"
        response = self.session.post(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    # ------- GPT BRIDGE -------
    def gpt_bridge(self, payload: dict):
        url = f"{self.base_url}/gpt/bridge"
        response = self.session.post(url, headers=self._headers(), json=payload)
        response.raise_for_status()
        return response.json()

    # ------- OVERRIDE: Trigger GitHub Workflow via GitHub API -------
    def github_trigger_workflow(self, repo_full: str, workflow_id: str, ref: str, inputs=None):
        # This intentionally uses GitHub API rather than AGI Core
        github_token = os.getenv("GITHUB_TOKEN")
        assert github_token, "Set GITHUB_TOKEN in env"

        gh_url = f"https://api.github.com/repos/{repo_full}/actions/workflows/{workflow_id}/dispatches"
        body = {
            "ref": ref
        }
        if inputs:
            body["inputs"] = inputs

        headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github+json"
        }
        resp = self.session.post(gh_url, headers=headers, json=body)
        if resp.status_code != 204:
            raise Exception(f"Failed to trigger: {resp.status_code}, {resp.text}")
        return {"status": "Triggered"}

# --- USAGE ---
if __name__ == "__main__":
    c = AgiHybridClient(token="your-hybrid-api-token")
    print(c.fusion_analyze("EURUSD", "H1"))
    print(c.vault_sync())
    # Example GPT bridge
    payload = {"messages": [{"role": "user", "content": "trend EURUSD H1"}]}
    print(c.gpt_bridge(payload))
    # Example trigger GitHub Actions
    # print(c.github_trigger_workflow("tjx578/TUYUL-KARTEL-FX-AGI-HYBRID", "sync_vault.yml", ref="main"))
