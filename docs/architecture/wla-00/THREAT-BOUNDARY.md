# WLA-00 Threat Boundary

Status: `PROPOSED`

Scope: the proposed Wolf15 learning plane from source export through SHADOW

Evidence type: repository-scoped design and static source review; runtime controls
are `NOT_MEASURED`

## Overview

The WLA learning plane consumes observational evidence derived from WOLF15 and
turns it into append-only Facts, Episodes, Outcomes, Replays, Reflections,
Datasets, Challengers, and SHADOW evaluations. It is not an execution plane.

The highest-consequence security objective is to ensure that compromise,
poisoning, error, or authority creep in learning cannot mutate WOLF15, fabricate
canonical Alpha, weaken governance/risk, or reach a broker/EA. The next objective
is evidentiary integrity: a reviewer must be able to determine exactly what was
known when, how a label was formed, and which artifacts produced a result.

Static evidence shows legacy code and workflows with parameter writes, remote
dispatch, commits/pushes, and metric-driven merge behavior. Those surfaces are
not WLA controls and remain non-authoritative until contained under the legacy
register. Their operational state was not tested here.

## Threat Model, Trust Boundaries, and Assumptions

### Assets and privileges that matter

1. WOLF15 canonical Alpha identity, payload, ordering, and authority provenance.
2. WOLF15 configuration, database, outbox, risk, verdict, and execution surfaces.
3. Broker/EA/order credentials and network paths, which WLA must never possess.
4. Journal evidence, stream integrity roots, corrections, and retention receipts.
5. Temporal availability, outcome maturity, and point-in-time lineage.
6. Replay, Dataset, Challenger, and SHADOW manifests and artifact digests.
7. Human gate identities, decisions, evidence bindings, and separation of duties.
8. CI, repository, artifact-registry, deployment, and cloud credentials.
9. Confidential data, secrets, licensed feeds, and potentially sensitive operator
   annotations.

### Actors

| Actor | Trust position | Allowed capability |
| --- | --- | --- |
| WOLF15 source/export adapter | Trusted producer within its pinned source contract | Emit observational export atomically with source fact |
| External market/news/broker providers | Untrusted or partially trusted upstream data | Supply data to WOLF15; no WLA authority |
| Journal ingress and steward | Trusted learning evidence boundary | Validate, quarantine, append, correct via source-owned events |
| Orchestrator/replay/dataset services | Trusted for bounded derived work | Read eligible evidence and write learning-owned artifacts |
| Reflection/model code | Untrusted-to-semi-trusted computation | Produce hypotheses or Challenger artifacts in sandbox |
| SHADOW session controller | High-trust but narrowly bounded learning control component | Verify a pinned eligibility receipt and start/stop only its exact isolated session envelope; distinct identity from trainer/evaluators |
| SHADOW evaluator | Compromise-assumed isolated consumer | Read mirrors, append evaluation evidence only |
| Researchers/model developers | Authenticated but fallible/possibly malicious insiders | Create proposals/artifacts, not approve themselves |
| Human approvers | High-trust, authenticated governance actors | Decide exact, scoped gates with separation of duties |
| CI/repository/dependency systems | Supply-chain trust boundary | Build and verify pinned artifacts; no model-driven approval |
| Legacy bots/workflows | Untrusted legacy surface for WLA purposes | None until inventoried and contained/adopted |

### Trust boundaries

```text
[External providers]
        | untrusted data
        v
[WOLF15 canonical authority]
        | TB-1: typed, one-way, observational export
        v
[Journal ingress + quarantine] -- TB-2 --> [append-only evidence store]
        |                                  |
        | TB-3 derived-job input           | TB-4 point-in-time query
        v                                  v
[Orchestrator / Replay / Dataset builders / Reflection sandbox]
        | TB-5 sealed artifact registry
        v
[Challenger training + independent evaluation]
        | TB-6 explicit human SHADOW-policy/authority gate
        v
[isolated SHADOW]
        -X- TB-7: no WOLF15/control/broker/EA path

[Legacy repos/workflows] -X- TB-8: quarantine; no implicit imports or credentials
```

### Boundary requirements

