---
id: ADR-002
title: Staged topology and repository sequencing
status: PROPOSED
date: 2026-08-24
---

# ADR-002: Staged topology and repository sequencing

## Context

Creating Journal, Orchestrator, Domain Knowledge, and Adaptive Memory at once
would establish interfaces and authority before the evidence model is stable. It
would also make unused repositories look operational.

## Decision

The mandatory work order is:

```text
WLA-00 -> WLA-01 -> WLA-02 -> WLA-03 -> Gate P0-A
```

Only a recorded `PASS` at Gate P0-A makes `wolf15-learning-journal` eligible for
creation. `PASS` is a human governance decision backed by evidence; it is not an
automated state transition.

Later capabilities are introduced one at a time:

1. **Journal** proves append-only ingestion, lineage, correction, query, and
   retention semantics.
2. **Orchestrator** becomes eligible only when repeated journal workflows require
   coordination and can run with no source or execution credentials.
3. **Domain Knowledge** becomes eligible only when curated, reviewable knowledge
   artifacts exist and automatic promotion is impossible.
4. **Adaptive Memory** becomes eligible only when retrieval/index behavior is
   rebuildable, non-authoritative, and cannot silently alter datasets or Alpha.

Repository creation is not a milestone by itself. Each repository needs a
charter, owner, authority ceiling, threat boundary, data classification, SLOs,
retention policy, and exit/rollback plan before creation.

WLA-01 has a bounded constitutional minimum: the typed
`AlphaLearningEnvelopeV1` contract, canonical serialization/version policy, and
positive/negative fixtures, with no runtime activation. Its complete charter and
the detailed charters for WLA-02/03 must be accepted separately and must not
weaken any WLA-00 invariant.

## Consequences

- Parallel research is allowed; parallel claims of completion are not.
- No empty repositories, placeholder services, or credentials are created to
  “reserve” the architecture.
- The program can stop safely after any stage without a half-authorized mesh.

## Rejected alternatives

- **Create all four repositories now.** Rejected due to premature coupling and
  authority ambiguity.
- **Use one legacy quad-repo loop as a shortcut.** Rejected because its roles and
  mutation semantics conflict with WLA.
- **Skip P0-A for documentation-only changes.** Rejected because P0-A is the
  boundary before the first persistent learning repository exists.

## WLA-00 acceptance

- The stage ledger has one state per stage: `NOT_STARTED`, `IN_PROGRESS`,
  `BLOCKED`, `PASS`, or `FAIL`.
- No later-stage `PASS` exists without all earlier `PASS` receipts.
- Repository eligibility requirements are included in Gate P0-A evidence.

At WLA-00 acceptance, WLA-01/02/03 and P0-A remain `NOT_STARTED`; their future
receipts are conformance obligations, not prerequisites for this ADR.

## Downstream conformance obligations

- WLA-01 publishes its complete contract/fixture charter before implementation.
- WLA-02 and WLA-03 publish bounded charters before work is claimed complete.
- Gate P0-A rejects missing or out-of-order stage receipts, and repository
  creation remains `NOT_CREATED` until its explicit `PASS`.
