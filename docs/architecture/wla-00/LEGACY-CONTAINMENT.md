# Legacy Containment Register

Status: `PROPOSED`

Runtime status of listed surfaces: `NOT_MEASURED`

## 1. Rule

All pre-WLA reflective, AGI, vault, auto-learning, auto-heal, auto-push, and
auto-merge artifacts are historical or legacy surfaces. Their presence is not
evidence of WLA conformance. They MUST NOT be imported, scheduled, credentialed,
or described as active learning architecture unless a later stage explicitly
adopts them after review.

WLA terms do not alias legacy terms. In particular:

- a legacy journal row is not a WLA Fact or Episode;
- a reflective feedback score is not an Outcome;
- a reflective cycle is not a deterministic Replay;
- a heuristic update is not a Reflection approval;
- a JSON collection is not a sealed Dataset;
- an adaptive model is not a Challenger; and
- simulated or paper behavior is not WLA SHADOW unless it satisfies ADR-009.

## 2. Static evidence register

| Surface | Static evidence | WLA disposition |
| --- | --- | --- |
| Legacy governance claims the Hybrid repo adjusts weights and may update the FX vault | `docs/Dokumen Tata Kelola Sistem AGI Hibrida TUYUL-KARTEL-FX (Quad Repo).md`, section 3 | Non-authoritative; prohibited write-back model |
| Legacy overview claims meta-learning and repository sync are active/live | `README.md`, sections 2, 5, and 6 | Documentation claim only; operational truth `NOT_MEASURED` |
| Local orchestration, system-overview, fusion, and API documents describe automatic/real-time reflective flows and mutating endpoints | `docs/architecture/BOT_ORCHESTRATOR_FLOW.md`; `docs/TUYUL FX AGI System Overview (v5.8r++).md`; `docs/hybrid_fusion_orchestrator_v540.md`; `docs/API_INDEX.md` | Bannered historical surfaces; WLA standing denied at L1 |
| Config enables automatic meta-learning and cross-repo reflection | `configs/quad_repo_governance_schema.json` | Legacy config; MUST NOT be consumed by WLA |
| Relearning code writes learning parameters in place | `core/reflective/relearning_cycle.py:13` | Direct mutation path; prohibited |
| CLI stages all files, commits, and pushes `main` | `scripts/tuyul_cli_autopush.py:8` | Prohibited autonomous repository mutation |
| Auto-merge hook merges a PR from metric thresholds | `ai_bridge/github_automerge_hook_v6.py:19` | Prohibited self-approval/self-promotion pattern |
| Bootstrap generator rewrites source/runtime hooks | `scripts/reflective_integrate_bootstrap_v6.py` | Prohibited self-modification path |
| Scheduled workflows commit, push, dispatch, and trigger meta-learning | `.github/workflows/` including `trigger_meta_learning.yml`, `reflective_integrity_audit.yml`, and `quad_vault_reflective_sync.yml` | Must be separately inventoried and denied before Gate P0-A |
| Runtime bridge accepts cycle/journal commands and bridge code emits repository dispatch | `core/bridge/reflective_bridge_runtime.py`; `core/reflective/repo_bridge_manager.py` | Prohibited WLA callback/backchannel and repository mutation |
| Compose exposes a Redis command surface without visible authentication in static config | `docker-compose.yaml` | Runtime reachability `NOT_MEASURED`; deny/adopt decision required |
| Legacy modules emit trade-like classes/fields and actionable alerts | `modules/hybrid_balance_controller.py`; `core/twms/twms_trigger_h1.py`; `trq_m15_premove_realtime_v58r_montecarlo.py` | Must never be treated as SHADOW output contracts |
| Legacy adapters replace missing data with defaults, random values, zero, or current time | `core/utils/data_feed_adapter.py`; `core/reflective/reflective_data_bridge.py`; `core/reflective/kartel_reflective_realign.py` | Synthetic/fallback evidence must be typed and isolated; defaulting prohibited |
| Legacy audit/dispatch paths use latest/mtime/last-N views and missing-to-zero values | `.github/workflows/reflective_integrity_audit.yml`; `.github/workflows/meta_reflective_dispatch.yml`; `core/reflective/repo_health_monitor.py` | Not point-in-time-safe; prohibited as WLA eligibility or training input |
| Legacy journal schema co-locates decision inputs and realized outcomes and provides only a generic timestamp | `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/schemas/journal_entry.schema.json` | Not reusable as WLA contract; leakage-prone semantics |
| Legacy Journal bridges send records to an external sync endpoint and overwrite local cache projections with current-time enrichment | `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/agi_sync/journal_bridge.py:108`; `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/agi_sync/agi_bridge.py:25` | Not the append-only, one-way WLA evidence protocol |
| FX Knowledge root describes itself as a “Theoretical Ground Truth Repository” | `TUYUL-FX-KNOWLEDGE-VAULT-AGI/README.md:15` | Legacy theoretical claim; not canonical Alpha or WLA evidence authority |
| FX Knowledge governance declares ground truth, promotion, automated sync/correction, and active status | `TUYUL-FX-KNOWLEDGE-VAULT-AGI/docs/vault_governance.md` | Bannered and covered repository-wide at L1; technical activation remains `NOT_MEASURED` |
| Legacy Journal design declares a “Single Source of Truth” and its README returns feedback for re-learning | `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/docs/QUAD_VAULT_JOURNAL_DESIGN.md:14`; `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/README.md:111` | Conflicting authority/feedback claim; not the future WLA Journal |
| Legacy Journal overview claims retraining, bidirectional sync, automatic workflows, and reflective truth | `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI/docs/JOURNAL_OVERVIEW.md` | Bannered and covered repository-wide at L1; explicitly not reusable as WLA Journal |
| Legacy knowledge documentation describes automatic promotion into heuristics | `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI/README.md` | Prohibited promotion model |
| Kartel Knowledge documents reflective self-modification | `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI/knowledge_base/modern/self_modification_protocol.md`; `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI/docs/SELF_MODIFICATION_GUIDE.md` | Historical only; prohibited as WLA self-promotion or mutation authority |
| Kartel Knowledge architecture declares bidirectional Quad Repo sync and a meta-learning/repository-sync cycle | `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI/docs/SYSTEM_ARCHITECTURE_V573.md` | Bannered and covered repository-wide at L1; technical activation remains `NOT_MEASURED` |