- `TB-1`: source identity, ordering, hashes, time, and observational authority are
  typed; export append is atomic with the canonical source transaction or has an
  equally strong reconciliation proof. WLA ingress, backlog, or outage is never a
  synchronous acknowledgement or dependency for WOLF15 analysis/risk/execution;
  source-local export failure semantics belong to explicit WOLF15 governance.
- `TB-2`: malformed, unknown-version, conflicting, or gap-affected input is
  quarantined without source mutation.
- `TB-3/TB-4`: derived jobs use least-privilege read roles and explicit as-of
  queries; raw evidence and projections have separate write roles.
- `TB-5`: artifacts are content-addressed, signed/attested, scanned, immutable,
  and loaded with safe formats; untrusted model deserialization is prohibited.
- `TB-6`: the human gate binds the exact SHADOW policy, authority ceiling,
  controller/evaluator identities, and control evidence; it cannot be supplied by
  artifact owners, CI, agents, or models alone. It does not sign every
  Challenger/session. Each instance instead requires an automated eligibility
  receipt bound to its exact Challenger, dataset, policy, limits, and expiry.
- `TB-7`: credential, ACL, and egress controls deny verdict, risk, execution,
  broker, EA, GitHub mutation, and WOLF15 write paths.
- `TB-8`: every legacy trigger, credential, import, and egress path reaches
  containment level L3 or L4 before Gate P0-A.

### Attacker-controlled and operator-controlled inputs

Attacker-controlled or compromise-assumed inputs include market/vendor payloads,
transport frames, repository dispatch payloads, filenames/paths, artifact
metadata, model files, dependency packages, prompts/reflection text, timestamps,
event IDs, source references, and resource-size/cardinality parameters.

Operator-controlled inputs include gate decisions, retention actions, stage
configuration, kill/disable controls, approved source policies, and credentials.
Operator input is authenticated and audited but not assumed correct.

Developer-controlled inputs include contracts, feature/label code, split rules,
dependencies, migrations, and workflow definitions. Code review and CI reduce but
do not eliminate insider and supply-chain risk.

### Assumptions

- WOLF15's internal Alpha correctness and execution constitution are governed by
  WOLF15, not re-proven by WLA. WLA verifies exported identity and integrity.
- WOLF15 exposes or will expose a source-owned, observational contract suitable
  for WLA-01; the existing ObserverTelemetryEnvelopeV1 is prior art, not the new
  learning contract.
- Trustworthy identity, UTC time, immutable revision IDs, and a secrets manager
  are available before runtime work.
- Human approvers authenticate individually; shared approvals are invalid.
- `WLA00-EXC-001` is a disclosed single-owner bootstrap exception, not shared or
  independent approval. It accepts the lack of separation only for WLA-00 and
  WLA-01 contract-only artifacts, expires at WLA-01 completion or scope
  expansion, and cannot satisfy any runtime, repository-creation, deployment, or
  Gate P0-A separation requirement.
- SHADOW can be deployed in a separate identity/failure domain with default-deny
  egress.

If an assumption is unverified, its dependent gate remains `BLOCKED` or
`NOT_MEASURED`.

## Attack Surface, Mitigations, and Attacker Stories

