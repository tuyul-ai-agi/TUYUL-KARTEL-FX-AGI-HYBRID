# WLA-00 Human Ratification Packet

Packet ID: `WLA00-RP-20260824-002`

Supersedes: `WLA00-RP-20260824-001`

Ratification ID: `de760418-7c42-4cfc-b1cf-a8f472aefba4`

Gate: `WLA-00-RATIFICATION`

Submitted verdict: `APPROVED`

Canonical status: `NOT_EVALUATED_PENDING_VERIFIED_SIGNATURE`

WLA-01 authorized: `FALSE`

Decision time: `2026-08-24T07:29:18.577Z`

Governance mode: `SINGLE_OWNER_BOOTSTRAP`

Prepared against receipt: `WLA00-VR-20260824-005`

This packet records the human owner's submitted decision and the narrow
single-owner exception. Submission alone is not the effective ratification. The
canonical status remains fail-closed until a GitHub `Verified` commit made by
the authenticated owner binds the exact tuple in section 7 and a validation
record confirms it.

## 1. Exact review scope

The decision binds all three digests below. This packet and its verification
receipt are excluded from the reviewed-content digest because they carry the
decision and verification evidence rather than define the constitution.

| Digest set | Count | SHA-256 |
| --- | ---: | --- |
| Normative WLA-00 package | 19 | `22b887455e6269db581971ece2b6a6ba47fb47e058251593c7c2f31ae3243005` |
| Supporting four-repository alignment | 38 | `bf936dd58f4b50c31195b2ae7065c34559983ea93f1b615b404b8a5fb74f521a` |
| Combined reviewed scope | 57 | `c2905ff65b9dd9bf07da555ce1cd6ea1e2898432f6f49a5e5d98a7a6cbb6fb6d` |

| Repository | Documentation branch | Pinned baseline revision |
| --- | --- | --- |
| `TUYUL-KARTEL-FX-AGI-HYBRID` | `codex/wla-00-ratification` | `ba70b5e6d29391fcbe6d5eaf67dd7a47b76dc09d` |
| `TUYUL-FX-KNOWLEDGE-VAULT-AGI` | `codex/wla-00-ratification` | `01aacfacf0f0b5884f3ede2813797dd4a982d140` |
| `TUYUL-KARTEL-FX-JOURNAL-VAULT-AGI` | `codex/wla-00-ratification` | `a98f87a875944b7367375074d539d712e5954192` |
| `TUYUL-KARTEL-FX-KNOWLEDGE-VAULT-AGI` | `codex/wla-00-ratification` | `2c54821b3c6f5b90cfe53e5115c15f20e2c1a04d` |

Any change to a reviewed file invalidates these digests and requires a new
packet and receipt before ratification can become effective.

## 2. Constitutional owner and authentication

| Field | Recorded value |
| --- | --- |
| Legal/display name | `Dwi Kelana Putra` |
| Owner alias | `KELANA TJX` |
| Authority basis | `SYSTEM_OWNER_AND_REPOSITORY_OWNER` |
| GitHub login | `tjx578` |
| GitHub numeric subject ID | `221953664` |
| GitHub node ID | `U_kgDODTq-gA` |
| Issuer/trust anchor | `GitHub` verified-commit service and repository commit verification API |
| Authentication reference | `https://github.com/tjx578` plus immutable owner-attestation commit identity |
| Authentication time | `2026-08-24T07:29:18.577Z` decision time; commit time MUST be recorded by GitHub |
| Authentication role | Constitutional owner acting under `WLA00-EXC-001` |
| Signature reference | `PENDING_GITHUB_VERIFIED_OWNER_ATTESTATION_COMMIT` |
| Expiry/revocation check | `PENDING` until commit verification and signer association are validated |

The target WOLF15 baseline is
`7ff2a9194b22e185b35dc61574c61628ba404939`. Its commit is a technical
baseline, not the human signature. Runtime envelope keys are prohibited from
serving as governance-signing keys.

## 3. Single-owner bootstrap exception

Exception ID: `WLA00-EXC-001`

Reason: the system currently has one human owner and operator.

| Property | Recorded value |
| --- | --- |
| Multi-role independence achieved | `FALSE` |
| Backup assignments available | `FALSE` |
| Assumed roles | `ARO`, `WAO`, `JDS`, `MRR`, `SEC` |
| Concurrence mode | `OWNER_SELF_CONCURRENCE_EXCEPTION` |
| Reusable | `FALSE` |
| Expiry event | Completion of WLA-01 or any scope expansion, whichever occurs first |
| Separation-of-duties gate | `NOT_SATISFIED`; must be re-evaluated before broader authority |

Independent concurrence is recorded honestly:

