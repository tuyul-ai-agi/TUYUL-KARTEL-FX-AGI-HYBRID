---
title: WLA-01 and WLA-02 Cross-Repository Governance Reference
document_role: GOVERNANCE_REFERENCE_ONLY
reference_classification: NON_NORMATIVE_REFERENCE
hybrid_code_target: NONE
canonical_code_target: tjx578/TUYUL-FX-WOLF-15LAYER-SYSTEM
canonical_schema_owner: WOLF15
hybrid_charter_state: LOCAL_UNCOMMITTED
cross_repo_binding: PENDING_VERIFICATION
date: 2026-08-25
---

# WLA-01 and WLA-02 Cross-Repository Governance Reference

This document is a non-normative governance and research reference retained at
the original stable path. It does not own, define, amend, or implement the
canonical WLA contract. WOLF15 is the canonical code and schema owner; any
conflict is resolved in favor of the authenticated WOLF15 artifacts.

## 1. Authority binding and current status

This reference is subordinate to and bounded by the immutable signed decision:

| Authority field | Bound value |
| --- | --- |
| Decision record | `WLA00-RD-20260824-001` |
| Ratification ID | `de760418-7c42-4cfc-b1cf-a8f472aefba4` |
| Canonical verdict | `PASS` |
| Effective at | `2026-08-24T08:04:07Z` |
| Reviewed WLA-00 digest | `c2905ff65b9dd9bf07da555ce1cd6ea1e2898432f6f49a5e5d98a7a6cbb6fb6d` |
| Verified attestation commit | `726f368aaa5f549348674be8eac0a29578412b40` |
| Governance mode | `SINGLE_OWNER_BOOTSTRAP` |
| Exception | `WLA00-EXC-001` |
| Authorized scope | `CONTRACT_ONLY` |

The reconciled program status is:

```text
DOCUMENT_ROLE                    = GOVERNANCE_REFERENCE_ONLY
REFERENCE_CLASSIFICATION         = NON_NORMATIVE_REFERENCE
HYBRID_CODE_TARGET               = NONE
CANONICAL_CODE_TARGET            = tjx578/TUYUL-FX-WOLF-15LAYER-SYSTEM
CANONICAL_SCHEMA_OWNER           = WOLF15

WLA_00_RATIFICATION              = PASS
WLA_01_AUTHORIZED_BASE           = 7ff2a9194b22e185b35dc61574c61628ba404939
WLA_01_COMPLETION_COMMIT         = 22ee9774930d2bf5d09a32851098a8dba8918167
WLA_01_CANONICAL_STATUS          = PASS
WLA00_EXC_001                    = EXPIRED_CONSUMED

WLA_02_GOVERNANCE_HEAD           = 97567f6070cfa6584dcbe32fb442498ee45382c2
WLA_02_IMPLEMENTATION_COMMIT     = 85260251e456ef1c7f0475b7a078fc95616ba86d
WLA_02_COMPLETION_RECEIPT_COMMIT = 247075035bc0d69c7122d15313db01cb65f6249f
WLA_02_IMPLEMENTATION            = PASS
WLA_02_DOD                       = PASS
WLA_02_PUBLICATION               = COMPLETE
WLA02_EXC_001                    = EXPIRED_CONSUMED

WLA_03_AUTHORIZED                = FALSE
GATE_P0_A                        = NOT_EVALUATED
WOLF15_LEARNING_JOURNAL          = NOT_CREATED
HYBRID_CHARTER_STATE             = LOCAL_UNCOMMITTED
CROSS_REPO_BINDING               = PENDING_VERIFICATION
RUNTIME_MUTATION                 = NONE
```

Pre-signature `NOT_EVALUATED` and `NOT_STARTED` statements in
`wla-00/RATIFICATION-PACKET.md`, `wla-00/VERIFICATION-RECEIPT.md`, and the
ratified 19-file WLA-00 constitution are historical as-of statements. They MUST
NOT be rewritten: the packet hash and reviewed digest are inputs to the signed
decision. For current status, authenticated WOLF15 decisions, implementation
receipts, and their exact commits take precedence over this reference.

The research baseline is explicitly excluded from the 19-file normative set and
the 38-file supporting set recorded in `wla-00/VERIFICATION-RECEIPT.md`:

```text
SIGNED_SET_MEMBERSHIP = EXCLUDED
SIGNED_57_FILE_DIGEST  = c2905ff65b9dd9bf07da555ce1cd6ea1e2898432f6f49a5e5d98a7a6cbb6fb6d
CHARTER_SHA256         = MEASURED_EXTERNALLY_PER_LOCAL_REVISION
```

The signed digest therefore remains a historical snapshot, while this file's
current SHA-256 is independent evidence and must not be written into the signed
receipt.

## 2. Objective, deliverables, and non-goals

