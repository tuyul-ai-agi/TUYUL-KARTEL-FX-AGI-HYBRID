# WLA-00 Event Vocabulary

Status: `PROPOSED`

Purpose: semantic vocabulary only; this is not the
`AlphaLearningEnvelopeV1` wire schema.

## 1. Naming grammar

Durable events use:

```text
<bounded-context>.<aggregate>.<past-tense-fact>.v<major>
```

An event says what already happened. Requests use a separate command channel and
an imperative verb. A command's acceptance is never inferred from delivery; a
resulting event or explicit rejection is required.

Each dot-delimited segment uses lowercase kebab-case; underscores are forbidden
in event names. A compound fact such as `observation-recorded` stays one segment.

Reserved words `promote`, `execute`, `order`, `deploy`, `champion`, and
`self_modify` MUST NOT appear in WLA event or command names under this
constitution.

## 2. Canonical nouns

| Term | Normative meaning |
| --- | --- |
| Alpha | A canonical WOLF15 decision artifact; never a learning prediction |
| Fact | Immutable source observation exported by WOLF15 with provenance |
| Fact receipt | Journal evidence that a Fact was accepted, duplicated, or quarantined; not a new Alpha fact |
| Episode | Deterministically sealed set of Fact references under a versioned assembly policy |
| Outcome Evidence | Source-owned Fact describing later fill/reject/cancel or approved horizon evidence; preserves source authority |
| Outcome | Matured WLA label derived from Outcome Evidence under a pinned labeling policy; authoritative only inside that policy/dataset lineage |
| Replay | Deterministic as-of reconstruction plus run receipt |
| Reflection | Cited, uncertain hypothesis derived from evidence |
| Dataset | Immutable sealed materialization with point-in-time lineage and splits |
| Challenger | Immutable candidate model/rule artifact evaluated under a pinned protocol |
| SHADOW | Isolated observational evaluation mode with no source/control/execution output |
| Correction | New append-only artifact emitted by the accountable owner of the artifact being corrected; it supersedes but never rewrites that artifact |
| Invalidation | Append-only declaration that an artifact is ineligible for new use |
| Gate decision | Human-authenticated `PASS` or `FAIL` bound to exact evidence |

“Champion”, “production model”, and “live learner” are outside the WLA-00
vocabulary.

Correction authority follows artifact authority. Only WOLF15/the approved source
owner may correct a source Fact or source Outcome Evidence. A WLA owner may
correct only its own derived artifact, such as an Outcome label, and that
correction remains derived evidence; it cannot correct, replace, or reinterpret
the source artifact itself.

## 3. Semantic envelope fields

WLA-01 MUST resolve these concepts into typed fields and canonical serialization:

| Group | Required semantics |
| --- | --- |
| Contract | `envelope_version`, `event_name`, `event_version`, `schema_id` |
| Identity | stable `event_id`, `logical_event_key` |
| Causality | `correlation_id`, nullable `causation_id`, bounded direct source refs, and for large ancestry a sealed manifest/range reference plus integrity root |
| Stream | `stream_id`, `stream_sequence`, predecessor sequence/hash for ordered streams |
| Source | `source_system`, `source_service`, code revision, deployment ID, policy/config version |
| Time | `occurred_at_utc`, `observed_at_utc`, `source_published_at_utc`, `first_received_at_utc`, `ingested_at_utc`, `learning_available_at_utc`, source precision/clock status |
| Authority | source authority class, `source_interaction_authority=OBSERVATIONAL_ONLY`, and a closed WLA evidence/governance authority class |
| Safety | `can_mutate_source=false`, `can_issue_verdict=false`, `can_execute=false`, `can_self_promote=false` |
| Integrity | canonical payload hash, envelope/event hash, canonicalization version |
| Quality | status, reason codes, missingness, uncertainty, correction/supersession refs |
| Trace | producer run ID and, when derived, replay/dataset/model manifest refs |

Safety fields are invariants, not feature flags. A payload cannot override them.

## 4. Closed conceptual authority taxonomy

WLA-01 MUST map the following closed concepts to typed values. It may refine a
class only through a reviewed contract version; it cannot accept arbitrary
authority strings.

