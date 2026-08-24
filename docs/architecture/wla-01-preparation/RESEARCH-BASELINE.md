---
title: WLA-01 Pre-Charter Research Baseline
document_role: NON_NORMATIVE_RESEARCH
program_stage: NOT_STARTED
date: 2026-08-24
---

# WLA-01 Pre-Charter Research Baseline

This document records early research explicitly permitted by WLA-00. It does not
accept WLA-00, start or pass WLA-01, define a wire contract, modify WOLF15, create
a learning repository, activate an outbox consumer, or grant runtime authority.

WLA-01 remains `NOT_STARTED`. Every candidate decision below is subordinate to
the WLA-00 constitution and requires an accepted WLA-01 charter before code is
written.

## 1. Evidence baseline

| Evidence | Exact baseline | Research use | Limitation |
| --- | --- | --- | --- |
| WLA-00 reviewed scope | Combined digest `e7671f213f9dc9dda56ab19ca30efd0cc6e7f50d6ef94d562d11fb84fea45818` | Governing semantic requirements | Ratification remains `NOT_EVALUATED` |
| Frozen WOLF15 observer export | `TUYUL-FX-WOLF-15LAYER-SYSTEM-prw1`, branch `feat/observer-telemetry-export-v1`, revision `7ff2a9194b22e185b35dc61574c61628ba404939` | Verified source-export prior art | Read-only research source; it is not `AlphaLearningEnvelopeV1` |
| WOLF15 primary checkout | Revision `7c45484e9124bb4a8a745dc1ef8832a7745ea58c` with unrelated local changes | Existence and divergence check only | Excluded from content analysis and must not be modified by this work |

The frozen PR-W1 worktree was clean before and after the read-only inspection.
Twenty-two targeted unit tests covering its envelope and outbox passed locally
with bytecode and pytest cache writes disabled. No PostgreSQL integration test,
runtime, deployment, network, broker, or EA state was executed or measured in
this research pass.

### Pinned prior-art files

| Repository-relative path | SHA-256 |
| --- | --- |
| `contracts/observer_telemetry_export_v1.py` | `787f3e2219a9778a4bcff21428c59be3d517d96ee0cac40a5c511a4d580dd672` |
| `storage/observer_export_outbox.py` | `bc7e6bfd69da13bf9e80a7256d5b32772fa3fd921095ced82326a913d3f2f622` |
| `storage/migrations/versions/20260822_01_observer_export_outbox.py` | `3e6ccafcb4bdc9827ef5c05d8d9f3af8c2db7a0634c6f4ca87b0e543b7664aed` |
| `tests/test_observer_telemetry_export_v1.py` | `4d5b20e1b336af635d28e24cef4cd83ada6313f180057d1d09afc0fe529b3e81` |
| `tests/test_observer_export_outbox.py` | `09eda0045afae528664699295222c69ee7c51d55b38607104ba1a5d12cd8294c` |
| `tests/integration/test_observer_export_outbox_postgres.py` | `bf52238e9056beae12c74e0fdf71f93cbf8700d9eeddf5059832c1f064c9be48` |

## 2. What PR-W1 already proves locally

`ObserverTelemetryEnvelopeV1` is useful prior art for a WOLF15-owned,
observational export boundary:

- frozen models reject extra fields;
- canonical UTF-8 JSON uses sorted keys, compact separators, and rejects NaN;
- payload types, payload versions, and source authority classes are bound through
  a closed registry;
- stable UUIDv5 event identity derives from payload type and logical event key;
- stream sequence and predecessor hash are contiguous;
- source system is fixed to `WOLF15`, with service, revision, deployment, schema,
  and policy identity;
- payload and envelope hashes are deterministic;
- `observer_authority` is fixed to `OBSERVATIONAL_ONLY` and
  `observer_can_mutate_source` is fixed to false;
- identical retries are idempotent while same-ID/different-content retries are
  integrity conflicts;
- the outbox append shares the caller-owned canonical transaction, advances a
  locked stream head, and reads without storing a consumer cursor in WOLF15; and
- the database migration supplies immutable-row enforcement and SELECT-only
  observer grants.

These properties should be reused as tested design patterns. Reuse does not mean
renaming the existing envelope or treating its current payload registry as the
learning contract.

## 3. Requirement-to-prior-art gap map