Line references are evidence anchors at the baseline revision, not permanent
identifiers. The owning stage must re-resolve them against its reviewed revision.

## 3. Containment levels

| Level | Meaning | Sufficient for Gate P0-A? |
| --- | --- | --- |
| `L0_DISCOVERED` | Surface is known but unrestricted | No |
| `L1_DECLARED_NON_AUTHORITATIVE` | Documentation explicitly denies WLA standing | No |
| `L2_RUNTIME_DENIED` | Credentials, triggers, imports, and egress are disabled or absent | No |
| `L3_CI_ENFORCED` | Tests and policy prevent reintroduction or activation | Yes |
| `L4_REMOVED_OR_ARCHIVED` | Surface is removed or clearly quarantined as inert history | Yes |

This WLA-00 package reaches `L1_DECLARED_NON_AUTHORITATIVE` only. Gate P0-A
requires `L3_CI_ENFORCED` or `L4_REMOVED_OR_ARCHIVED` for every relevant legacy
surface. A filename containing `read-only`, a failed `git push`, or a comment that
says `sandbox` is not containment evidence.

## 4. Required inventory fields

Before Gate P0-A, every legacy surface MUST have:

- stable inventory ID;
- repository, path, and revision;
- trigger type (import, CLI, HTTP, schedule, dispatch, manual, startup);
- mutation and egress capabilities;
- credentials or permissions it can request;
- WLA disposition (`REMOVE`, `ARCHIVE`, `DENY`, or reviewed `ADOPT`);
- containment evidence and verifier;
- residual risk and owner; and
- last verification time.

No `ADOPT` disposition is valid merely because legacy code already exists.

## 5. Blocker and closure ledger

| Blocker ID | Scope | Accountable owner | Deadline | Status | Closure evidence |
| --- | --- | --- | --- | --- | --- |
| `LEGACY-DISC-001` | Add prominent WLA legacy/non-authoritative banners or equivalent authoritative repository-wide index entries to every conflicting root, governance, architecture, learning, and control-surface document across all four reviewed repositories. Future discoveries remain in scope automatically. | Dwi Kelana Putra as `ARO` and repository owner under `WLA00-EXC-001` | Before WLA-00 `ACCEPTED` | `VALID` | Four repository-wide declarations bind every baseline artifact; 10 Hybrid, 8 FX Knowledge, 8 legacy Journal, and 9 Kartel Knowledge entry points carry direct warnings; cross-repo receipt records exact paths, hashes, and resolved WLA links. `VALID` is evidence quality, not gate `PASS`. |
| `LEGACY-OWNER-001` | Assign a named primary and govern backup availability for every legacy surface class | Dwi Kelana Putra as `ARO` and `SEC` under `WLA00-EXC-001` | Before WLA-00 `ACCEPTED` | `VALID` | Ratification packet records the single owner, unavailable backups, contract-only scope, and non-reusable expiry; closure still depends on verified owner signature |
| `LEGACY-INV-001` | Complete path/trigger/credential/egress/mutation inventory and disposition | `SEC` with `OPS` | Before Gate P0-A evaluation | `OPEN` | Versioned inventory with no unowned item |
| `LEGACY-CONT-001` | Reach L3/L4 for every relevant legacy path | `SEC` with `OPS` | Before Gate P0-A `PASS` | `NOT_EXECUTED` | CI/runtime negative controls and archive/removal receipts |
| `LEGACY-JOURNAL-001` | Prove the legacy Journal is not reused, renamed, or synchronized into the new ledger | `JDS` with `ARO` | Before Gate P0-A `PASS` | `NOT_EXECUTED` | Repository charter, namespace/credential isolation, migration decision |

Each row blocks only the target and deadline named in that row.
`LEGACY-DISC-001` now has valid static discoverability evidence but does not
ratify WLA-00 or prove runtime containment. `LEGACY-OWNER-001` has a bounded
single-owner closure subject to the verified ratification signature.
`LEGACY-INV-001`, `LEGACY-CONT-001`, and
`LEGACY-JOURNAL-001` are downstream P0-A blockers and do not create a WLA-00
ordering deadlock. `OPEN` and `NOT_EXECUTED` never count as a pass for their
named target. A role name without a named person is not closure.