| Role | Concurrence record |
| --- | --- |
| `WAO` | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |
| `JDS` | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |
| `MRR` | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |
| `SEC` | `NOT_AVAILABLE_SINGLE_OWNER_EXCEPTION` |

No backup concurrence is claimed. If another human acts later, a new role
assignment and authenticated decision are required.

## 4. Scope ceiling

The exception may authorize only:

- WLA-01 contract-only spike;
- schema and contract tests; and
- documentation and deterministic fixtures.

It does not authorize:

- runtime registration;
- database migration or outbox activation;
- dispatcher, broker, or EA access;
- deployment or production mutation;
- advisory activation or execution authority;
- creation of any learning repository; or
- Gate P0-A certification.

The exception grants no self-promotion path. Challenger and SHADOW remain
non-executing downstream concepts subject to later gates.

## 5. Conditions and conflicts

Conditions are the canonical RFC 8785 JSON value `[]` encoded as UTF-8.

Conditions hash:
`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.

There are no declared conditions. The multi-role conflict is explicit and is
accepted only through restriction-only exception `WLA00-EXC-001`. Any scope
expansion expires the exception and returns authorization to fail-closed.

## 6. Contract directions locked by this decision

- WOLF15 owns the initial source events
  `wolf15.alpha-fact.exported.v1` and
  `wolf15.outcome-evidence.exported.v1`.
- A Journal receipt is a distinct consumer-owned event and is not registered in
  WLA-01.
- `alpha-fact` MUST be a typed discriminated union backed by an allowlist.
- Unknown fact types, forbidden fields, and unknown nested schemas MUST be
  rejected fail-closed.
- WLA-01 is contract-only: no runtime registration, migration, dispatcher,
  broker, EA, or execution authority.

## 7. Signed-statement binding

The owner-attestation commit MUST bind these values exactly:

| Bound field | Value |
| --- | --- |
| Packet hash | Recomputed SHA-256 of this packet after publication |
| Target base SHA | `7ff2a9194b22e185b35dc61574c61628ba404939` |
| Verdict | `APPROVED` |
| Conditions hash | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |
| Role | `CONSTITUTIONAL_OWNER` assuming `ARO,WAO,JDS,MRR,SEC` under `WLA00-EXC-001` |
| Ratification ID | `de760418-7c42-4cfc-b1cf-a8f472aefba4` |
| Decision timestamp | `2026-08-24T07:29:18.577Z` |
| Reviewed combined digest | `c2905ff65b9dd9bf07da555ce1cd6ea1e2898432f6f49a5e5d98a7a6cbb6fb6d` |

Validation MUST confirm the commit is immutable/resolvable, is `Verified` by
GitHub, maps to subject `tjx578` / `221953664`, postdates the decision, is not
revoked or invalidated, and has not been replayed for another ratification ID.
Any mismatch results in `BLOCKED`.

## 8. Submitted declaration

The constitutional owner submitted this declaration:

> Saya, Dwi Kelana Putra (KELANA TJX), sebagai pemilik sistem dan repository,
> menyetujui WLA-00 dengan verdict APPROVED.
>
> Saya mengesahkan SINGLE_OWNER_BOOTSTRAP_EXCEPTION WLA00-EXC-001 karena saat
> ini seluruh fungsi governance berada pada saya sendiri.
>
> Otorisasi hanya berlaku untuk WLA-01 contract-only spike. Tidak mengizinkan
> runtime registration, database/outbox activation, deployment, broker/EA
> access, repo baru, Gate P0-A certification, atau production mutation.
>
> Conditions: []
>
> Saya mengizinkan pembuatan dan commit dokumen ratifikasi pada branch
> dokumentasi khusus melalui akun GitHub tjx578.

## 9. Effective-decision rule

The submitted verdict becomes canonical `PASS` and
`WLA_01_AUTHORIZED=TRUE` only after the signed-statement binding passes every
check and an immutable ratification decision record references the verified
attestation commit. Until then:

```text
WLA_00_RATIFICATION = NOT_EVALUATED
WLA_01              = NOT_STARTED
WLA_01_AUTHORIZED   = FALSE
REPOSITORY_MUTATION = DOCUMENTATION_ONLY_AUTHORIZED
RUNTIME_MUTATION    = NONE
```

Even after `PASS`, the authorization ceiling remains `CONTRACT_ONLY`. The
ratification does not create a repository, activate a workflow, satisfy
WLA-01/02/03, pass Gate P0-A, or grant production authority.

Early source research remains non-normative in the
[WLA-01 pre-charter research baseline](../wla-01-preparation/RESEARCH-BASELINE.md)
and does not itself start WLA-01.