The canonical WLA-01 implementation in WOLF15 defines the version-one
producer-to-learning contract for exactly two source-owned event families:

- `wolf15.alpha-fact.exported.v1`; and
- `wolf15.outcome-evidence.exported.v1`.

Sections 4 through 8 retain a non-normative research projection of the closed
`AlphaLearningEnvelopeV1` schema, canonical serialization and hash rules, and 22
fixture cases. They are traceability aids only. They neither override the
canonical WOLF15 contract nor authorize duplicate schema, fixture, or test
implementation in HYBRID.

WLA-01 does not authorize any of the following:

- runtime registration, application wiring, imports from a live runtime, or a
  deployed producer or consumer;
- database tables, migrations, object stores, filesystems used as storage,
  caches, queues, schedulers, cursors, checkpoints, or retention jobs;
- a new or generalized outbox, changes to the frozen PR-W1 outbox, an outbox
  consumer, dispatcher, transport, webhook, callback, or acknowledgement path;
- creation, initialization, or remote provisioning of any repository, including
  `wolf15-learning-journal`;
- WLA-to-WOLF15 writes to databases, outboxes, caches, configuration, feature
  flags, repositories, queues, APIs, or control surfaces;
- WOLF15 repair/reconciliation calls, inbound WLA callbacks, or any reverse
  channel hidden behind nominally read-only code;
- broker, EA, terminal, order-router, risk-reservation, trade-outbox, deployment,
  merge, or production credentials or calls;
- Episode, Outcome-label, Replay, Reflection, Dataset, Challenger, or SHADOW
  runtime implementation; or
- verdict, execution, advisory activation, promotion, self-promotion, Gate P0-A
  certification, or a claim of production readiness.

The envelope mirrors source evidence. It is not a command, acknowledgement,
repair request, verdict, order, signal, or permission.

## 3. Repository ownership and code target

```text
HYBRID_CODE_TARGET           = NONE
CANONICAL_CODE_TARGET        = tjx578/TUYUL-FX-WOLF-15LAYER-SYSTEM
CANONICAL_SCHEMA_OWNER       = WOLF15
WLA_01_AUTHORIZED_BASE       = 7ff2a9194b22e185b35dc61574c61628ba404939
WLA_01_COMPLETION_COMMIT     = 22ee9774930d2bf5d09a32851098a8dba8918167
WLA_01_CANONICAL_STATUS      = PASS
```

The WOLF15 SHA `7ff2a9194b22e185b35dc61574c61628ba404939` is the authorized WLA-01 base.
The completed contract is bound to WOLF15 commit
`22ee9774930d2bf5d09a32851098a8dba8918167`. HYBRID remains a documentation
consumer and has no WLA schema implementation target.

No schema file, fixture file, pure contract test, runtime registration, or
implementation branch may be created from this reference in HYBRID. Any later
cross-repository integration requires separate authenticated authorization and
must consume the WOLF15-owned contract without forking ownership.

## 4. WLA01-RD decision register

All eight pre-charter decisions are retained for traceability. Their canonical
resolution is the completed WOLF15 implementation, not this reference.

| ID | Resolution | Charter consequence |
| --- | --- | --- |
| `WLA01-RD-001` | `WOLF15_CANONICAL_TARGET_AUTHENTICATED` | WOLF15 owns the schema; authorized base and completion commit are bound in section 3; HYBRID remains `NONE`. |
| `WLA01-RD-002` | `UUIDV5_CLOSED_LOGICAL_IDENTITY_V1` | Stable identity uses the exact namespace and tuple in section 5.2; deployment is provenance, not logical identity. |
| `WLA01-RD-003` | `EVENT_OWNED_SOURCE_TEMPORAL_PROFILE_V1` | Source envelopes carry only source-owned clocks; future Journal and derived clocks are forbidden in these events. |
| `WLA01-RD-004` | `RFC8785_JCS_UTF8_SHA256_V1` | Payload and envelope hashes use the non-self-referential projections in section 6. |
| `WLA01-RD-005` | `TWO_EVENT_CLOSED_REGISTRY_V1` | Only the two source event families and their mapped payload unions in section 5.8 are recognized. |
| `WLA01-RD-006` | `SOURCE_OUTCOME_EVIDENCE_UNION_V1` | Fill, partial fill, reject, cancel, and approved horizon evidence remain source facts; command intent and price touch are insufficient. |
| `WLA01-RD-007` | `FINITE_CONTRACT_LIMITS_V1` | Exact byte, reference, batch, query-span, and retry ceilings are fixed in section 7. |
| `WLA01-RD-008` | `HONEST_UNKNOWN_QUARANTINE_V1` | A source envelope with a missing revision is rejected; uncertain clocks are quarantined when honestly declared; neither becomes learning-eligible. |

