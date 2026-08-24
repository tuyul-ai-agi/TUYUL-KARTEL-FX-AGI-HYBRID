---
id: ADR-005
title: Append-only evidence, corrections, invalidation, and retention
status: PROPOSED
date: 2026-08-24
---

# ADR-005: Append-only evidence, corrections, invalidation, and retention

## Context

Historical evidence can arrive late, be corrected by its owner, or later be found
invalid. In-place edits make old replays irreproducible and allow future knowledge
to leak into past datasets.

## Decision

Facts, Episodes, Outcomes, Replay receipts, Reflections, Dataset manifests,
Challenger manifests, SHADOW evaluations, and gate decisions are append-only.
Their content-addressed identity and original timestamps never change.

A correction is a new artifact emitted by the accountable owner of the artifact
being corrected. Only WOLF15/the approved source owner may correct a source Fact
or source Outcome Evidence. A WLA owner may correct only its own derived
artifact, including an Outcome label, and may never use that correction to
rewrite or reinterpret source evidence.

Every correction identifies:

- the artifact it supersedes;
- correction reason and responsible producer;
- correction occurrence and availability times;
- old and new payload hashes;
- whether downstream artifacts require invalidation or rebuild; and
- reviewer/approval evidence when the corrected field affects labels or gates.

An invalidation marks an artifact ineligible for new use. It does not erase the
artifact or rewrite prior run receipts. Rebuilds produce new IDs and manifests.

Deletion for legal, privacy, or retention reasons uses an auditable tombstone and
a redaction/erasure procedure appropriate to the data class. The system preserves
the minimum non-sensitive evidence needed to explain why a prior artifact can no
longer be reproduced. Secrets MUST never be stored in WLA events, so secret
rotation is not modeled as event correction.

Storage compaction MAY create verified projections, but the projection is never
the source ledger. Hash-chain breaks, missing predecessors, or identity/content
conflicts quarantine the affected stream and all dependent artifacts.

## Consequences

- Historical reports remain explainable after corrections.
- Dataset lineage must record the exact correction version available at cutoff.
- Retention costs are explicit rather than hidden through mutation.
- “Latest” is a query choice, never a replacement for point-in-time truth.

## Rejected alternatives

- **Update the original row.** Rejected because it destroys historical truth.
- **Delete bad runs without a trace.** Rejected because gates and model results
  would become unauditable.
- **Treat the latest payload as canonical for all time.** Rejected because it
  causes temporal leakage.

## WLA-00 acceptance

- Reviewers accept append-only correction, invalidation, and retention semantics
  and confirm that “latest” cannot rewrite historical truth.
- The rules identify ownership and downstream invalidation requirements.

## Downstream conformance obligations

The following are `NOT_EXECUTED` during WLA-00:

- WLA-01 defines correction, supersession, and invalidation references.
- The owning downstream replay stage proves old as-of replays remain stable after
  a later correction.
- Conflicting duplicates quarantine rather than overwrite.
- Retention and erasure tests preserve a non-sensitive audit receipt.
