---
title: WLA-00 Technical Constitution
status: PROPOSED
version: 0.1.0
date: 2026-08-24
scope: Wolf15 learning architecture before AlphaLearningEnvelopeV1 implementation
---

# WLA-00 Technical Constitution

## 1. Constitutional decision

WLA-00 establishes the technical constitution for the Wolf15 learning program.
It does not activate a learning runtime and it does not define the serialized
`AlphaLearningEnvelopeV1` contract.

The binding architecture is:

```text
WOLF15 canonical Alpha
        |
        v  approved, observational export only
Fact -> Episode -> Outcome -> Replay -> Reflection -> Dataset -> Challenger -> SHADOW
```

The learning plane may reach `Challenger` and `SHADOW`. It MUST NOT self-promote,
replace WOLF15 Alpha, issue a verdict, size a position, create an order intent,
contact a broker/EA, mutate WOLF15 state, or gain execution authority.

## 2. Status and ratification

This package is `PROPOSED`. Its design can be complete while ratification remains
pending. It becomes `ACCEPTED` only when every WLA-00 Definition of Done item is
satisfied and the required human approvers record an explicit decision. Silence,
CI success, a model score, a reflection, or the passage of time cannot ratify it.

Named role assignment, domain-review concurrence, conflicts, and the final human
decision are recorded in the
[WLA-00 ratification packet](RATIFICATION-PACKET.md). Preparing that packet does
not change the gate from `NOT_EVALUATED` and does not authorize WLA-01.

`WLA00-EXC-001` permits one explicitly authenticated constitutional owner to
ratify WLA-00 under `SINGLE_OWNER_BOOTSTRAP` without claiming independent
concurrence or backup availability. The exception authorizes only the WLA-01
contract spike, schema/contract tests, documentation, and deterministic fixtures.
It expires at WLA-01 completion or any scope expansion and cannot authorize
runtime registration, database/outbox activation, broker/EA access, deployment,
production/advisory activation, a learning repository, or Gate P0-A.

Normative terms `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are used as
requirements. A more restrictive authority or safety rule wins any conflict.

## 3. Scope

WLA-00 defines:

- the source-of-truth and authority hierarchy;
- the staged lifecycle from Fact through SHADOW;
- the order `WLA-00 -> WLA-01 -> WLA-02 -> WLA-03 -> Gate P0-A`;
- ownership and separation of duties;
- event semantics without fixing a wire format;
- provenance, integrity, replay, and correction rules;
- temporal and information-leakage controls;
- threat boundaries and severity calibration;
- legacy containment requirements; and
- the evidence required to declare WLA-00 complete.

WLA-00 explicitly excludes:

- implementation of `AlphaLearningEnvelopeV1`;
- creation of `wolf15-learning-journal` or the later learning repositories;
- database migrations, queues, dispatches, scheduled workflows, credentials, or
  deployments;
- training or selecting a model;
- production, paper-trading, order-routing, broker, or EA changes; and
- any claim that the legacy reflective stack is an implementation of WLA.

## 4. Delivery order

The only legal program order is:

```text
WLA-00 PROPOSED
  -> WLA-00 ACCEPTED
  -> WLA-01
  -> WLA-02
  -> WLA-03
  -> Gate P0-A human decision
  -> create wolf15-learning-journal only if Gate P0-A = PASS
  -> Journal maturity gate
  -> Orchestrator eligibility
  -> Domain Knowledge eligibility
  -> Adaptive Memory eligibility