| Authority class | Owner | Meaning | Capability ceiling in WLA |
| --- | --- | --- | --- |
| `WOLF15_CANONICAL_ALPHA` | WOLF15 | Source-owned canonical Alpha Fact | Mirrored data only; consumer is observational |
| `WOLF15_SOURCE_OUTCOME_EVIDENCE` | WOLF15/source execution bridge | Source-owned fill/reject/cancel or approved later evidence | Mirrored data only; not a WLA label |
| `WLA_JOURNAL_RECEIPT` | Journal | Acceptance, duplicate, quarantine, gap, or conflict evidence | Append-only learning evidence |
| `WLA_DERIVED_EPISODE` | Journal policy | Deterministic Fact grouping | Derived evidence only |
| `WLA_DERIVED_OUTCOME_LABEL` | Outcome-label policy | Matured label over Episode plus Outcome Evidence | Dataset lineage only |
| `WLA_DERIVED_REPLAY` | Replay policy | As-of reconstruction and receipt | Derived evidence only |
| `WLA_DERIVED_REFLECTION` | Reflection policy | Cited hypothesis | Advisory only |
| `WLA_DERIVED_DATASET` | Dataset policy | Sealed point-in-time materialization | Training/evaluation input only |
| `WLA_DERIVED_CHALLENGER` | Training policy | Candidate artifact and manifest | Challenger only |
| `WLA_DERIVED_SHADOW_EVIDENCE` | SHADOW policy | Non-actionable comparison evidence | Observational only |
| `HUMAN_GOVERNANCE_DECISION` | Authenticated approvers | Scoped program/policy/gate decision | Grants only the named WLA eligibility; never Alpha/execution authority |

Every WLA-produced or WLA-consumed envelope carries the invariant
`source_interaction_authority=OBSERVATIONAL_ONLY`. Source authority describes
provenance; it does not transfer the source's capability to a consumer. Derived
evidence carries `wla_decision_authority=NONE`. Only an authenticated
`HUMAN_GOVERNANCE_DECISION` may carry `wla_gate_authority=HUMAN_SCOPED`, limited
to the exact gate and evidence hashes it names. It still has no WOLF15, Alpha,
risk, verdict, or execution authority. Unknown authority classes are quarantined.

## 5. Allowed event catalog

| Event | Producer | Meaning | Required causal input |
| --- | --- | --- | --- |
| `wolf15.alpha-fact.exported.v1` | WOLF15 export adapter | Canonical Alpha-related Fact was exported observationally | Canonical WOLF15 source record |
| `learning.fact.accepted.v1` | Journal ingress | Source event passed contract/integrity checks and was appended | Exported Fact |
| `learning.fact.quarantined.v1` | Journal ingress | Source event was preserved outside eligible evidence with reasons | Received payload/transport receipt |
| `learning.episode.sealed.v1` | Episode builder | Episode membership and assembly policy were sealed | Accepted Facts |
| `learning.episode.invalidated.v1` | JDS-controlled invalidation recorder | Episode cannot be used for new downstream work | Episode plus correction/integrity evidence |
| `wolf15.outcome-evidence.exported.v1` | WOLF15 export adapter | Source-owned later outcome evidence was exported observationally | Canonical WOLF15/broker-bridge source record |
| `learning.outcome.label-matured.v1` | Outcome builder | Derived Outcome label became legally available under a pinned policy | Episode plus eligible Outcome Evidence |
| `learning.outcome.label-corrected.v1` | JDS-controlled Outcome correction recorder | New derived label supersedes an earlier label after source/policy correction | Earlier Outcome, correction, and labeling policy |
| `learning.replay.completed.v1` | Replay engine | Deterministic replay completed with sealed receipt | Eligible Episode/Outcome and pinned manifest |
| `learning.replay.failed.v1` | Replay engine | Replay terminated without valid semantic output | Requested manifest and failure evidence |
| `learning.reflection.proposed.v1` | Reflection engine/researcher | Cited hypothesis was proposed | Replay/evidence references |
| `learning.reflection.reviewed.v1` | Human review recorder | Reflection disposition was recorded | Proposed Reflection and reviewer identity |
| `learning.dataset.sealed.v1` | Dataset builder | Point-in-time dataset and splits were sealed | Eligible evidence/replay manifests |
| `learning.dataset.invalidated.v1` | JDS-controlled invalidation recorder | Dataset is ineligible for new use | Dataset and correction/leakage evidence |
| `learning.challenger.registered.v1` | Training runner | Immutable candidate artifact was registered | Sealed Dataset and training manifest |
| `learning.challenger.evaluated.v1` | Independent evaluator | Pinned evaluation completed | Challenger and evaluation protocol |
| `learning.challenger.invalidated.v1` | MRR-controlled invalidation recorder | Challenger is ineligible for new evaluations | Challenger and defect evidence |
| `learning.eligibility.evaluated.v1` | Policy evaluator | Automated artifact eligibility was evaluated under an already ratified policy | Artifact, policy version, and machine-check evidence |
| `learning.shadow.started.v1` | SHADOW session controller | Policy-eligible isolated evaluation session started | Challenger, active human-ratified SHADOW policy, and eligibility receipt |
| `learning.shadow.observation-recorded.v1` | Shadow evaluator | Non-actionable prediction/comparison evidence was appended | Shadow session and mirrored Fact |
| `learning.shadow.completed.v1` | Shadow evaluator | Shadow protocol reached its declared end | Shadow session observations |
| `learning.shadow.stopped.v1` | SHADOW session controller | Shadow session was killed or isolated without expanding capability | Session, authenticated operator/safety action, and reason |
| `learning.gate.decision-recorded.v1` | Human approval recorder | Explicit gate `PASS` or `FAIL` was recorded | Exact evidence digests and approvers |
| `learning.artifact.invalidated.v1` | Accountable-owner-controlled invalidation recorder | Generic derived artifact is blocked from new use | Artifact and reason evidence |

