---
id: ADR-009
title: Human gates, SHADOW ceiling, and fail-closed rollout
status: PROPOSED
date: 2026-08-24
---

# ADR-009: Human gates, SHADOW ceiling, and fail-closed rollout

## Context

The learning pipeline needs autonomy for evidence processing while preventing a
good score, scheduled job, agent instruction, or model output from becoming an
implicit promotion decision.

## Decision

Every program, repository, authority-ceiling, deployment-mode, or policy-version
transition uses a signed human gate record with:

- gate ID and policy version;
- exact artifact/revision/digest set reviewed;
- required checks and their evidence classes;
- explicit `PASS` or `FAIL` (never inferred from missing checks);
- named approvers and separation-of-duties proof;
- decision time, reason, conditions, and expiry where applicable; and
- rollback/disable procedure and residual risks.

`BLOCKED`, `UNKNOWN`, `NOT_MEASURED`, expired evidence, stale approvals, missing
approvers, or skipped checks are not `PASS`.

For bootstrap WLA-00 only, `WLA00-EXC-001` may record one authenticated system
and repository owner assuming `ARO`, `WAO`, `JDS`, `MRR`, and `SEC`. The record
MUST say that independent concurrence and backups are unavailable, bind one
cryptographic owner attestation to the complete ratification tuple, and limit
authorization to the WLA-01 contract-only spike. The exception expires at WLA-01
completion or scope expansion, is non-reusable, and grants no runtime,
database/outbox, broker/EA, deployment, production/advisory, repository-creation,
or Gate P0-A authority.

Within an already human-ratified policy and fixed authority ceiling, the artifact
pipeline from Fact through Challenger and SHADOW MAY run autonomously. Each
artifact transition requires a machine-verifiable eligibility receipt, not a new
human signature. That receipt can prove policy conformance only; it cannot change
policy, create a repository, expand credentials/egress, select itself as Alpha,
or authorize a mode beyond SHADOW.

Gate P0-A controls only eligibility to create `wolf15-learning-journal`. It does
not approve Orchestrator, Domain Knowledge, Adaptive Memory, a model, SHADOW, or
production use.

SHADOW is the maximum autonomous operating mode. A SHADOW process:

- consumes a mirrored, observational stream under a human-ratified SHADOW policy;
- writes only to learning-owned evidence stores;
- has no broker/EA, order, verdict, risk, WOLF15 mutation, merge, or deployment
  credentials;
- cannot influence routing, sizing, alerts used as trade instructions, or Alpha;
- is killable independently of WOLF15; and
- remains safe if delayed, duplicated, compromised, or unavailable.

WLA-00 authorizes no transition beyond SHADOW. Any future request requires a new
constitution-level ADR and explicit human decision; it cannot be implied by this
document.

## Consequences

- Autonomous learning can continue producing evidence without acquiring control.
- A gate failure preserves prior safe state and records the failure.
- Rollback means disable/isolate and select an earlier accepted artifact; it does
  not delete evidence or replay an old trade decision.

## Rejected alternatives

- **Threshold-based auto-promotion.** Rejected because metrics can be incomplete,
  leaked, or optimized. Automated eligibility inside a fixed SHADOW policy is
  permitted because it grants no new authority.
- **Treat SHADOW as a timed probation before production.** Rejected; time creates
  evidence, not authority.
- **Fail open when the gate service is unavailable.** Rejected because absence of
  approval cannot grant permission.

## WLA-00 acceptance

- Reviewers accept the distinction between human authority/policy gates and
  automated artifact eligibility.
- The SHADOW ceiling and every fail-closed state are explicit and traceable.

## Downstream conformance obligations

The following are `NOT_EXECUTED` during WLA-00:

- Gate fixtures prove every non-`PASS` state blocks progression.
- Shadow threat tests prove absence of prohibited credentials and egress.
- Kill/disable tests leave WOLF15 unaffected.
- No event name, API, UI, or workflow implements implicit promotion.