| WLA-00 semantic group | PR-W1 coverage | WLA-01 gap or required disposition |
| --- | --- | --- |
| Contract identity | Source schema version plus payload type/version exist | Add explicit `envelope_version`, `event_name`, `event_version`, and `schema_id`; do not infer them from a Python class name |
| Stable identity | UUIDv5 event ID exists; logical key exists only in the draft/outbox column | Serialize a bounded `logical_event_key`; define the canonical identity tuple and collision domain across services and deployments |
| Causality | Payload-specific source IDs or evidence refs exist in some bodies | Add typed correlation, nullable causation, bounded direct refs, and sealed ancestry-manifest/range references with an integrity root |
| Stream integrity | Sequence, predecessor sequence, and predecessor hash are strong | Specify gap, fork, duplicate, cross-deployment retry, and stream-reset behavior with canonical fixtures |
| Source provenance | System, service, commit, deployment, schema, and policy are present | Add explicit config identity and a fail-closed policy for unavailable code revision; `UNAVAILABLE` cannot silently become eligible |
| Time | Only occurred and source publication times exist | Resolve observed, first-received, ingested, learning-available, precision, and clock-health semantics without mutating the source event |
| Authority | Source authority class and observational consumer ceiling exist | Map the closed WLA authority taxonomy; add decision and human-gate authority fields with event-specific invariants |
| Safety | Source mutation is fixed false | Also fix verdict, execution, and self-promotion capability to false; payloads cannot override any safety field |
| Integrity | Payload hash and externally stored envelope/event hash exist | Pin a canonicalization version and define the exact non-self-referential hash projection carried or stored with serialized bytes |
| Quality | Some payloads contain decisions, coverage, and reason codes | Add generic evidence status, reason codes, missingness, uncertainty, correction, supersession, and invalidation references |
| Trace | Source deployment and policy are present | Add producer run ID and typed replay, dataset, model, and manifest references for derived events |
| Cardinality | Some source ID tuples are bounded only by type shape | Set byte, direct-ref, batch, query-span, and retry limits; use sealed manifests for large ancestry |
| Outcome Evidence | Execution-command state can be mirrored | Define source-owned fill, reject, cancel, partial-fill, and approved horizon evidence; command state or price touch alone is not Outcome Evidence |
| Learning ingress | Not implemented | Define reference parsing, duplicate, quarantine, gap, and conflict fixtures only; no runtime consumer is authorized in WLA-01 |

## 4. Recommended temporal ownership model

A single source event cannot truthfully know future ingress timestamps, and an
append-only source event cannot be updated after Journal receipt. The WLA-01
charter should therefore resolve the required clocks through event-owned temporal
profiles:

| Event owner/profile | Required clocks | Forbidden behavior |
| --- | --- | --- |
| WOLF15 source export | `occurred_at_utc`, `observed_at_utc`, `source_published_at_utc`, precision, clock health | Fabricating receipt/ingestion time or accepting a learner callback |
| Journal ingress receipt | `first_received_at_utc`, `ingested_at_utc`, `learning_available_at_utc` plus source-event reference | Rewriting or enriching the original WOLF15 event in place |
| Derived WLA artifact | Source clocks by reference plus applicable maturity, seal, and invalidation clocks | Backdating availability or hiding late arrival/correction |

The core envelope may use a discriminated temporal profile or event-specific
typed extension. It should not make future consumer-owned timestamps nullable in
a way that lets producers omit clocks they actually own.

## 5. Candidate minimum contract architecture

The charter should specify one versioned envelope core and a closed event-payload
registry. This is a design candidate, not a wire schema:

| Component | Minimum responsibility |
| --- | --- |
| `ContractIdentityV1` | Envelope version, event name/version, schema ID, canonicalization version |
| `EventIdentityV1` | Stable event ID and bounded logical event key |
| `CausalityV1` | Correlation, causation, bounded direct refs, optional sealed ancestry reference |
| `StreamPositionV1` | Stream ID, sequence, predecessor sequence/hash, declared ordering scope |
| `SourceIdentityV1` | System, service, immutable revision, deployment, policy, config identity |
| Typed temporal profile | Source, ingress, or derived clocks with ordering and uncertainty validation |
| `AuthorityV1` | Closed source/evidence authority, observational source interaction, no WLA decision authority except scoped human gate records |
| `SafetyV1` | Four literal-false invariants for source mutation, verdict, execution, and self-promotion |
| `IntegrityV1` | Payload hash, detached envelope/content hash rule, canonicalization version |
| `QualityV1` | Evidence status, reasons, missingness, uncertainty, correction/supersession/invalidation refs |
| `TraceV1` | Producer run and bounded replay/dataset/model/manifest references |
| Event-specific payload | Closed schema selected by event name and version; extra or unknown fields fail closed |

WLA-01 should initially implement positive source payloads only for
`wolf15.alpha-fact.exported.v1` and
`wolf15.outcome-evidence.exported.v1`. Other WLA-00 catalog names remain known
but unsupported until their owning stage registers an accepted payload schema.
Known-but-unsupported and unknown events are quarantined, never parsed as a
generic dictionary with authority-bearing meaning.

## 6. Identity and hashing decisions to resolve

1. Event identity must survive identical retry across producer restarts without
   allowing two services or event types to collide. Deployment ID should remain
   provenance, not automatically become part of logical identity.
2. The logical identity tuple should include at least event name/version, source
   system or source namespace, and a source-owned logical key. The exact tuple
   requires WAO/JDS review.
3. The serialized envelope hash cannot include itself recursively. WLA-01 must
   define either a detached hash or an exact canonical projection that excludes
   the hash field.
