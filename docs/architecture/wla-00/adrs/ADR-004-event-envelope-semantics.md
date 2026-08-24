---
id: ADR-004
title: Event identity, provenance, ordering, and integrity semantics
status: PROPOSED
date: 2026-08-24
---

# ADR-004: Event identity, provenance, ordering, and integrity semantics

## Context

Learning evidence crosses process and, eventually, repository boundaries.
Retries, late arrival, duplicate delivery, schema drift, and source deployment
changes must be distinguishable without relying on arrival order or filenames.

## Decision

Every durable WLA event contract MUST define these semantic groups, even if the
future wire format names them differently:

- **identity:** event ID, event name/version, logical event key;
- **causality:** correlation ID, causation ID, bounded direct source references,
  and sealed manifest/range plus integrity-root references for large ancestry;
- **stream:** stable stream ID, monotonic sequence, predecessor identity/hash;
- **source:** system, service, immutable code revision, deployment ID, policy and
  schema versions;
- **time:** occurred, observed, source-published, first-received, ingested, and
  learning-available times in UTC;
- **authority:** source authority class and learning-plane authority ceiling;
- **integrity:** canonical payload hash and, where ordered, envelope/chain hash;
- **quality:** explicit valid, quarantined, unknown, not measured, corrected, or
  invalid state; and
- **safety:** source mutation and execution capabilities fixed to false for
  learning consumers.

Event IDs are stable for one logical source event. A retry with identical content
is idempotent. The same identity with different content is an integrity conflict,
not an update. Unknown fields, versions, authority classes, time zones, NaN, or
non-canonical encodings fail closed.

Ordering is guaranteed only within a declared stream. Cross-stream order is
derived from time and causality with uncertainty preserved; it is never inferred
from ingestion sequence alone.

Contracts set hard bounds on payload bytes, direct reference count, batch size,
query span, and retry count. Replay/Dataset/Challenger ancestry with large
cardinality lives in immutable manifests rather than unbounded envelopes.

This ADR defines semantics, not `AlphaLearningEnvelopeV1` serialization.

## Consequences

- Replays can detect gaps, forks, duplicates, and payload drift.
- A source deployment with unavailable revision is quarantined unless an
  explicitly accepted policy permits a bounded `UNKNOWN` representation.
- Consumers must support duplicate delivery without duplicate artifacts.

## Rejected alternatives

- **Use one timestamp and random UUID.** Rejected because it cannot prove
  point-in-time availability or stable idempotency.
- **Accept extra fields for forward compatibility.** Rejected for authority and
  safety contracts; version negotiation must be explicit.
- **Use repository commit time as event time.** Rejected because transport and
  market time are different evidence.

## WLA-00 acceptance

- The semantic groups, failure behavior, and version boundary are complete enough
  to constrain WLA-01 without selecting a wire format.
- Reviewers accept explicit ordering, identity, causality, time, authority, and
  integrity semantics.

## Downstream conformance obligations

The following are `NOT_EXECUTED` during WLA-00:

- WLA-01 publishes canonical serialization and deterministic hash fixtures.
- Duplicate-identical, duplicate-conflicting, gap, fork, downgrade, and unknown
  field tests fail or pass exactly as specified.
- All timestamps require an offset and normalize to UTC without losing source
  precision metadata.