The Producer column names the emitting service identity or service class, not a
new human governance role. Human accountability and permitted writers are those
in [the ownership matrix](OWNERSHIP-MATRIX.md). A human/operator safety action is
authenticated causation for a stop; the dedicated controller remains the sole
writer of SHADOW session lifecycle receipts.

WLA-01 MAY split an event into narrower versioned types, but it MUST NOT collapse
different lifecycle nouns or broaden any authority.

## 6. Commands

The only command families eligible for later design are:

- `request_fact_reconciliation`;
- `request_episode_build`;
- `request_outcome_maturity_check`;
- `request_replay`;
- `request_reflection`;
- `request_dataset_build`;
- `request_challenger_training`;
- `request_challenger_evaluation`;
- `request_shadow_start`; and
- `request_shadow_stop`.

Commands MUST be idempotent, authenticated, scoped to learning-owned resources,
and auditable. `request_shadow_start` requires an active human-ratified SHADOW
policy and a passing automated eligibility receipt. It does not require a new
human decision for every run unless that policy explicitly says so.
`request_fact_reconciliation` is strictly an internal comparison against the
already exported ledger; it MUST NOT call back to WOLF15 or request source repair.

## 7. Status vocabularies

### Evidence quality

`VALID`, `QUARANTINED`, `UNKNOWN`, `NOT_MEASURED`, `NOT_APPLICABLE`,
`SUPERSEDED`, `INVALIDATED`.

`VALID` means only that contract, provenance, integrity, and eligibility checks
for that evidence class passed. It never means `valid_for_execution`, gate
`PASS`, safe, ready, accurate, profitable, or authorized.

### Outcome maturity

`PENDING`, `MATURED`, `CENSORED`, `UNKNOWN`, `INVALIDATED`.

### Gate

`NOT_EVALUATED`, `PASS`, `FAIL`, `BLOCKED`, `EXPIRED`. Only an explicit, current
`PASS` grants the specific eligibility named by that gate.

### Program stage

`NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `PASS`, `FAIL`.

### Verification execution

`NOT_EXECUTED`, `PASS`, `FAIL`, `BLOCKED`. `NOT_EXECUTED` is never a pass or code
failure.

### Repository lifecycle

`NOT_CREATED`, `ELIGIBLE`, `CREATED`, `ARCHIVED`. `ELIGIBLE` is not permission to
skip the creation gate.

### Run completion

`COMPLETED`, `FAILED`, `CANCELLED`, `NON_DETERMINISTIC`, `QUARANTINED`.

Statuses from different vocabularies are not interchangeable. In particular,
`COMPLETED` is not `PASS`, and `UNKNOWN` is not zero.

## 8. Cardinality and load limits

- Direct causal references are bounded by the contract. Large ancestry uses an
  immutable manifest URI/ID, covered range, count, and integrity root.
- Dataset rows and event IDs MUST NOT be embedded wholesale in a parent envelope.
- Payload size, source-ref count, stream batch size, query span, retry count, and
  job resource budgets have fail-closed limits.
- Backpressure is absorbed inside learning-owned queues/storage. It can delay WLA
  availability but cannot synchronously block WOLF15 Alpha, risk, or execution.

## 9. Compatibility rules

- Major versions are explicit and never guessed.
- Unknown event names, major versions, authority classes, or safety semantics are
  quarantined.
- Additive optional fields require a declared minor-version policy in WLA-01.
- Renames use a new version; consumers do not maintain undocumented aliases.
- Legacy Quad Repo event names have no WLA compatibility status by default.