4. Payload hash and envelope hash must declare one canonicalization version.
   Consumers may not reconstruct alternative bytes and call them canonical.
5. A same-ID/same-content retry is a duplicate. Same-ID/different-content is a
   conflict. A correction is a new event with explicit correction/supersession
   references, never an overwrite.

## 7. Candidate fixture matrix

### Positive fixtures

- canonical Alpha Fact with exact bytes, payload hash, envelope hash, and stable
  ID;
- source-owned fill, reject, cancel, and partial-fill Outcome Evidence variants;
- identical retry producing the same identity and hashes;
- contiguous two-event stream chain;
- a Journal acceptance receipt that references rather than mutates the source
  envelope; and
- a bounded ancestry-manifest reference whose count/range/integrity root match.

### Negative and fail-closed fixtures

- extra field, unknown event name, unknown major version, and unregistered payload;
- payload/event/authority mismatch and canonical-byte/hash mismatch;
- any safety invariant set true or omitted where the schema requires it;
- naive timestamp, invalid offset, unexplained inversion, or fabricated ingress
  timestamp in a source event;
- duplicate ID with conflicting content, sequence gap, fork, predecessor mismatch,
  or undeclared stream reset;
- oversized payload, excessive direct refs, invalid ancestry root, or unbounded
  inline lineage;
- unavailable source revision without an explicitly accepted quarantine policy;
- Outcome label or fill claim derived only from price touch or execution-command
  intent;
- source/derived authority relabeling, unknown authority class, or human-gate
  authority without authenticated decision evidence; and
- any attempt to serialize a command, verdict, order, broker call, repository
  mutation, deployment action, or promotion authority.

## 8. Proposed WLA-01 charter boundary

After WLA-00 is accepted, the bounded WLA-01 charter should authorize only:

1. a typed `AlphaLearningEnvelopeV1` contract and canonical serialization;
2. closed enums/registries for version, event, authority, quality, and safety;
3. source Alpha Fact and source Outcome Evidence payload schemas;
4. canonical positive and negative JSON/byte/hash fixtures;
5. pure contract tests and a no-storage/no-network reference parser; and
6. an exact verification receipt and human WLA-01 decision.

It should explicitly prohibit:

- changing or reusing the frozen PR-W1 branch;
- database migration, outbox consumer, queue, cursor, scheduler, workflow,
  credentials, deployment, or repository creation;
- Episode, Outcome-label, Replay, Reflection, Dataset, Challenger, or SHADOW
  runtime implementation;
- any WOLF15 acknowledgement dependency or WLA-to-WOLF15 write path; and
- treating test success as human acceptance or Gate P0-A evidence.

The likely implementation location is a new, isolated WOLF15 worktree/branch for
the producer-owned contract, with contract fixtures and pure tests beside it.
The exact base revision and file placement remain charter decisions. The current
frozen PR-W1 checkout and the dirty primary checkout are not eligible targets.

## 9. Research decision backlog

| ID | Decision needed | Required role review | Current research disposition |
| --- | --- | --- | --- |
| `WLA01-RD-001` | Exact envelope owner, repository, base revision, and branch strategy | `ARO`, `WAO`, `SEC` | Unresolved; no code target authorized |
| `WLA01-RD-002` | Stable logical identity tuple and collision domain | `WAO`, `JDS` | Reuse UUIDv5 pattern only after tuple is ratified |
| `WLA01-RD-003` | Source, ingress, and derived temporal profile encoding | `JDS`, `MRR` | Separate event-owned clocks recommended |
| `WLA01-RD-004` | Canonicalization version and non-self-referential envelope hash | `ARO`, `JDS`, `SEC` | Existing canonical JSON is prior art, not yet the WLA contract |
| `WLA01-RD-005` | Initial event registry and payload compatibility policy | `ARO`, `WAO`, `JDS` | Register only two source event families initially |
| `WLA01-RD-006` | Source Outcome Evidence variants and finality vocabulary | `WAO`, `JDS`, `MRR` | Command state and price touch are insufficient |
| `WLA01-RD-007` | Payload, reference, batch, query, and retry limits | `SEC`, `JDS` | Must be finite and fail closed |
| `WLA01-RD-008` | Missing revision and clock-uncertainty quarantine policy | `WAO`, `MRR`, `SEC` | Unknown cannot become eligible by default |

## 10. Exit condition from research

This research artifact may be used as input only after the WLA-00 ratification
packet records authenticated named owners/backups, required concurrence, and an
explicit `PASS` bound to the reviewed digest. The next artifact is then a
separately reviewed WLA-01 charter. Until that happens, status remains:

```text
WLA-00 ratification = NOT_EVALUATED
WLA-01 = NOT_STARTED
AlphaLearningEnvelopeV1 = NOT_IMPLEMENTED
runtime tests = NOT_EXECUTED
runtime state = NOT_MEASURED
wolf15-learning-journal = NOT_CREATED
```
