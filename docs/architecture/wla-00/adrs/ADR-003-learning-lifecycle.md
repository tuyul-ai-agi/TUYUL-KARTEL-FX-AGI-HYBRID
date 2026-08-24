---
id: ADR-003
title: Canonical learning lifecycle from Fact to SHADOW
status: PROPOSED
date: 2026-08-24
---

# ADR-003: Canonical learning lifecycle from Fact to SHADOW

## Context

Terms such as log, feedback, reflection, dataset, and model are often used as if
they were interchangeable. That collapses evidence, derived interpretation, and
runtime authority into one mutable object.

## Decision

WLA adopts eight distinct artifact classes:

| Stage | Meaning | May depend on | Must never mean |
| --- | --- | --- | --- |
| Fact | Immutable WOLF15-sourced observation with provenance | Approved source export | Inferred truth or label |
| Episode | Deterministically sealed group of Fact references | Facts available by cutoff | Mutable session bag |
| Outcome | Matured learning label produced by a versioned policy from source-owned Outcome Evidence, with horizon/finality/censoring/correction and learning-availability time | Episode and authoritative later evidence | Broker truth, mutable reward, or a label guessed from future prices |
| Replay | Deterministic as-of reconstruction and its run receipt | Episode, eligible Outcome, pinned code/config | Live decision or source rewrite |
| Reflection | Cited hypothesis about evidence and replay results | Replay and evidence | Fact, policy, approval, or executable rule |
| Dataset | Sealed point-in-time materialization with lineage and splits | Eligible artifacts available by cutoff | Latest-view query result |
| Challenger | Immutable candidate artifact plus training/evaluation manifest | Sealed dataset | Champion, Alpha, or production model |
| SHADOW | Isolated observation-only evaluation of a Challenger | Approved challenger and live mirrored facts | Paper execution, control, or promotion |

The arrows express dependency and information maturity, not permission to mutate
one row through eight statuses. Artifacts remain distinct and retain immutable
links to their causes.

Not every Fact must form an Episode, not every Episode has a matured Outcome,
and not every Reflection becomes dataset input. Missing stages remain explicit.

## Consequences

- A reflection cannot overwrite the evidence it interprets.
- A challenger score cannot rewrite dataset labels.
- SHADOW output may be journaled for evaluation but cannot enter WOLF15 inputs.
- Corrections create new lineage branches and may invalidate downstream
  artifacts without erasing them.

## Rejected alternatives

- **Single mutable learning record.** Rejected because it destroys as-of history.
- **Treat every reflection as knowledge.** Rejected because narrative confidence
  is not validation.
- **Let SHADOW be an automatic pre-production state.** Rejected; SHADOW is the
  autonomous ceiling under this constitution.

Source-owned **Outcome Evidence** (for example fill, reject, cancel, or approved
market-horizon evidence) remains a Fact class with source authority. The WLA
**Outcome label** is derived and authoritative only for the exact labeling-policy
version and downstream dataset lineage. It never becomes broker/execution truth.

## WLA-00 acceptance

- The eight stages and the Outcome Evidence/Outcome label distinction are
  unambiguous and mapped to the event vocabulary.
- Reviewers confirm that no stage transition implies source mutation or approval.

## Downstream conformance obligations

The following are `NOT_EXECUTED` until their owning later stage:

- Event vocabulary defines distinct event families for all eight artifact types.
- Contracts reject illegal stage substitutions and missing lineage.
- Tests prove an incomplete or `UNKNOWN` upstream state cannot be silently
  advanced.
