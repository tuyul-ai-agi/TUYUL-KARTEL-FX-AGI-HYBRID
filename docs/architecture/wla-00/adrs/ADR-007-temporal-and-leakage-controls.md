---
id: ADR-007
title: Point-in-time temporal semantics and leakage prevention
status: PROPOSED
date: 2026-08-24
---

# ADR-007: Point-in-time temporal semantics and leakage prevention

## Context

Trading data has multiple clocks: market occurrence, system observation,
publication, learner availability, label maturity, and later correction. A single
timestamp or latest-state join can give a replay information unavailable at the
historical decision time.

## Decision

Every temporal artifact records the applicable clocks defined in the temporal
rules. Eligibility is determined by
`learning_available_at_utc <= as_of_cutoff_utc`, not merely by occurrence time,
source publication time, first receipt, or current database state.

Outcome labels are separate artifacts. They become eligible only after their
declared horizon closes, the authoritative evidence is observed, accepted into
Journal, and `learning_available_at_utc` is reached. Until then the outcome is
`PENDING` or `UNKNOWN`, never zero or loss.

Replay and dataset construction use point-in-time joins. Transformations,
normalizers, vocabulary builders, imputers, selectors, and calibration are fit on
the training partition only. Time series splits are chronological and grouped by
episode/causal unit; overlapping label horizons require purge and embargo.
Random row splits are forbidden in WLA datasets. A future non-market dataset
with demonstrably independent samples would require a separately scoped
constitution and is outside this learning lifecycle.

Revised macro data, corrected candles, and late source events are versioned by
availability time. A historical replay sees only the version legally available
at its cutoff.

## Consequences

- Dataset size may be smaller because unresolved or overlapping samples are
  excluded.
- Metrics may be `NOT_MEASURED` until denominators mature.
- Reprocessing after a correction creates a new dataset version; it does not
  change old reported metrics.

## Rejected alternatives

- **Use event/market time alone.** Rejected because publication and ingestion can
  occur later.
- **Backfill outcomes into the original signal row.** Rejected because future
  labels become visible to historical queries.
- **Random train/test split by row.** Rejected because related episodes and
  overlapping horizons can cross partitions.

## WLA-00 acceptance

- Reviewers accept the multi-clock, point-in-time, maturity, and split rules as
  normative and internally consistent.
- The leakage test catalog covers future values, revisions, transforms, related
  samples, outcomes, reflections, and retrieval.

## Downstream conformance obligations

The following are `NOT_EXECUTED` during WLA-00:

- Temporal canary tests detect deliberately injected future-only features.
- Late-arrival and revision fixtures produce correct as-of views.
- Split reports prove chronology, grouping, purge, embargo, and fit scope.
- Time-zone ambiguity, naive timestamps, and clock inversions fail closed.