This reference cannot reopen or amend a decision. Any change requires a
versioned, authenticated decision in the canonical WOLF15 repository.

## 5. `AlphaLearningEnvelopeV1` schema reference

```text
REFERENCE_CLASSIFICATION = NON_NORMATIVE_REFERENCE
CANONICAL_SCHEMA_OWNER   = WOLF15
```

All capitalized requirements in this section describe the referenced WOLF15
contract behavior. They do not create implementation authority or schema
ownership in HYBRID.

### 5.1 Closed object and primitive rules

The envelope is one frozen JSON object with these required top-level members in
the data model:

```text
contract, identity, causality, stream, source, time, authority,
safety, integrity, quality, trace, payload
```

Every object is closed: unknown fields fail validation. Required fields cannot
be omitted. Optional fields are omitted when absent; JSON `null` is forbidden.
Booleans are JSON booleans. Structural counts are base-10 JSON integers.
Market, price, and quantity values are strings matching
`^-?(0|[1-9][0-9]*)(\.[0-9]+)?$`; exponent notation, leading plus signs,
trailing decimal points, NaN, and infinities are forbidden.

All identifiers and enums are case-sensitive. Hashes use
`sha256:<64-lowercase-hex>`. UUIDs use lowercase RFC 4122 text. Timestamps use
UTC RFC 3339 form `YYYY-MM-DDTHH:MM:SS.ffffffZ` with exactly six fractional
digits. Unicode strings must be valid Unicode scalar values; lone surrogates are
rejected.

### 5.2 Contract and identity

| Path | Type and rule |
| --- | --- |
| `contract.envelope_version` | Literal `alpha-learning-envelope.v1` |
| `contract.event_name` | Closed enum of the two section 2 event names |
| `contract.event_version` | Integer literal `1` |
| `contract.schema_id` | Event-mapped literal `wolf15.alpha-fact.v1` or `wolf15.outcome-evidence.v1` |
| `identity.event_id` | UUIDv5 derived below; supplied value MUST match recomputation |
| `identity.logical_event_key` | 1-256 ASCII characters matching `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$` |

The fixed UUID namespace is
`d67ae630-3c5f-55ad-b726-66108bd53cc7`, derived as UUIDv5 of URL namespace and
the UTF-8 name `urn:wolf15:wla:alpha-learning-envelope:v1`.

The UUIDv5 name is the UTF-8 encoding of this five-part tuple with literal LF
(`0x0a`) separators and no terminal LF:

```text
contract.event_name
contract.event_version as ASCII decimal
source.system
source.service
identity.logical_event_key
```

The values cannot contain CR or LF. `source.deployment_id`, stream position, and
timestamps are excluded so an identical logical retry across producer restarts
retains its identity. Same ID plus same canonical content is a duplicate; same
ID plus different canonical content is an integrity conflict. A correction is a
new event ID linked through `quality.corrects_event_id` or
`quality.supersedes_event_id`, never an overwrite.

A retry after restart MUST replay the originally serialized bytes and original
deployment provenance. Rebuilding the event with a new deployment ID under the
same logical key is same-ID/different-content and therefore a conflict, not a
valid retry.

### 5.3 Causality and stream

| Path | Type and rule |
| --- | --- |
| `causality.correlation_id` | Required UUID |
| `causality.causation_id` | Optional UUID; omitted for a root event |
| `causality.direct_source_refs` | Sorted unique array of 1-16 `SourceRefV1` objects |
| `causality.ancestry_manifest` | Optional single `AncestryManifestRefV1`; required instead of extra inline refs |
| `stream.stream_id` | 1-160 ASCII characters using the logical-key pattern |
| `stream.ordering_scope` | Literal `SOURCE_SERVICE_STREAM` |
| `stream.sequence` | Integer from 1 through 9,007,199,254,740,991 (the I-JSON exact-integer ceiling) |
| `stream.previous_sequence` | Omitted at sequence 1; otherwise exactly `sequence - 1` |
| `stream.previous_envelope_hash` | Omitted at sequence 1; otherwise required and hash-shaped |

`SourceRefV1` is the closed object `{ref_type, ref_id, ref_hash}`. `ref_type` is
one of `WOLF15_SOURCE_RECORD`, `WOLF15_POLICY`, or `WOLF15_EVIDENCE`; `ref_id` is
1-256 characters; `ref_hash` is hash-shaped. References are sorted by
`ref_type`, then `ref_id`, then `ref_hash`, using Unicode code-point order.

`AncestryManifestRefV1` is the closed object `{manifest_id, manifest_hash,
first_ref_id, last_ref_id, ref_count}`. Its IDs use the same 1-256 character
bound, its hash is hash-shaped, and `ref_count` is 17 through 10,000,000. The
manifest is evidence by reference only; WLA-01 authorizes no storage or fetch.

### 5.4 Source and time

