# WLA-00 Authority Rules

Status: `PROPOSED`

These rules define capabilities, not intentions. A component violates the
constitution if it can perform a prohibited action, even if normal code paths do
not call it.

## 1. Canonical authority

| ID | Rule |
| --- | --- |
| `AUTH-001` | WOLF15 is the sole canonical Alpha source. |
| `AUTH-002` | WOLF15's constitutional verdict path remains the sole trade-verdict authority; WLA cannot add or substitute a verdict path. |
| `AUTH-003` | Every WLA identity MUST be technically unable to mutate WOLF15 source state. |
| `AUTH-004` | Mirrored source fields retain their WOLF15 authority class as provenance, while the envelope and consumer remain `OBSERVATIONAL_ONLY`. |
| `AUTH-005` | Broker/EA acknowledgements may be observed as outcomes only through an approved source-owned export; they do not make Journal execution-authoritative. |

## 2. Evidence authority

| ID | Rule |
| --- | --- |
| `AUTH-006` | Journal owns append-only learning evidence, not Alpha truth. |
| `AUTH-007` | Only WOLF15/the approved source owner may correct a source Fact or source Outcome Evidence. A WLA owner may correct only its own derived artifact; it cannot use a derived correction to alter or reinterpret source evidence. |
| `AUTH-008` | Episode assembly cannot alter or fill missing Facts. |
| `AUTH-009` | Outcome builders cannot infer authoritative fills, rejects, or maturity from price movement alone. |
| `AUTH-010` | Replays, reflections, datasets, indexes, embeddings, and metrics are derived evidence and MUST retain lineage. |
| `AUTH-011` | A Reflection is a hypothesis. It cannot become a rule, label, feature, or knowledge artifact without a separately recorded review path. |
| `AUTH-012` | An Adaptive Memory index is a disposable projection. Rebuilding or losing it cannot change canonical evidence. |
| `AUTH-012A` | Synthetic, fallback, estimated, placeholder, or imputed source-like data MUST be explicitly typed and isolated; it can never be relabeled as a canonical Fact. |
| `AUTH-012B` | Missing, stale, failed, or inaccessible evidence remains `UNKNOWN`/`NOT_MEASURED`; it cannot default to zero, a confidence score, “now”, readiness, or permission. |

## 3. Mutation and execution denials

| ID | Rule |
| --- | --- |
| `AUTH-013` | WLA MUST NOT write WOLF15 databases, outboxes, caches, configuration, feature flags, repositories, queues, or control APIs. |
| `AUTH-014` | WLA MUST NOT possess broker, trading terminal, EA, order-router, execution queue, risk-reservation, or trade-outbox credentials. |
| `AUTH-015` | WLA MUST NOT emit `BUY`, `SELL`, order, sizing, stop, target, cancel, modify, or risk-reservation commands. |
| `AUTH-016` | WLA MUST NOT alter capital, exposure, risk limits, pair admission, kill switches, governance locks, or runtime routing. |
| `AUTH-017` | WLA MUST NOT send alerts that an operator or bot is instructed to execute as trades. Research notifications must be clearly non-actionable. |
| `AUTH-018` | WLA MUST NOT commit, push, merge, deploy, or modify another repository through an autonomous learning decision. |
| `AUTH-019` | Bidirectional transports are denied unless reverse operations are removed by credentials and policy, not merely unused in code. |
| `AUTH-019A` | WLA has no inbound callback or command channel to WOLF15; reconciliation operates only on already exported evidence. |

## 4. Challenger, SHADOW, and approval

| ID | Rule |
| --- | --- |
| `AUTH-020` | A Challenger is never Alpha, champion, production, or execution-approved by virtue of its score. |
| `AUTH-021` | SHADOW is observation-only and the maximum autonomous mode authorized by WLA-00. |
| `AUTH-022` | No automated component may approve, promote, merge, deploy, or expand its own capability. |
| `AUTH-023` | A valid gate requires named human approvers, exact evidence hashes, separation of duties, and an explicit decision. |
| `AUTH-024` | Approval expiry, missing approval, `UNKNOWN`, `NOT_MEASURED`, `BLOCKED`, skipped checks, and conflicting evidence all deny progression. |
| `AUTH-025` | Emergency actions may kill, isolate, revoke, or reduce capability. They cannot enable or expand it. |

## 5. Allowed capability ceiling by component

| Component | Allowed | Explicitly denied |
| --- | --- | --- |
| WOLF15 export adapter | Serialize source-owned facts and append them atomically to an approved observational outbox | Learning, outcome labeling, source rewrite, remote promotion |
| Journal ingress | Validate, deduplicate, quarantine, append receipts and evidence | Source repair, verdict, execution, reflection approval |
| Episode builder | Deterministically group eligible Fact references | Fact mutation, outcome access before cutoff |
| Outcome builder | Append matured, source-backed Outcome artifacts | Backfill source rows, infer fills without authority |
| Replay engine | Reconstruct pinned as-of views and emit receipts | Live decisions, source calls with mutation capability |
| Reflection engine | Produce cited hypotheses with uncertainty | Policy changes, feature activation, promotion |
| Dataset builder | Build and seal point-in-time datasets | Relabel after seeing evaluation results |
| Training runner | Produce immutable Challenger artifacts | Register as Alpha/champion or deploy |
| SHADOW session controller | Verify the active human-ratified policy and independent eligibility receipt; start or stop only an isolated, learning-owned session; append session lifecycle events | Edit policy or eligibility evidence, train/evaluate the same Challenger, expand mode, hold source/control/execution credentials, gain WOLF15 reachability |
| SHADOW evaluator | Compare namespaced non-actionable prediction classes with mirrored facts and append evidence | Execution-shaped signal/order payloads, `executable` flags, lot/risk/entry/SL/TP instructions, actionable alerts, routing, write-back |
| Eligibility policy evaluator | Evaluate a pinned human-ratified policy and emit an eligibility receipt | Edit policy, expand capability, approve itself, share identity with artifact producer/trainer |
| CI | Validate contracts, policy, tests, hashes, and manifests | Human approval, promotion, production deployment by model score |

## 6. Enforcement layers

Every prohibition that matters MUST be enforced in at least two independent
layers, and execution/source-mutation prohibitions in at least three:

1. type/schema invariant;
2. application authorization;
3. credential scope and secret inventory;
4. network/egress policy;
5. storage role/ACL;
6. CI static policy and negative tests; and
7. runtime audit/alerting.

Documentation alone is never an enforcement layer.