| Attack surface / story | Security outcome | Required mitigations |
| --- | --- | --- |
| Forge a WOLF15 event or relabel a legacy row as canonical Alpha | Poison Facts and all descendants | Producer authentication, source allowlist, typed authority, stable IDs, hashes/signatures, revision binding, quarantine |
| Replay an event, reuse an ID with changed content, or fork a stream | Duplicate or inconsistent evidence | Deterministic IDs, idempotency, monotonic per-stream sequence, predecessor hash, conflict quarantine, reconciliation |
| Shift timestamps or exploit late/revised data | Lookahead leakage and false performance | Distinct clocks, point-in-time views, revision history, maturity rules, clock-health checks, canary tests |
| Replace missing data with zero/default/random/“now” or relabel synthetic data as observed | Fabricated evidence and false readiness | Explicit epistemic status, typed synthetic namespace, fail-closed admission, provenance tests |
| Backfill Outcome into a Fact or infer fill from price touch | Label leakage/fabricated execution truth | Separate artifacts, source-owned outcome evidence, horizon/maturity policy, append-only corrections |
| Poison Episode membership or split related samples across partitions | Inflated evaluation | Versioned deterministic assembly, grouping, purge/embargo, sealed split manifest, independent review |
| Reflection/prompt injection claims a rule is approved | Authority creep through narrative | Reflection status/type isolation, citations, untrusted-text handling, no tool/control credentials, human curation |
| Malicious dataset/model artifact exploits deserialization | Code execution or credential theft | Safe non-executable formats, sandboxing, signature/digest verification, no secrets, read-only filesystem, resource limits |
| Compromised Orchestrator submits huge/repeating jobs | Availability/cost exhaustion | Quotas, bounded cardinality, idempotent jobs, cancellation, isolation, rate limits, budget alerts |
| Invoke a legacy runtime command/Redis/dispatch backchannel | Source or repository mutation outside WLA gates | No inbound WLA callback, L3/L4 legacy containment, scoped identities, network deny, command allowlist |
| Metric poisoning or selective reporting triggers promotion | Unsafe capability expansion | No auto-promotion, sealed protocol, denominators/uncertainty, failed-run retention, independent reviewer, human gate |
| Steal CI/GitHub/cloud credentials through training code | Repository/deployment compromise | Per-stage identities, short-lived scoped tokens, secretless jobs where possible, egress policy, provenance attestations |
| Reactivate legacy scheduled workflows or auto-merge hooks | Bypass WLA gates and mutate repositories | L3/L4 containment, workflow inventory, disabled triggers/credentials, CI denylist, protected branches, review |
| Compromise SHADOW and call WOLF15/broker/control plane | Trade or source impact | Separate account/network, no relevant DNS/routes/secrets, ACL deny, egress tests, independent kill switch |
| Abuse correction/retention to erase adverse results | Cherry-picking and audit loss | Append-only invalidation, tombstones, approval for label-affecting correction, immutable prior manifests |
| Cross-tenant/project path traversal or object-ID abuse | Read/overwrite other evidence | Canonical paths, object-level authorization, tenant/project binding, no user-controlled filesystem paths |

### Critical/high control accountability

Every Critical or High threat blocks its named gate until the mapped evidence is
`PASS`. Test IDs below are constitutional obligations whose execution status is
currently `NOT_EXECUTED`.

| Control ID | Critical/high threat | Accountable owner | Owning stage/gate | Required evidence/test | Residual disposition |
| --- | --- | --- | --- | --- | --- |
| `TM-C01` | WLA mutates WOLF15, verdict/risk, broker/EA, or execution | `SEC` with `WAO` concurrence | Downstream charter allocation and P0-A | `NEG-CAP-001`: credentials, ACL, egress, callback, and prohibited-call negatives | `BLOCK` until pass; no risk acceptance |
| `TM-C02` | Forged/relabelled/replayed/forked canonical event | `WAO` with `JDS` | WLA-01 contract fixtures plus downstream transport charter/P0-A | `SRC-INT-001`: producer identity, authority, canonical hash, stable ID, gap/fork/conflict fixtures | `BLOCK` until pass |
| `TM-C03` | Temporal leakage or fabricated Outcome passes evaluation | `MRR` with `JDS` | Downstream charter allocation and P0-A | `TIME-LEAK-001`: future canary, revisions, maturity, split, transform, holdout tests | `BLOCK` until pass |
| `TM-C04` | Malicious/tampered Dataset, model, or executable artifact | `SEC` with `MRR` | Downstream charter allocation and Challenger gate | `ART-SUPPLY-001`: safe format, digest/signature, sandbox, dependency provenance, tamper tests | `BLOCK` until pass |
| `TM-C05` | Self-approval, forged gate, metric-driven promotion, or policy-evaluator collusion | `ARO` with `SEC`/`MRR` concurrence | Downstream charter allocation and each authority gate | `GATE-SOD-001`: identity, evidence binding, concurrence, expiry, producer/evaluator separation negatives | `BLOCK` until pass |
| `TM-C06` | Legacy workflow/bot/Redis/dispatch/source-write path reactivated | `SEC` with `OPS` | P0-A | `LEGACY-CONT-001`: complete inventory plus L3/L4 trigger, secret, import, and egress enforcement | `BLOCK`; removal/archive preferred |
| `TM-C07` | CI, repository, registry, or cloud credential theft | `SEC` with `OPS` | Downstream charter allocation and deployment gates | `SUPPLY-ID-001`: short-lived scoped identities, secret scan, egress and provenance attestation | `BLOCK` until pass |
| `TM-C08` | Learning backlog/outage degrades WOLF15 authority path | `WAO` with `OPS` | Downstream transport charter and P0-A | `BACKPRESSURE-001`: saturation/outage test proving no synchronous acknowledgement or source degradation | `BLOCK` until pass |
| `TM-C09` | Compromised SHADOW escapes to source/control/execution | `SEC` with `OPS` | Future SHADOW policy gate | `SHADOW-ISO-001`: separate identity/account/network, no secrets/routes, kill and egress negatives | SHADOW remains `BLOCKED` until pass |