| Path | Type and rule |
| --- | --- |
| `source.system` | Literal `WOLF15` |
| `source.service` | 1-160 ASCII characters matching `^[A-Za-z0-9][A-Za-z0-9._-]{0,159}$` |
| `source.code_revision` | Exactly 40 lowercase hexadecimal characters |
| `source.deployment_id` | 1-200 printable non-control characters |
| `source.source_schema_version` | 1-100 ASCII version characters |
| `source.policy_version` | 1-100 ASCII version characters |
| `source.config_hash` | Hash-shaped digest of the non-secret effective configuration |
| `time.profile` | Literal `WOLF15_SOURCE_V1` |
| `time.occurred_at_utc` | Required canonical UTC timestamp |
| `time.observed_at_utc` | Required canonical UTC timestamp |
| `time.source_published_at_utc` | Required canonical UTC timestamp |
| `time.precision` | `MICROSECOND`, `MILLISECOND`, `SECOND`, or `SOURCE_DECLARED_COARSER` |
| `time.clock_health` | `SYNCHRONIZED`, `DEGRADED`, or `UNKNOWN` |
| `time.uncertainty_ms` | Integer 0-86,400,000 |
| `time.inversion_reason` | Optional 1-160 character closed reason code; never free-form authority |

The normal order is `occurred <= observed <= source_published`. An unexplained
inversion is rejected. A declared inversion, `DEGRADED`/`UNKNOWN` clock health,
or non-zero uncertainty is preserved only with `quality.status=QUARANTINED` and
a matching reason code. Source events MUST NOT carry `first_received_at_utc`,
`ingested_at_utc`, `learning_available_at_utc`, maturity, seal, or invalidation
times. Those are owned by future consumer/derived events and cannot be guessed,
backdated, or added to the source envelope.

### 5.5 Authority and safety invariants

| Path | Type and rule |
| --- | --- |
| `authority.source_authority` | Event-mapped literal `WOLF15_CANONICAL_ALPHA` or `WOLF15_SOURCE_OUTCOME_EVIDENCE` |
| `authority.source_interaction_authority` | Literal `OBSERVATIONAL_ONLY` |
| `authority.wla_decision_authority` | Literal `NONE` |
| `authority.wla_gate_authority` | Literal `NONE` |
| `safety.can_mutate_source` | Literal `false` |
| `safety.can_issue_verdict` | Literal `false` |
| `safety.can_execute` | Literal `false` |
| `safety.can_self_promote` | Literal `false` |

The fields are invariants, not feature flags. They must be present and false;
payloads may not shadow or override them. Any command-, order-, sizing-, stop-,
target-, broker-call-, repository-mutation-, deployment-, or promotion-shaped
authority field is forbidden anywhere in the envelope.

### 5.6 Integrity, quality, and trace

| Path | Type and rule |
| --- | --- |
| `integrity.hash_algorithm` | Literal `SHA-256` |
| `integrity.canonicalization_version` | Literal `RFC8785-JCS-UTF8-V1` |
| `integrity.payload_hash` | Hash-shaped; MUST match section 6.2 |
| `integrity.envelope_hash` | Hash-shaped; MUST match section 6.3 |
| `quality.status` | `VALID`, `QUARANTINED`, `UNKNOWN`, `NOT_MEASURED`, `SUPERSEDED`, or `INVALIDATED` |
| `quality.reason_codes` | Sorted unique array of 0-16 codes, each 1-160 ASCII characters |
| `quality.missing_fields` | Sorted unique array of 0-16 JSON Pointer strings |
| `quality.corrects_event_id` | Optional UUID; mutually exclusive with the next two references |
| `quality.supersedes_event_id` | Optional UUID; mutually exclusive with the other two references |
| `quality.invalidates_event_id` | Optional UUID; mutually exclusive with the other two references |
| `trace.producer_run_id` | Required UUID |
| `trace.replay_refs` | Required empty array in both WLA-01 source events |
| `trace.dataset_refs` | Required empty array in both WLA-01 source events |
| `trace.model_refs` | Required empty array in both WLA-01 source events |
| `trace.manifest_refs` | Sorted unique array of 0-4 hash-shaped references |

`VALID` requires empty `reason_codes` and `missing_fields`, synchronized clocks,
zero uncertainty, an available code revision, and no correction/invalidation
reference. Any correction reference requires a non-`VALID` status and a reason.
Only the source owner may emit source correction, supersession, or invalidation.
`UNKNOWN` and `NOT_MEASURED` remain literal states and are never coerced to
zero, false, loss, success, eligibility, or `VALID`.

### 5.7 Payload wrapper and registry mapping

`payload` is the closed object `{payload_type, payload_version, body}`.
`payload_version` is the literal `1.0`. The registry is exact:

| Event name | Schema ID | Source authority | Payload type |
| --- | --- | --- | --- |
| `wolf15.alpha-fact.exported.v1` | `wolf15.alpha-fact.v1` | `WOLF15_CANONICAL_ALPHA` | `AlphaFactPayloadV1` |
| `wolf15.outcome-evidence.exported.v1` | `wolf15.outcome-evidence.v1` | `WOLF15_SOURCE_OUTCOME_EVIDENCE` | `OutcomeEvidencePayloadV1` |

Any cross-row combination, unknown name/type/version, known-but-unregistered WLA
event, or arbitrary dictionary body is rejected. Minor-version guessing and
aliases are forbidden. A new subtype requires a reviewed contract version.

### 5.8 Typed payload unions

`AlphaFactPayloadV1.body` is a discriminated union on `fact_type`. Its initial
allowlist is grounded in the pinned PR-W1 prior art and excludes execution
command state:

| `fact_type` | Required closed source body |
| --- | --- |
| `PAIR_ADMISSION_EVALUATION_V3_1` | `symbol`, `raw_block_id`, `evaluation_id`, `coverage_status`, `decision`, optional `reason_code`, `rule_version`, optional `evaluated_at_utc`, `source_event_range`, sorted unique `source_event_ids`, and `execution_authority=false` |
| `STRATEGY_ANALYSIS_ADMISSION_V1` | `analysis_admission_id`, optional `strategy_lifecycle_id`, `authority_scope_id`, `symbol`, `admission_class`, `decision`, optional `reason_code`, `rule_version`, `admitted_at_utc`, optional `next_required_stage`, sorted unique `source_event_ids`, and `execution_authority=false` |
| `ANALYSIS_LIFECYCLE_TRANSITION_V1` | `strategy_lifecycle_id`, `symbol`, optional `previous_state`, `new_state`, `reason_code`, `transition_time_utc`, sorted unique `source_event_ids`, and `execution_authority=false` |
| `CONTEXT_EPOCH_TRANSITION_V1` | optional `context_epoch_id`, `strategy_lifecycle_id`, optional `previous_epoch_id`, `material_context_hash`, `direction_domain`, sorted unique `route`, optional `target_map_version`, `transition_reason`, `transition_time_utc`, sorted unique `source_event_ids`, and `execution_authority=false` |
| `CANONICAL_DECISION_REASON_V1` | `decision_id`, optional `strategy_lifecycle_id`, `authority_scope_id`, `stage`, source-owned `decision`, `reason_code`, ordered unique `reason_codes`, optional `next_required_stage`, sorted unique `evidence_refs`, `decided_at_utc`, and `execution_authority=false` |
| `RISK_STATE_MIRROR_V1` | `risk_state_id`, source-owned `state`, mirrored `valid_for_execution`, mirrored `risk_authority`, and `observed_at_utc` |
| `FINAL_SIGNAL_STATE_MIRROR_V1` | `final_signal_id`, source-owned `state`, mirrored `direction` (`BUY`, `SELL`, or `WAIT`), mirrored `valid_for_execution`, and `observed_at_utc` |

For these seven subtypes, JSON primitive types, enum members, regexes, field
bounds, timestamp normalization, collection ordering, and coherence validators
are reproduced as a non-normative research reference from
`contracts/observer_telemetry_export_v1.py` at WOLF15 prior-art revision
`7ff2a9194b22e185b35dc61574c61628ba404939`, file SHA-256
`787f3e2219a9778a4bcff21428c59be3d517d96ee0cac40a5c511a4d580dd672`.
This is a historical contract evidence pin, not a HYBRID code target, import
authorization, or permission to modify/reuse the frozen branch. The completed
WOLF15 contract is authoritative.

Mirrored `valid_for_execution`, `risk_authority`, direction, or decision values
describe the WOLF15 source record only. They never change the envelope's four
safety invariants or transfer capability to WLA. Every nested subtype is closed;
its bounds and coherence rules are summarized from the pinned contract. This
reference cannot tighten, relax, alias, or reinterpret the WOLF15 wire contract.

`OutcomeEvidencePayloadV1.body` is a discriminated union on `evidence_type`:

| `evidence_type` | Required closed source body and invariants |
| --- | --- |
| `FILL` | `fill_id`, `source_execution_ref`, `symbol`, `side`, positive `filled_quantity`, positive `average_fill_price`, `evidence_at_utc`, `finality=FINAL`, and 1-16 source evidence refs |
| `PARTIAL_FILL` | `fill_id`, `source_execution_ref`, `symbol`, `side`, positive `ordered_quantity`, positive `filled_quantity` strictly below ordered quantity, `average_fill_price`, `remaining_disposition` (`OPEN`, `CANCELLED`, `REJECTED`, or `EXPIRED`), `evidence_at_utc`, `finality` (`PROVISIONAL` only when open, otherwise `FINAL`), and 1-16 source evidence refs |
| `REJECT` | `rejection_id`, `source_request_ref`, `symbol`, `reason_code`, `evidence_at_utc`, `finality=FINAL`, and 1-16 source evidence refs |
| `CANCEL` | `cancellation_id`, `source_order_ref`, `symbol`, positive `cancelled_quantity`, `reason_code`, `evidence_at_utc`, `finality=FINAL`, and 1-16 source evidence refs |
| `HORIZON_OBSERVATION` | `subject_ref`, `horizon_policy_ref`, `horizon_start_utc`, `horizon_end_utc`, `horizon_state` (`MATURED`, `CENSORED`, or `UNKNOWN`), `evidence_document_ref`, `evidence_document_hash`, `evidence_at_utc`, matching finality (`FINAL`, `CENSORED`, or `UNKNOWN`), and 1-16 source evidence refs |

Unless a row is narrower, IDs and references use the 1-256 character logical-key
alphabet, `symbol` matches `^[A-Z0-9._-]{3,32}$`, reason codes are 1-160 ASCII
characters, timestamps follow section 5.1, and source evidence refs are
`SourceRefV1`. Positive decimal strings must be numerically greater than zero
after exact decimal parsing; binary floating-point comparison is forbidden.

`side` is mirrored source provenance (`BUY` or `SELL`), not an instruction.
Outcome Evidence is eligible only when emitted by the approved source owner and
backed by its source evidence references. Execution-command intent, requested
state, WLA inference, and price touch alone cannot produce `FILL` or
`PARTIAL_FILL`. `CENSORED`, `UNKNOWN`, and provisional partial fills cannot be
silently mapped to a negative class, loss, or zero return.

## 6. Canonical serialization and hashing

### 6.1 Canonical bytes

`RFC8785-JCS-UTF8-V1` means RFC 8785 JSON Canonicalization Scheme output encoded
as UTF-8 with no BOM, no trailing newline, and no surrounding framing bytes.
Object member order in source text is irrelevant; canonical output uses JCS
ordering. Arrays retain their semantically validated order. Duplicate JSON keys,
invalid Unicode, non-I-JSON numbers, NaN, infinity, comments, and trailing data
are rejected before hashing.

### 6.2 Payload hash

Define `payload_projection` as the complete validated `payload` object containing
`payload_type`, `payload_version`, and `body`. Then:

```text
payload_hash = "sha256:" + lowercase_hex(
  SHA256(JCS_UTF8(payload_projection))
)
```

The supplied `integrity.payload_hash` MUST equal the recomputed value.

### 6.3 Envelope hash

Define `envelope_hash_projection` as the complete validated envelope after
inserting the recomputed `integrity.payload_hash`, with exactly the
`integrity.envelope_hash` member omitted. No other member is omitted or nulled.
Then:

```text
envelope_hash = "sha256:" + lowercase_hex(
  SHA256(JCS_UTF8(envelope_hash_projection))
)
```

The supplied `integrity.envelope_hash` MUST equal the recomputed value. The full
wire bytes are JCS UTF-8 of the complete envelope including both hashes. A stream
predecessor points to the preceding full envelope's recomputed envelope hash.
Consumers may not reserialize a different model, normalize strings, change
decimal scale, or omit optional members differently and call those bytes
canonical.

## 7. Finite limits and fail-closed disposition

| Limit | Value | Violation disposition |
| --- | ---: | --- |
| Complete canonical envelope | 262,144 bytes | `REJECT` |
| Canonical `payload` object | 131,072 bytes | `REJECT` |
| Direct source references | 16 | Use one sealed ancestry manifest or `REJECT` |
| Ancestry manifest represented refs | 10,000,000 | `REJECT` |
| String limit when no narrower field limit exists | 500 UTF-8 bytes | `REJECT` |
| Reason or missing-field codes | 16 each | `REJECT` |
| Envelopes in a pure contract batch | 100 | `REJECT` |
| Declared query span for future conformance fixtures | 86,400 seconds | `REJECT`; no query runtime is authorized |
| Identical-delivery retries represented by one test case | 8 | Ninth attempt is a policy failure; no scheduler is authorized |

Disposition vocabulary for fixtures is closed:

- `ACCEPT_ELIGIBLE`: schema, identity, order, provenance, hash, authority,
  safety, and quality requirements all pass;
- `ACCEPT_QUARANTINED`: bytes are structurally honest and preserved for evidence,
  but missing/uncertain source evidence denies learning eligibility; and
- `REJECT`: bytes cannot be admitted as an `AlphaLearningEnvelopeV1` event.

