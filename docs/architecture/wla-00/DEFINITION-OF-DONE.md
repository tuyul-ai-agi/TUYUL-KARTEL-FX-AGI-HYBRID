# WLA-00 Definition of Done

Status: `PROPOSED`

## 1. What “done” means

WLA-00 has three deliberately separate states:

1. **Authoring complete:** all required proposal artifacts exist and pass local
   document verification.
2. **Accepted:** authenticated human governance ratifies the proposal after every
   WLA-00 item below is satisfied, including any explicitly bounded bootstrap
   exception.
3. **Downstream conformance:** WLA-01/02/03 and Gate P0-A later prove the contract
   and capability controls. These proofs are not prerequisites for accepting
   WLA-00, otherwise the official order would deadlock.

No state is inferred. A missing or stale receipt is not a pass.

## 2. Current program ledger

This table is updated only by an explicit evidence-backed decision:

| Item | Status at this proposal | Meaning |
| --- | --- | --- |
| WLA-00 authoring | `COMPLETED` | Docs-only package verified in `VERIFICATION-RECEIPT.md`; this is not ratification |
| WLA-00 ratification gate | `NOT_EVALUATED` | Ratification packet prepared; no human acceptance claimed |
| WLA-01 | `NOT_STARTED` | Charter and implementation evidence absent |
| WLA-02 | `NOT_STARTED` | Charter and implementation evidence absent |
| WLA-03 | `NOT_STARTED` | Charter and implementation evidence absent |
| Downstream contract/runtime tests | `NOT_EXECUTED` | Not a pass and not a code failure |
| Gate P0-A | `NOT_EVALUATED` | Journal creation is not eligible |
| `wolf15-learning-journal` | `NOT_CREATED` | Must remain absent before P0-A `PASS` |
| Orchestrator repository/capability | `NOT_CREATED` | Later eligibility gate required |
| Domain Knowledge repository/capability | `NOT_CREATED` | Later eligibility gate required |
| Adaptive Memory repository/capability | `NOT_CREATED` | Later eligibility gate required |

## 3. WLA-00 acceptance checklist

Every checkbox is mandatory for status `ACCEPTED`.

A checked item means local/static proposal evidence exists at the verification
receipt digest. It is not a human approval and cannot compensate for any
unchecked item.

### A. Constitutional completeness

- [x] README states scope, non-goals, precedence, mandatory order, autonomous
  ceiling, and change control.
- [x] ADR-000 through ADR-009 exist, have unique IDs, status, context, decision,
  consequences, rejected alternatives, WLA-00 acceptance conditions, and clearly
  separated downstream obligations.
- [x] Threat boundary covers assets, actors, attacker/operator/developer inputs,
  trust boundaries, assumptions, attack stories, mitigations, and severity.
- [x] Ownership matrix names accountable roles, required concurrence, access
  ceilings, and separation of duties.
- [x] Event vocabulary distinguishes events, commands, artifact nouns, authority,
  statuses, corrections, and bounded lineage.
- [x] Authority rules explicitly deny source mutation, self-promotion, execution,
  broker/EA, risk, control-plane, and repository-mutation authority.
- [x] Temporal rules define source publication, receipt, ingestion, learning
  availability, maturity, as-of joins, corrections, splits, and leakage tests.
- [x] Definition of Done separates documentation acceptance from future runtime
  conformance.

### B. Semantic consistency

- [x] WOLF15 is canonical Alpha in every artifact.
- [x] Outcome Evidence is source-owned; Outcome label is policy-derived and has
  explicit horizon, finality, censoring, correction, and availability semantics.
- [x] WLA outage/backpressure cannot block or degrade WOLF15
  analysis/risk/verdict/execution, and no learner acknowledgement controls source.
- [x] Automated artifact processing through Challenger/SHADOW is permitted only
  under a fixed human-ratified policy and does not become self-approval.
- [x] Policy evaluator is independent of the artifact producer/trainer and cannot
  edit policy, credentials, stage, or mode.
- [x] SHADOW session controller is independently identified, can instantiate
  only the exact approved session envelope, and cannot train, evaluate, edit
  policy/eligibility, or widen authority.
- [x] Human gates apply to program/repository/policy/authority changes; automated
  eligibility applies only inside the existing ceiling.
- [x] `UNKNOWN`, `NOT_MEASURED`, `NOT_EXECUTED`, `NOT_EVALUATED`, and
  `NOT_CREATED` remain distinct from zero, failure, success, and readiness.
- [x] Direct source references are bounded; large ancestry uses sealed manifests,
  ranges, counts, and integrity roots.

### C. Discoverability and legacy containment

- [x] Repository root README links to WLA-00 and states that all earlier reflective
  learning claims are legacy/non-authoritative for WLA.
- [x] Every conflicting legacy root/governance/architecture document across the
  four reviewed repositories has a prominent `LEGACY / NON-AUTHORITATIVE FOR WLA`
  banner or is listed as an explicit acceptance blocker with owner and deadline.
- [x] No legacy Journal repository is renamed or reused as
  `wolf15-learning-journal`.
- [x] The required full legacy inventory scope covers code, workflow triggers,
  schedules, dispatches, external commands, Git/GitHub mutation, source/config
  writes, default/synthetic data, actionable outputs, credentials, egress, and
  storage mutation; `LEGACY-INV-001` remains explicitly `OPEN` until its
  downstream pre-P0-A deadline and is not misreported as completed at WLA-00.
- [x] WLA-00 reaches at least containment
  `L1_DECLARED_NON_AUTHORITATIVE` across all four reviewed repositories.
- [x] Every legacy surface class has a named primary and a bounded L3/L4 plan for
  P0-A; backup unavailability is explicitly recorded by `WLA00-EXC-001` and may
  not survive WLA-01 completion or scope expansion.
