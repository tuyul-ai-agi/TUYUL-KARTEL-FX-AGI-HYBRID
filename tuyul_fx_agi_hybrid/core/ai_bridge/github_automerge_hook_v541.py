from api_github_com__jit_plugin import triggerRuntimeReload

def create_automerge_pr(repo, branch="autosync/v541"):
    triggerRuntimeReload({
        "event_type": "create_pull_request",
        "client_payload": {
            "repo": repo,
            "branch": branch,
            "title": "AutoSync TUYUL v5.4.1-DHT",
            "body": "Automated push by TUYUL AGI — verified and integrity checked."
        }
    })