There may be additional Medium/Low controls, but no Critical/High threat may be
unowned, unmapped, expired, waived by automation, or represented by
`NOT_EXECUTED` at a passing gate.

### Existing controls and useful prior art

At WOLF15 PR-W1 revision `7ff2a9194b22e185b35dc61574c61628ba404939`,
`contracts/observer_telemetry_export_v1.py` demonstrates frozen schemas, canonical
JSON hashing, stable logical identities, explicit source/authority, UTC timing,
and `observer_can_mutate_source=false`. `storage/observer_export_outbox.py`
demonstrates transactional append, stream sequence, predecessor hashes, and
conflicting-duplicate detection. These controls are design evidence only until
the future learning contract and deployment pass their own gates.

The legacy Hybrid repository also contains adverse prior art that must not cross
the boundary: `core/reflective/relearning_cycle.py` writes configuration,
`scripts/tuyul_cli_autopush.py` pushes repository state, and
`ai_bridge/github_automerge_hook_v6.py` can merge from metric thresholds.

### Out-of-scope attacker stories

- A complete compromise of WOLF15's constitutional source is outside WLA's
  prevention scope, but WLA must limit blast radius and preserve detectable
  provenance/integrity failures.
- Broker-market misconduct is outside WLA. WLA has no broker capability and may
  only consume approved, source-owned outcome evidence.
- Generic market-model quality failure without a violated integrity, leakage, or
  authority invariant is a model-risk issue, not automatically a security
  vulnerability.
- Loss of a disposable Adaptive Memory index is primarily availability if the
  canonical ledger and rebuild manifest remain intact.

## Severity Calibration (Critical, High, Medium, Low)

### Critical

A realistic path allows learning or SHADOW to issue/alter orders, mutate WOLF15
Alpha/verdict/risk/configuration, bypass a kill/governance lock, acquire broker/EA
credentials, or self-promote/deploy into an execution-capable path. Also critical:
forged gate approval that directly grants such capability.

`WLA00-EXC-001` does not satisfy `GATE-SOD-001`. It is a time- and scope-bounded
owner risk acceptance for contract-only work. `TM-C05` remains blocking before
runtime registration, database/outbox activation, deployment, production or
advisory activation, learning-repository creation, Gate P0-A, or any broader
authority.

### High

A realistic path forges canonical-looking Facts/Outcomes at scale, defeats
append-only integrity, steals high-impact CI/cloud/repository credentials, causes
systematic temporal leakage that can pass a human gate, substitutes a malicious
model artifact for a reviewed digest, or reactivates legacy mutation workflows.

### Medium

A flaw exposes non-secret research evidence beyond intended readers, corrupts a
bounded derived projection that is detected before a gate, permits resource
exhaustion isolated to learning, or causes incomplete audit metadata without
changing canonical evidence or authority.

### Low

A defect affects documentation, low-sensitivity metadata, or a disposable local
index with no credible path to evidence corruption, credential exposure, gate
bypass, WOLF15 influence, or execution. Cosmetic metric/display discrepancies
remain low only when backend truth and gate behavior are unaffected.

Severity is raised when the affected identity has broader credentials, the
artifact can cross a gate, or detection/recovery evidence is absent. It is lowered
when default-deny capability controls independently prevent source/control impact.

Repository: TUYUL-KARTEL-FX-AGI-HYBRID::docs/architecture/wla-00
Version: ba70b5e6d29391fcbe6d5eaf67dd7a47b76dc09d
