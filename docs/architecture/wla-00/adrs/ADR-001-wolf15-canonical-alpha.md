---
id: ADR-001
title: WOLF15 remains canonical Alpha
status: PROPOSED
date: 2026-08-24
---

# ADR-001: WOLF15 remains canonical Alpha

## Context

Learning requires faithful historical Alpha evidence. It does not require, and
must not acquire, ownership of Alpha generation or execution. A mirror may carry
a WOLF15 record that was valid for execution at source without becoming an
executable object in the learning plane.

## Decision

WOLF15 is the only canonical source for Alpha facts. The learning plane consumes
an approved, versioned, observational export. It never reconstructs canonical
Alpha from dashboards, legacy journals, reports, prompts, broker fills, or model
predictions.

The boundary is one way:

```text
WOLF15 canonical transaction -> approved export/outbox -> learning ingress
learning plane               -X-> WOLF15 state/config/verdict/execution
```

The future `AlphaLearningEnvelopeV1` MUST preserve source identity, source
revision/deployment, authority class, logical event identity, ordering,
timestamps, payload integrity, and the invariant that the observer cannot mutate
the source. Its exact wire schema is deferred until WLA-00 is accepted.

Learning credentials MUST be incapable of writing WOLF15 databases, queues,
configuration, repositories, verdicts, risk state, execution commands, or
broker/EA surfaces. A transport that technically supports bidirectional calls is
not acceptable unless the reverse capability is independently denied.

WLA availability, ingress latency, retries, backlog, or outage MUST NOT be a
synchronous dependency of WOLF15 analysis, risk, verdict, or execution. WLA sends
no acknowledgement that permits or blocks source processing. The durability and
failure semantics of the source-local export/outbox remain a WOLF15 governance
decision and must be explicit before implementation; remote learner health can
never determine the source transaction result. Export gaps remain visible as
`UNKNOWN`/gap evidence rather than being repaired by the learner.

## Consequences

- Source corrections originate from WOLF15 and arrive as new exported events.
- Learning may reject or quarantine malformed exports, but cannot repair WOLF15.
- An exported `valid_for_execution=true` value remains observed source data; it
  grants no learning-plane capability.
- If source provenance is unavailable, the event is quarantined as `UNKNOWN`
  rather than relabeled.

## Rejected alternatives

- **Let Journal become Alpha source-of-truth.** Rejected because a consumer must
  not overtake its producer's decision authority.
- **Infer missing Alpha from fills or price movement.** Rejected because outcome
  evidence cannot recreate a historical decision without leakage.
- **Allow a “safe” feedback callback.** Rejected until a separately governed,
  non-learning control contract exists; WLA does not authorize one.

## WLA-00 acceptance

- Reviewers accept the one-way authority and availability boundary as a complete
  normative decision with no unresolved authority-bearing placeholder.
- The decision is mapped to the support documents and WLA-00 DoD.

## Downstream conformance obligations

These are assigned to later stages and are `NOT_EXECUTED` during WLA-00; they do
not block acceptance of this ADR:

- Source-owner and security reviewers approve the one-way boundary.
- WLA-01 fixtures distinguish source execution validity from observer authority.
- The owning downstream charter proves write, callback, broker, and control-plane
  paths fail before P0-A.
- Missing or stale source evidence remains explicit and blocks downstream use.