Missing or malformed source revision is `REJECT`. A truthful unavailable
revision represented by an external transport receipt may be
`ACCEPT_QUARANTINED`, but that receipt is not one of the two WLA-01 source event
schemas and cannot be relabeled as a valid source envelope. Degraded/unknown
clock health is `ACCEPT_QUARANTINED` only when declared as specified in section
5.4; otherwise it is `REJECT`.

## 8. Golden-fixture reference cases

```text
REFERENCE_CLASSIFICATION = NON_NORMATIVE_REFERENCE
CANONICAL_SCHEMA_OWNER   = WOLF15
REFERENCE_CASE_COUNT     = 22
```

The 7 positive, 2 quarantine, and 13 negative cases below are non-normative
traceability summaries. Their executable fixtures and acceptance evidence are
owned by WOLF15. HYBRID must not reproduce or reinterpret them as a second
canonical corpus.

### 8.1 Positive and quarantine fixtures

| ID | Required case | Acceptance criteria |
| --- | --- | --- |
| `WLA01-FX-P01` | Canonical Alpha Fact | One allowlisted subtype returns `ACCEPT_ELIGIBLE`; exact canonical bytes, UUIDv5, payload hash, and envelope hash match the golden values. |
| `WLA01-FX-P02` | All Alpha Fact subtypes | One fixture per seven allowlisted subtypes validates its closed nested schema and authority mapping. |
| `WLA01-FX-P03` | Outcome variants | Fill, partial-open, partial-final, reject, cancel, matured horizon, censored horizon, and unknown horizon fixtures preserve their exact finality semantics. |
| `WLA01-FX-P04` | Identical retry | Eight deliveries produce one event identity and identical hashes; no duplicate artifact is implied. |
| `WLA01-FX-P05` | Two-event chain | Sequence 1 has no predecessor; sequence 2 points to sequence 1 and validates contiguously. |
| `WLA01-FX-P06` | Correction | A new event ID links to the old ID; the old bytes and hashes remain unchanged. |
| `WLA01-FX-P07` | Bounded ancestry | A 16-ref event validates inline; a 17-ref event validates only with a coherent sealed manifest reference. |
| `WLA01-FX-Q01` | Declared uncertain clock | Honest `DEGRADED` or `UNKNOWN` clock metadata plus reasons returns `ACCEPT_QUARANTINED`, never eligible. |
| `WLA01-FX-Q02` | Honest unknown quality | `UNKNOWN`/`NOT_MEASURED` remains literal and cannot yield a numeric/default label or readiness result. |

### 8.2 Negative fixtures

Every fixture below MUST return `REJECT`, emit no canonical eligible event, and
perform no network, storage, callback, or WOLF15 write:

| ID | Required rejection |
| --- | --- |
| `WLA01-FX-N01` | Extra field at every object level, duplicate JSON key, omitted required field, or forbidden `null`. |
| `WLA01-FX-N02` | Unknown event name, unknown major/minor version, unregistered payload, or event/schema/payload/authority mismatch. |
| `WLA01-FX-N03` | Wrong UUID namespace or tuple, same ID with different content, malformed UUID, or CR/LF identity injection. |
| `WLA01-FX-N04` | Payload-hash mismatch, envelope-hash mismatch, uppercase/malformed hash, alternate canonicalization, NaN, infinity, or invalid Unicode. |
| `WLA01-FX-N05` | Any safety invariant true, omitted, shadowed by a payload, or accompanied by command/verdict/execution/repository/deployment/promotion authority. |
| `WLA01-FX-N06` | Naive/non-UTC timestamp, wrong precision form, unexplained inversion, or fabricated ingress/learning-availability time in a source event. |
| `WLA01-FX-N07` | Sequence gap, fork, wrong predecessor sequence/hash, undeclared reset, or cross-stream predecessor. |
| `WLA01-FX-N08` | Oversized envelope/payload/string, 17 inline refs without a manifest, unordered/duplicate refs, invalid manifest root/range/count, or over-limit batch/query/retry case. |
| `WLA01-FX-N09` | Missing/malformed revision, config hash, deployment identity, source evidence, or an attempt to convert unavailable evidence to `VALID`. |
| `WLA01-FX-N10` | Fill/partial-fill derived only from price touch, command intent, WLA inference, or evidence owned by an unapproved producer. |
| `WLA01-FX-N11` | Invalid partial quantity/finality combination, horizon end before start, or censored/unknown outcome coerced to a final numeric label. |
| `WLA01-FX-N12` | Source/derived authority relabeling, unknown authority class, WLA gate authority, human-gate payload, or source correction emitted by WLA. |
| `WLA01-FX-N13` | Attempted outbox consumer/cursor, callback, repair request, acknowledgement dependency, storage write, repository creation, broker/EA call, or WLA-to-WOLF15 write in the reference harness. |

Negative harness checks MUST fail before an external request is attempted. Pure
contract tests may use in-memory values only; even temporary persistence is not
part of WLA-01 acceptance.

