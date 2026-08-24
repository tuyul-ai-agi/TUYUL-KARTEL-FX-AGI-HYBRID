---
id: ADR-000
title: WLA constitution, scope, and precedence
status: PROPOSED
date: 2026-08-24
---

# ADR-000: WLA constitution, scope, and precedence

## Context

Existing repositories use overlapping terms such as reflective learning,
meta-learning, journal, knowledge, and adaptive memory. Some documents describe
automatic mutation and promotion. Without an explicit precedence rule, those
claims could be mistaken for authority to implement or operate the new learning
plane.

## Decision

WLA-00 is the constitutional baseline for all Wolf15 learning work. It governs
the learning plane while WOLF15's own constitution remains authoritative for
Alpha, risk, verdict, and execution.

All WLA artifacts begin as `PROPOSED`. Only named humans may accept or supersede
an ADR. Code, CI, agents, metrics, challengers, and SHADOW processes may provide
evidence but may not approve themselves.

The precedence order is the one defined in the package README. If two rules
conflict, the rule that grants less authority or preserves more source evidence
wins until a human governance decision resolves the conflict.

Legacy artifacts have no implied grandfathering. Adoption requires an explicit
later-stage decision, a current threat review, contract conformance, and negative
authority tests.

## Consequences

- WLA-00 can be reviewed independently of runtime implementation.
- Existing “active” or “stable” labels cannot establish current readiness.
- Later contracts cannot broaden authority through a schema field or default.
- Emergency action may restrict or disable capability, but cannot expand it.

## Rejected alternatives

- **Treat current reflective repositories as the baseline implementation.**
  Rejected because their semantics and mutation paths predate WLA boundaries.
- **Let implementation define the architecture.** Rejected because authority
  and leakage defects would become backward-compatibility obligations.
- **Auto-accept ADRs when tests pass.** Rejected because tests are evidence, not
  governance authority.

## WLA-00 acceptance

- Every WLA document declares a status and scope.
- The document index resolves to ADR-000 through ADR-009 and all support files.
- Reviewers confirm that no lower-level artifact can overrule WOLF15 or WLA-00.
- The legacy containment register is reviewed and has an accountable owner.

No WLA-01/02/03 implementation or runtime evidence is required to accept this
decision. Those stages must later prove conformance to it.

## Downstream conformance obligations

- Every later charter, contract, implementation, and gate record declares which
  WLA-00 rules it proves and which remain `NOT_EXECUTED`.
- No legacy artifact gains compatibility or authority without a reviewed adoption
  decision and current evidence.