```

WLA-01 has one bounded minimum scope fixed by this constitution: specify and
implement the `AlphaLearningEnvelopeV1` contract plus canonical positive and
negative fixtures, with no runtime activation. Its full charter and the detailed
charters for WLA-02 and WLA-03 MUST be accepted separately. Work may be researched
early, but no later stage may be treated as complete, deployed, or authoritative
before every prior gate passes.

The other learning repositories MUST NOT be scaffolded as a batch. A repository
is created only after the preceding capability demonstrates a need, a bounded
owner, and a passing gate.

## 5. Source and decision precedence

From highest to lowest precedence:

1. WOLF15 constitutional authority and its canonical runtime records govern
   Alpha, risk, verdict, and execution truth.
2. This WLA-00 package governs the learning plane.
3. Accepted WLA ADRs govern their stated decisions.
4. Versioned contracts govern serialization only inside their accepted scope.
5. Implementations and configuration must conform to all higher levels.
6. Dashboards, reports, prompts, reflections, embeddings, and README claims are
   projections or advice and are never sources of authority.

If evidence is absent, stale, inaccessible, or contradictory, the value remains
`UNKNOWN` or `NOT_MEASURED`. It MUST NOT be converted to zero, success, safety,
readiness, or permission.

## 6. Non-negotiable invariants

1. WOLF15 remains the sole canonical Alpha source.
2. Information may flow out of WOLF15; learning authority never flows back.
3. Learning identities and derived claims always retain source lineage.
4. Facts and outcomes are immutable; corrections append new records.
5. Outcome information is unavailable before its legal availability time.
6. Replay reconstructs an as-of view; it never reads the latest convenient view.
7. Reflections are hypotheses, not facts, labels, rules, or approvals.
8. Datasets are sealed, reproducible snapshots with explicit cutoffs and splits.
9. Challengers cannot become champion, Alpha, or production artifacts by score.
10. SHADOW is terminal for autonomous behavior and has no control-plane output.
11. Human approval cannot be synthesized from a metric or automated event.
12. Any authority ambiguity fails closed and blocks progression.

## 7. Evidence baseline

This proposal was grounded against static repository evidence, not runtime
claims:

| Evidence set | Revision | Use |
| --- | --- | --- |
| `TUYUL-FX-WOLF-15LAYER-SYSTEM-prw1` | `7ff2a9194b22e185b35dc61574c61628ba404939` | Prior art for typed, hash-chained, observational-only export boundaries. It is not `AlphaLearningEnvelopeV1`. |
| `TUYUL-KARTEL-FX-AGI-HYBRID` | `ba70b5e6d29391fcbe6d5eaf67dd7a47b76dc09d` | Legacy reflective surfaces and documentation being constitutionally contained. |
| `TUYUL-FX-KNOWLEDGE-VAULT-AGI` | `01aacfacf0f0b5884f3ede2813797dd4a982d140` | Legacy theoretical/knowledge repository claims. |
| `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI` | `a98f87a875944b7367375074d539d712e5954192` | Legacy journal schemas and outcome co-location. |
| `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI` | `2c54821b3c6f5b90cfe53e5115c15f20e2c1a04d` | Legacy heuristic promotion and adaptive-memory claims. |

Static presence does not establish that any workflow or runtime is currently
enabled. Operational status remains `NOT_MEASURED` unless separately verified.

### Cross-repository WLA-00 alignment

The three sibling repositories carry local repository-wide declarations. These
files deny WLA standing to every artifact at their pinned baseline revision,
including files without a duplicate banner:

| Repository | Local boundary path | Baseline Markdown scope | WLA status |
| --- | --- | ---: | --- |
| `TUYUL-FX-KNOWLEDGE-VAULT-AGI` | `docs/WLA-00-LEGACY-BOUNDARY.md` | 127 files | `L1_DECLARED_NON_AUTHORITATIVE` |
| `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI` | `docs/WLA-00-LEGACY-BOUNDARY.md` | 8 files | `L1_DECLARED_NON_AUTHORITATIVE`; `DO_NOT_REUSE` as future Journal |
| `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI` | `docs/WLA-00-LEGACY-BOUNDARY.md` | 23 files | `L1_DECLARED_NON_AUTHORITATIVE` |

These are discoverability controls only. They do not establish L2 runtime denial,
L3 CI enforcement, L4 archive/removal, named human ownership, or acceptance.

## 8. Document map

| Artifact | Purpose |
| --- | --- |
| [ADR-000](adrs/ADR-000-wla-constitution-and-precedence.md) | Constitutional scope, status, and precedence |
| [ADR-001](adrs/ADR-001-wolf15-canonical-alpha.md) | WOLF15 canonical Alpha and one-way boundary |
| [ADR-002](adrs/ADR-002-staged-topology-and-repository-sequencing.md) | Staging and repository creation order |
| [ADR-003](adrs/ADR-003-learning-lifecycle.md) | Fact-to-SHADOW lifecycle |
| [ADR-004](adrs/ADR-004-event-envelope-semantics.md) | Event identity, provenance, and integrity semantics |
| [ADR-005](adrs/ADR-005-append-only-evidence-and-corrections.md) | Immutability, correction, and retention |
| [ADR-006](adrs/ADR-006-authority-and-capability-isolation.md) | Capability isolation and no self-promotion |
| [ADR-007](adrs/ADR-007-temporal-and-leakage-controls.md) | Point-in-time and leakage rules |
| [ADR-008](adrs/ADR-008-replay-dataset-and-challenger-reproducibility.md) | Reproducibility and evaluation |
| [ADR-009](adrs/ADR-009-gates-shadow-and-fail-closed-rollout.md) | Gates, SHADOW ceiling, and rollback |
| [Threat boundary](THREAT-BOUNDARY.md) | Assets, actors, trust boundaries, threats, severity |
| [Ownership matrix](OWNERSHIP-MATRIX.md) | Ownership, RACI, and separation of duties |
| [Event vocabulary](EVENT-VOCABULARY.md) | Canonical terms and allowed event names |
| [Authority rules](AUTHORITY-RULES.md) | Explicit allow/deny capability policy |
| [Temporal and leakage rules](TEMPORAL-AND-LEAKAGE-RULES.md) | As-of, labeling, splitting, and leakage tests |
| [Legacy containment](LEGACY-CONTAINMENT.md) | Quarantine rules for pre-WLA surfaces |
| [Definition of Done](DEFINITION-OF-DONE.md) | WLA-00 completion and Gate P0-A prerequisites |
| [Traceability](TRACEABILITY.md) | Requirement-to-decision-to-evidence map |
| [Ratification packet](RATIFICATION-PACKET.md) | Non-normative human ownership, review, and decision record |
| [Verification receipt](VERIFICATION-RECEIPT.md) | Non-normative authoring checks, digest, limitations, and current status |

## 9. Change control

- Changes to an accepted invariant require a new superseding ADR.
- Existing events, datasets, and decisions are never rewritten to make a new ADR
  appear historically effective.
- Emergency restriction may immediately reduce capability. Expanding capability
  requires normal review and cannot be an emergency shortcut.
- A rejected gate records reasons and evidence. It does not silently reset.
- No WLA component may approve a change to its own authority ceiling.
