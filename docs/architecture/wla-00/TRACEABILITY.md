# WLA-00 Traceability Matrix

Status: `PROPOSED`

| Requirement | Primary decision | Operational rule | Verification evidence |
| --- | --- | --- | --- |
| WOLF15 is canonical Alpha | ADR-001 | `AUTH-001` to `AUTH-004` | Source-owner review; downstream negative write-path tests before P0-A |
| Lifecycle is Fact through SHADOW | ADR-003 | Event vocabulary and lifecycle transition table | Contract fixtures and state-transition tests |
| WLA order is fixed | ADR-002 | Stage ledger in Definition of Done | Signed completion receipt for each stage |
| No batch creation of four repos | ADR-002 | Repository eligibility gates | Repository existence/change audit at each gate |
| No source mutation | ADR-001, ADR-006 | `AUTH-003`, `AUTH-013`, `AUTH-019`, `AUTH-019A` | Credential inventory; egress deny tests; source snapshot comparison |
| No execution authority | ADR-006, ADR-009 | `AUTH-014` to `AUTH-017` | Static capability scan plus runtime network/credential attestation |
| No self-promotion | ADR-006, ADR-009 | `AUTH-018`, `AUTH-020` to `AUTH-024` | Human approval receipt; negative promotion tests |
| Facts/outcomes are immutable | ADR-005 | Correction/supersession protocol | Append-only and duplicate-conflict tests |
| Events are attributable and ordered | ADR-004 | Required semantic header fields | Schema fixtures; hash/order/idempotency tests |
| Point-in-time correctness | ADR-007 | Availability-time and as-of rules | Temporal canaries and late-arrival tests |
| Replays are deterministic | ADR-008 | Replay manifest | Repeat-run digest comparison |
| Datasets are reproducible | ADR-008 | Dataset seal and split policy | Manifest digest and rebuild comparison |
| SHADOW is terminal autonomous state | ADR-009 | Human-ratified SHADOW policy plus per-artifact automated eligibility and a one-way telemetry-only boundary | Policy/authority gate receipt; eligibility fixture; egress, credential, and side-effect tests |
| Legacy stack is non-authoritative | ADR-000, ADR-006 | Legacy containment register | Inventory closure and CI denylist evidence |
| Unknown evidence stays unknown | ADR-000, ADR-007 | Explicit epistemic status vocabulary | Missing/stale input tests |
| WLA-00 cannot self-ratify | ADR-000, ADR-009 | Human sign-off matrix | Named approval record |

## Evidence classes

Evidence MUST remain separated into these classes:

1. `STATIC`: repository paths, contracts, configuration, and workflow definitions.
2. `TEST`: reproducible automated or manual test results tied to a revision.
3. `RUNTIME`: service identity, deployment, configuration, and observed behavior.
4. `EXTERNAL`: broker, EA, vendor, or third-party state from an authoritative source.
5. `GOVERNANCE`: signed human decisions and exceptions.

One class cannot silently stand in for another. In particular, a clean local test
does not prove a deployment state, and an empty local mirror does not prove broker
state.