- [x] Static presence and runtime activation are reported separately; unverified
  runtime state remains `NOT_MEASURED`.

### D. Governance and review

- [x] Dwi Kelana Putra (`KELANA TJX`) is the named primary for `ARO`, `WAO`,
  `JDS`, `MRR`, and `SEC`; unavailable backups and the expiration boundary are
  recorded under `WLA00-EXC-001` without inventing independent people.
- [x] The `ARO` submitted `APPROVED` with
  `OWNER_SELF_CONCURRENCE_EXCEPTION` dispositions for `WAO`, `JDS`, `MRR`, and
  `SEC`; the acceptance record must still validate the GitHub signature.
- [x] Primary author Codex is not the ratifying principal; the single-owner
  conflict, lack of independent concurrence, and lack of backups are explicit.
- [x] The owner submitted no blocking objection for threat, temporal/leakage,
  data-governance, source-owner, or model-risk review within the contract-only
  ceiling; independent review is not claimed and is required again before scope
  expansion.
- [x] Every Critical/High threat has a control ID, accountable owner, owning
  downstream stage/gate, test/evidence ID, and fail-closed residual disposition;
  none is unowned or unmapped.
- [x] Every exception reduces capability or is governed by a superseding ADR; no
  exception silently expands authority.

### E. Verification evidence

- [x] All internal Markdown links resolve.
- [x] ADR IDs and event names are unique and follow their grammar.
- [x] No unresolved placeholder marker, ambiguous “active/live/ready” claim,
  secret, credential, broker token, executable command, or serialized
  `AlphaLearningEnvelopeV1` appears in the WLA-00 package.
- [x] Cross-document review confirms that every mention of automatic promotion,
  bidirectional source control, a single generic availability timestamp, or
  random-row splitting is historical, rejected, or explicitly prohibited; no
  normative rule permits it.
- [x] The reviewed diff changes documentation only and identifies all unrelated
  pre-existing worktree changes.
- [x] Verification receipt records repository, base revision, reviewed paths,
  commands/checks, results, limitations, reviewer, and time.

## 4. WLA-00 acceptance record

The acceptance record MUST bind the exact tree/digest and contain:

| Field | Required value |
| --- | --- |
| Decision | `PASS` or `FAIL` |
| Scope | Exact WLA-00 paths and revision/digest |
| Governance mode | Normal multi-principal governance or a named, bounded exception |
| Ratification ID | Globally unique decision identifier |
| ARO | Authenticated person, decision, time |
| WAO concurrence | Authenticated person, decision, time |
| JDS concurrence | Authenticated person, decision, time |
| MRR concurrence | Authenticated person, decision, time |
| SEC concurrence | Authenticated person, decision, time |
| Open risks | Explicit list; empty only when verified empty |
| Conditions/expiry | Explicit value, including `NONE` where appropriate |
| Authentication/signature | Immutable references binding subject, role, packet hash, target SHA, verdict, conditions hash, ratification ID, and time |
| Supersedes | Prior record ID or `NONE` |

Current acceptance record: `NOT_EVALUATED`. The unsigned
[ratification packet](RATIFICATION-PACKET.md) is the only prepared decision
carrier. It is not an approval and cannot advance the program ledger.

## 5. Downstream conformance obligations

After WLA-00 is accepted, the WLA-01/02/03 charters allocate and prove at least:

- typed `AlphaLearningEnvelopeV1` serialization and version policy;
- source-owned Outcome Evidence vocabulary and policy-derived Outcome labels;
- stable IDs, canonical hashes, bounded lineage, stream gap/fork/conflict handling;
- one-way source export with no synchronous learner dependency;
- append-only ingestion, quarantine, correction, invalidation, and as-of query;
- reference Episode/Replay/Dataset behavior and deterministic fixtures;
- temporal/leakage canaries and preregistered Challenger evaluation protocol;
- capability/credential/ACL/egress denial tests;
- policy-evaluator independence and SHADOW isolation; and
- rollback, recovery, observability, retention, and resource/backpressure limits.

These are `NOT_EXECUTED` at WLA-00 acceptance and must not be described as proven.

## 6. Gate P0-A prerequisites

Gate P0-A may be evaluated only when WLA-00, WLA-01, WLA-02, and WLA-03 each have
an explicit `PASS`. P0-A then requires:

1. exact stage receipts and immutable evidence digests;
2. contract and reference-consumer conformance, including negative/fail-closed
   fixtures;
3. proof that learning outage/backpressure cannot affect WOLF15 authority paths;
4. legacy containment L3 or L4 for every relevant trigger/capability;
5. credential and network evidence showing no WOLF15 write, Git/GitHub mutation,
   broker/EA, risk, verdict, execution, deploy, or self-promotion capability;
6. current threat review and closed critical/high blockers;
7. point-in-time/leakage, reproducibility, load/backpressure, and recovery evidence;
8. a creation charter, owner, access model, retention policy, cost envelope,
   observability, rollback, and archive plan for `wolf15-learning-journal`;
9. confirmation that the legacy Journal will not be reused or synchronized into
   the new canonical ledger; and
10. authenticated human `PASS` under the approved P0-A policy.

Any missing, stale, expired, `UNKNOWN`, `NOT_MEASURED`, `NOT_EXECUTED`, or
conflicting item makes P0-A `BLOCKED` or `FAIL`, never `PASS`.

## 7. Post-P0-A boundary

A P0-A `PASS` grants only permission to create `wolf15-learning-journal` under
its approved charter. It grants no permission to create Orchestrator, Domain
Knowledge, or Adaptive Memory; train a model; start SHADOW; or influence WOLF15.
Each later capability requires its own evidence and gate.
