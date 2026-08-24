# WLA-00 Ownership and Separation-of-Duties Matrix

Status: `PROPOSED`

## 1. Roles

| Role | Responsibility | Authority ceiling |
| --- | --- | --- |
| WOLF15 Alpha Owner (`WAO`) | Own canonical Alpha semantics and source export eligibility | WOLF15 Alpha/source only; cannot approve its own learning consumer security |
| WLA Architecture Owner (`ARO`) | Own WLA constitution and cross-component coherence | Architecture decisions; no model or execution promotion |
| Journal Data Steward (`JDS`) | Own evidence quality, lineage, retention, corrections, and access | Learning evidence store only |
| Orchestrator Owner (`ORO`) | Own job definitions, retries, and workflow observability | Schedule approved learning jobs only |
| Domain Knowledge Curator (`DKC`) | Review claims proposed for curated knowledge | Curated knowledge; no Alpha or deployment authority |
| Adaptive Memory Owner (`AMO`) | Own retrieval/index quality and rebuildability | Non-authoritative projections only |
| Model Developer (`MDV`) | Build datasets/training code and Challengers | Challenger artifacts only |
| Independent Model Risk Reviewer (`MRR`) | Validate evaluation, leakage controls, and limitations | Recommend/deny model gate; cannot build reviewed artifact |
| Security Approver (`SEC`) | Validate trust boundaries, identities, credentials, and egress | Security gate; no model self-approval |
| Platform Operator (`OPS`) | Operate approved learning infrastructure and kill/disable paths | Availability and restriction; no Alpha or gate substitution |
| CI/Automation (`CI`) | Produce reproducible verification evidence | Evidence only; never accountable or approving |

Named people and backups are normally assigned during ratification. A role label
without an authenticated person is not an approval. `WLA00-EXC-001` is the only
bootstrap exception: it records one human constitutional owner, unavailable
backups, and owner self-concurrence without presenting them as independent
principals. Its authority ceiling is the WLA-01 contract-only spike.

## 2. Artifact ownership

| Artifact | Accountable owner | Permitted writers | Required reviewers | Forbidden writers |
| --- | --- | --- | --- | --- |
| WOLF15 canonical Alpha Fact | `WAO` | WOLF15 source transaction only | WOLF15 governance | All WLA roles/services |
| Source export event | `WAO` | Approved WOLF15 export adapter | `ARO`, `SEC` | Journal, Orchestrator, models |
| Ingress receipt/quarantine | `JDS` | Journal ingress | `SEC` | WOLF15 source adapter after publish |
| Episode | `JDS` | Approved deterministic builder | `MRR` | Reflection/model services |
| Outcome | `JDS` | Approved source-backed outcome builder | `WAO`, `MRR` | Challenger/SHADOW services |
| Replay receipt | `ORO` | Replay runner | `JDS`, `MRR` | WOLF15 runtime |
| Reflection | `DKC` | Reflection service or researcher | `JDS`, `MRR` | WOLF15 runtime |
| Curated domain-knowledge claim | `DKC` | Curator after human review | `WAO`, `MRR` as applicable | Reflection service alone |
| Dataset manifest | `JDS` | Dataset builder | `MRR` | Training runner after seal |
| Challenger manifest/model | `MDV` | Training runner | `MRR`, `SEC` | SHADOW evaluator after registration |
| Automated eligibility receipt | `MRR` | Independent policy-evaluator service | `SEC`, `OPS` | Artifact producer, training runner, policy editor |
| SHADOW session start/stop receipt | `OPS` | Dedicated SHADOW session-controller service | `MRR`, `SEC` | Trainer, Challenger owner, policy evaluator/editor, SHADOW evaluator |
| SHADOW evaluation | `MRR` | Shadow evaluator | `SEC`, `OPS` | Challenger/training runner |
| Gate decision | `ARO` | Approval service recording human decision | Roles required by gate | CI, agents, model, artifact owner alone |
| Adaptive-memory index | `AMO` | Approved indexer | `JDS`, `SEC` | WOLF15 and canonical Journal ledger |

For automated rows, “Required reviewers” ratify the policy and control class and
may audit receipts; they do not sign every artifact, run, or observation. Once
that policy is active, each instance progresses only on a machine-verifiable
eligibility receipt. Any policy, authority-ceiling, identity, credential, egress,
or deployment-mode change returns to a human gate.

