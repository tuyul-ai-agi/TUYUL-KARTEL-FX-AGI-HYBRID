---
id: ADR-006
title: Authority and capability isolation
status: PROPOSED
date: 2026-08-24
---

# ADR-006: Authority and capability isolation

## Context

Naming a service “observer”, “journal”, or “shadow” does not remove its technical
capabilities. Legacy surfaces include repository mutation, remote dispatch, model
parameter mutation, and metric-based auto-merge. Capability must be denied by
architecture, credentials, network policy, and tests.

## Decision

Each component receives the minimum capabilities in the ownership matrix. No WLA
service identity may have WOLF15 write credentials, broker/EA credentials,
execution queue access, deployment/promotion credentials, or permission to merge
its own changes.

The following separations are mandatory:

- producer and consumer identities are distinct;
- raw evidence storage and derived projections are distinct;
- dataset construction and model evaluation are distinct;
- challenger creation and gate approval are distinct;
- SHADOW runtime and WOLF15 runtime are distinct failure domains;
- CI verification and deployment/promotion authority are distinct; and
- emergency kill/disable authority cannot be used to enable capability.

Automated learning may ingest, group, replay, reflect, build sealed datasets,
train challengers, and evaluate in SHADOW after its stage gates pass. Automation
stops at evidence production. Only authorized humans may approve a gate or any
future transition beyond SHADOW.

A human approval service is not an escape hatch: it must authenticate the actor,
enforce separation of duties, bind the reviewed hashes, record reason and expiry,
and reject self-approval.

## Consequences

- Compromise of a learning component cannot directly alter Alpha or execute.
- A model can be excellent and still remain a Challenger indefinitely.
- Operational convenience such as shared tokens or one repository bot is not a
  valid reason to collapse roles.

## Rejected alternatives

- **Trust code conventions alone.** Rejected because a token or egress path can
  bypass intent.
- **Let CI promote when thresholds pass.** Rejected because measurement is not
  approval and can be poisoned.
- **Share WOLF15 credentials read/write but promise read-only use.** Rejected;
  authority is defined by possible actions, not expected behavior.

## WLA-00 acceptance

- Reviewers accept the capability ceiling and separation-of-duties model.
- Every prohibited authority maps to the authority rules, ownership matrix, threat
  boundary, and a named downstream evidence obligation.

## Downstream conformance obligations

The following capability and runtime proofs are `NOT_EXECUTED` during WLA-00:

- Capability inventory maps identities to concrete permissions and egress.
- Negative tests demonstrate prohibited calls fail before request execution.
- No WLA secret can authenticate to broker, EA, WOLF15 mutation, merge, or deploy
  surfaces.
- Human gate records bind exact evidence and prohibit self-approval.
