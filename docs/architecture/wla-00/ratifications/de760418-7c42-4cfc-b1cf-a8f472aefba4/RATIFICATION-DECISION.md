# WLA-00 Ratification Decision

Decision record ID: `WLA00-RD-20260824-001`

Ratification ID: `de760418-7c42-4cfc-b1cf-a8f472aefba4`

Canonical verdict: `PASS`

Effective at: `2026-08-24T08:04:07Z`

Validated at: `2026-08-24T08:05:36.759Z`

Governance mode: `SINGLE_OWNER_BOOTSTRAP`

Exception: `WLA00-EXC-001`

This immutable decision record validates the constitutional owner's signed
attestation. It is governance evidence, not part of the 57-file reviewed
constitution digest, and grants no authority beyond the explicit contract-only
ceiling below.

## 1. Bound evidence

| Evidence | Validated value |
| --- | --- |
| Ratification packet | `WLA00-RP-20260824-002` |
| Packet SHA-256 | `3f0dc8e53d47fdbf92efb7cbf388c974b904feadb3afb17612f0a0f52abfb6b8` |
| Reviewed combined SHA-256 | `c2905ff65b9dd9bf07da555ce1cd6ea1e2898432f6f49a5e5d98a7a6cbb6fb6d` |
| WOLF15 target base SHA | `7ff2a9194b22e185b35dc61574c61628ba404939` |
| Submitted verdict | `APPROVED` |
| Conditions | `[]` |
| Conditions SHA-256 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |
| Owner decision time | `2026-08-24T07:29:18.577Z` |
| Verified attestation commit | [`726f368aaa5f549348674be8eac0a29578412b40`](https://github.com/tuyul-ai-agi/TUYUL-KARTEL-FX-AGI-HYBRID/commit/726f368aaa5f549348674be8eac0a29578412b40) |
| GitHub verification | `verified=true`; `reason=valid`; `verified_at=2026-08-24T08:04:07Z` |
| Authenticated principal | `tjx578`; numeric ID `221953664` |
| Commit author | `tjx578` |
| Committer/trust anchor | GitHub `web-flow` |
| Signed attestation path | `OWNER-ATTESTATION.yaml` in this directory |

## 2. Validation sequence

| Check | Result |
| --- | --- |
| Packet hash matches attestation | `PASS` |
| Target SHA is a 40-character WOLF15 baseline | `PASS` |
| Ratification ID and decision timestamp match | `PASS` |
| Constitutional-owner role and assumed roles match | `PASS` |
| GitHub subject and numeric identity match | `PASS` |
| Signed statement contains the full decision tuple | `PASS` |
| Signature is present and GitHub reports `valid` | `PASS` |
| Signature timestamp postdates the owner decision | `PASS` |
| YAML parses without unknown top-level schema | `PASS` |
| RFC 8785 empty-conditions hash matches | `PASS` |
| Single-owner conflict is explicit | `PASS_WITH_RESTRICTION` |
| Independent concurrence is not falsely claimed | `PASS_WITH_RESTRICTION` |
| Backup assignment is not falsely claimed | `PASS_WITH_RESTRICTION` |
| Exception remains within its unexpired scope | `PASS` |
| Ratification ID replay in another decision | `NOT_DETECTED` |

GitHub's commit API is the revocation and validity reference for this decision.
If the verification becomes invalid, the account association changes, the
reviewed digest changes, or the exception expires, authorization returns to
fail-closed pending a new ratification.

## 3. Effective authorization

```text
GOVERNANCE_MODE       = SINGLE_OWNER_BOOTSTRAP
WLA_00_RATIFICATION   = PASS
WLA_01                = NOT_STARTED
WLA_01_AUTHORIZED     = TRUE
AUTHORIZED_SCOPE      = CONTRACT_ONLY
RUNTIME_MUTATION      = FORBIDDEN
NEW_REPOSITORY        = FORBIDDEN
GATE_P0_A             = NOT_EVALUATED
```

The first authorized stage action is the bounded WLA-01 contract-only spike for
`AlphaLearningEnvelopeV1`, including schema, deterministic fixtures, and
contract tests.

## 4. Continuing prohibitions

This decision does not authorize:

- runtime registration;
- database migration or outbox activation;
- dispatcher, broker, or EA access;
- deployment or production mutation;
- advisory activation or execution authority;
- creation of `wolf15-learning-journal` or any other learning repository;
- Gate P0-A certification; or
- self-promotion by a learner, Challenger, or SHADOW system.

WLA-02 and WLA-03 remain `NOT_STARTED`. Gate P0-A remains `NOT_EVALUATED`.
Journal creation remains prohibited until the complete official sequence passes.

## 5. Exception expiry

`WLA00-EXC-001` is non-reusable and expires at the earlier of:

1. completion of WLA-01; or
2. any proposed scope expansion.

Expiry does not invalidate historical evidence, but it ends the authorization
granted by this decision. A new governance evaluation is mandatory before any
runtime, repository-creation, deployment, production, Gate P0-A, or broader
learning authority is considered.
