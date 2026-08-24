---
id: ADR-008
title: Replay, dataset, and challenger reproducibility
status: PROPOSED
date: 2026-08-24
---

# ADR-008: Replay, dataset, and challenger reproducibility

## Context

A score is not auditable when the evidence snapshot, code, configuration, random
seeds, dependencies, or split rules cannot be reconstructed. Reproducibility is
also an integrity control against artifact substitution.

## Decision

Every Replay records a sealed manifest containing:

- input event/stream ranges and their integrity roots;
- as-of cutoff and source availability policy;
- code revision, dependency/environment lock, and configuration digest;
- deterministic ordering and random seeds;
- clock, timezone, and market-calendar versions;
- correction/invalidation view;
- output digest, warnings, gaps, and epistemic statuses; and
- runner identity and start/completion times.

Every Dataset records the replay manifests it derives from, the accepted dataset
specification, and any Reflection IDs that motivated that specification, plus
feature/label definitions, inclusion/exclusion reasons, split membership,
purge/embargo rules, fit artifacts, row/episode counts, class/coverage summaries,
and a content digest. It is immutable once sealed. Reflection or analysis based
on an evaluation cohort cannot become a feature, selector, label, or specification
change tested against that same sealed holdout.

Every Challenger records its dataset digest, training code/environment,
configuration, seed set, model artifact digest, evaluation protocol, metrics with
confidence/uncertainty, subgroup and regime results, failure analysis, and known
limitations. Challenger-to-challenger comparisons are valid only on compatible,
sealed evaluation protocols.

The primary metrics, threshold-selection procedure, subgroup hierarchy, stopping
rule, candidate budget, and evaluation holdout are preregistered before holdout
results are read. Every attempted Challenger and comparison remains in the run
ledger. Reusing a holdout for reflection-driven iteration invalidates it as final
evidence and requires a new out-of-time holdout.

A candidate earns the `Challenger` designation only when its preregistered
protocol compares it with the pinned canonical WOLF15 Alpha/baseline on identical
eligible evidence. Where return or trade-like outcomes are evaluated, the
protocol declares the same fees, spread, slippage, latency, censoring, and
execution-evidence rules for all comparators. Evaluation includes effectiveness,
calibration, coverage/abstention, safety/risk guardrails, uncertainty, denominators,
and regime/subgroup slices. Exact thresholds may be chosen later, but the primary
non-inferiority and safety guardrails must be fixed before holdout results are
read. A candidate lacking this comparator remains an experiment, not a
Challenger.

Two runs with the same manifest MUST produce the same semantic output or record a
`NON_DETERMINISTIC` failure. Hardware-level numeric tolerances must be declared in
advance and cannot be widened after results are seen.

## Consequences

- “Best run” without its failed siblings and protocol is insufficient evidence.
- Model files without manifests are untrusted artifacts.
- A changed dependency, label, split, or tolerance creates a new evaluation
  lineage rather than silently replacing the old one.

## Rejected alternatives

- **Track only model weights.** Rejected because weights do not explain evidence
  or evaluation.
- **Use latest dependencies/config.** Rejected because results drift.
- **Choose tolerance after comparing runs.** Rejected as outcome-driven policy.

## WLA-00 acceptance

- Reviewers accept the minimum Replay, Dataset, Challenger, preregistration, and
  holdout-sealing manifests.
- Reflection/spec lineage and multiple-comparison controls are explicit.

## Downstream conformance obligations

The following are `NOT_EXECUTED` during WLA-00:

- Repeat builds match declared digests/tolerances.
- Tampered input, manifest, or model artifacts are rejected.
- Metrics retain denominators, missingness, uncertainty, and evaluation scope.
- Failed and invalid runs remain auditable and cannot be cherry-picked away.