## 3. RACI for key decisions

Legend: `R` responsible, `A` administratively accountable, `C` consulted or
concurrent approver when marked `C*`, `I` informed, `X` no decision authority.
Each row has exactly one administrative owner; required concurrence prevents that
owner from acting unilaterally.

| Decision | WAO | ARO | JDS | ORO | DKC | AMO | MDV | MRR | SEC | OPS | CI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Accept WLA constitution | C* | A/R | C* | C | C | C | I | C* | C* | I | X |
| Accept source export semantics | A | C | R | I | X | X | X | C | C | I | X |
| Accept journal retention/correction policy | C | C | A/R | I | I | I | X | C | C | C | X |
| Approve replay/dataset protocol | C | C | R | C | I | X | C | A | C | I | X |
| Register a Challenger | I | I | C | I | I | X | R | A | C | I | X |
| Ratify/change SHADOW policy or authority ceiling | I | A | C | R | I | X | I | C* | C* | C | X |
| Emergency disable/isolate | I | I | I | C | I | I | I | I | C | A/R | X |
| Create `wolf15-learning-journal` after P0-A | C | A | R | I | I | I | I | C | C | C | X |

## 4. Mandatory separation-of-duties rules

1. `MDV` cannot be the sole `MRR` for the same Challenger or dataset.
2. `ORO` cannot approve the jobs it configures for a new authority boundary.
3. `WAO` cannot grant WLA write access to WOLF15 as an export shortcut.
4. `OPS` may disable immediately but cannot enable an unapproved stage.
5. `CI`, models, agents, service accounts, and repository bots cannot fill any
   accountable human role.
6. One person may hold multiple roles only when the relevant gate does not require
   those roles to be separated; the exception must be recorded before review.
   `WLA00-EXC-001` records that separation is not achieved and accepts that
   residual governance risk only for WLA-00 and the WLA-01 contract-only spike.
7. Gate P0-A requires concurrence from `ARO`, `WAO`, `JDS`, and `SEC`. If WLA-03
   includes evaluation behavior, `MRR` concurrence is also required.
8. WLA-00 acceptance normally requires recorded concurrence from `WAO`, `JDS`,
   `MRR`, and `SEC` in addition to the administrative `ARO` decision. Under
   `WLA00-EXC-001`, the same authenticated owner may submit those role
   dispositions as `OWNER_SELF_CONCURRENCE_EXCEPTION`; they are not independent
   concurrence. The primary author cannot be the ratifying principal.
9. The automated eligibility evaluator uses a distinct service identity from the
   artifact producer/training runner, reads a pinned human-ratified policy, and
   cannot edit policy, credentials, stage, or deployment mode.
10. The SHADOW session controller uses a distinct service identity from the
    trainer, Challenger owner, eligibility evaluator, policy editor, and SHADOW
    evaluator. It may instantiate only the mode, artifact, limits, and expiry
    named by a passing eligibility receipt; it cannot widen them.

## 5. Single-owner bootstrap assignment

| Field | Recorded value |
| --- | --- |
| Governance mode | `SINGLE_OWNER_BOOTSTRAP` |
| Constitutional owner | Dwi Kelana Putra (`KELANA TJX`) |
| Authority basis | `SYSTEM_OWNER_AND_REPOSITORY_OWNER` |
| GitHub subject | `tjx578`; GitHub user ID `221953664` |
| Assumed roles | `ARO`, `WAO`, `JDS`, `MRR`, `SEC` |
| Independent concurrence | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |
| Backups | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |
| Exception | `WLA00-EXC-001`; non-reusable |
| Expiry | WLA-01 completion or any scope expansion |
| Allowed | Contract schema, pure contract tests, documentation, deterministic fixtures |
| Forbidden | Runtime, database/outbox activation, broker/EA, deployment, production/advisory activation, new repositories, Gate P0-A |

If a backup later acts, the primary must be `UNAVAILABLE` or `RECUSED` and a
signed delegation reference is mandatory. Before any forbidden scope or later
gate, governance and separation of duties must be evaluated again.

## 6. Access review

Access is deny-by-default, time-bounded where possible, attributable to one
identity, and reviewed at each stage boundary. Shared personal tokens and
credentials that span WOLF15, learning, GitHub mutation, and deployment are
prohibited. Revocation evidence is part of rollback readiness.