### 8.3 Decision-to-fixture traceability

| Decision | Primary fixture evidence |
| --- | --- |
| `WLA01-RD-001` | `WLA01-VC-004`; WOLF15 is the canonical target and HYBRID remains documentation-only |
| `WLA01-RD-002` | `P01`, `P04`, `P06`, `N03` |
| `WLA01-RD-003` | `Q01`, `N06` |
| `WLA01-RD-004` | `P01`, `P04`, `P05`, `N04`, `N07` |
| `WLA01-RD-005` | `P02`, `P03`, `N01`, `N02`, `N12` |
| `WLA01-RD-006` | `P03`, `Q02`, `N10`, `N11` |
| `WLA01-RD-007` | `P07`, `N08` |
| `WLA01-RD-008` | `Q01`, `Q02`, `N06`, `N09`, `N11` |

Short fixture IDs in this table refer to the `WLA01-FX-*` IDs in sections 8.1
and 8.2. Canonical fixture evidence and exact revisions are recorded in WOLF15,
not created by this reference.

## 9. Traceable verification checklist

| Check ID | Requirement / authority | Evidence required | Current result |
| --- | --- | --- | --- |
| `WLA01-VC-001` | Signed WLA-00 decision | Decision ID, ratification ID, verified commit, reviewed digest, and `CONTRACT_ONLY` ceiling match section 1 | `PASS` by repository evidence |
| `WLA01-VC-002` | Preserve ratified scope | The 19 normative and 38 supporting files reproduce their signed digests; this research file is explicitly excluded; packet and receipt remain byte-identical | `PASS` required at each reference revision |
| `WLA01-VC-003` | Eight WLA01-RD decisions | Exactly `WLA01-RD-001` through `WLA01-RD-008` appear once as non-normative traceability records | `PASS` by document inspection |
| `WLA01-VC-004` | Single canonical target | Section 3 binds WOLF15 as canonical target and sets `HYBRID_CODE_TARGET=NONE` | `PASS` by reference reconciliation |
| `WLA01-VC-005` | Closed schema reference | Section 5 is explicitly `NON_NORMATIVE_REFERENCE` with `CANONICAL_SCHEMA_OWNER=WOLF15` | `PASS` by document inspection; canonical evidence belongs to WOLF15 |
| `WLA01-VC-006` | Deterministic bytes and hashes | Sections 6.1-6.3 remain a non-normative description; canonical implementation evidence belongs to WOLF15 | `PASS` as reference classification |
| `WLA01-VC-007` | Fixture reference | `P01-P07`, `Q01-Q02`, and `N01-N13` are labeled as 22 non-normative cases owned by WOLF15 | `PASS` by document inspection |
| `WLA01-VC-008` | Runtime/storage/outbox/repository prohibition | Sections 2 and 8.2 explicitly deny runtime, storage, outbox consumers, repository creation, and reverse writes | `PASS` by reference review |
| `WLA01-VC-009` | Documentation-only diff | Repository diff contains this reference only and no runtime, workflow, schema-code, fixture, test, or storage artifact | `PASS` required before handoff |
| `WLA01-VC-010` | Runtime evidence boundary | Runtime, database, network, deployment, broker, EA, and production state are not inferred from documentation | `NOT_EXECUTED` / `NOT_MEASURED` |
| `WLA01-VC-011` | WLA-01 completion | WOLF15 completion commit is `22ee9774930d2bf5d09a32851098a8dba8918167` | `PASS`; cross-repo binding remains pending until final verification |
| `WLA01-VC-012` | Later-stage isolation | WLA-02 is published at receipt commit `247075035bc0d69c7122d15313db01cb65f6249f`; WLA-03 remains unauthorized; Gate P0-A is not evaluated; learning repository is not created | `PASS` by status reconciliation |

This HYBRID reference proves only documentation reconciliation. WOLF15 commits
and receipts are the evidence for WLA-01 and WLA-02 implementation. Runtime,
database, network, deployment, broker, EA, and production state remain separate
evidence classes and are not inferred here.

## 10. Exit and change control

WLA-01 and WLA-02 are complete in the canonical WOLF15 evidence history. This
HYBRID reference does not reopen either stage and cannot authorize a later one.

```text
HYBRID_REFERENCE_VERIFICATION = REQUIRED_BEFORE_COMMIT
WLA_03_AUTHORIZED             = FALSE
NEXT_PROGRAM_GATE             = HUMAN_RATIFICATION_WLA_03
GATE_P0_A                     = NOT_EVALUATED
RUNTIME_MUTATION              = NONE
```

Any future update must keep the WOLF15 ownership binding explicit, preserve all
signed historical artifacts byte-for-byte, recompute this excluded file's
SHA-256 independently, and obtain new authority before WLA-03, runtime, outbox,
database, deployment, repository creation, or production work.
