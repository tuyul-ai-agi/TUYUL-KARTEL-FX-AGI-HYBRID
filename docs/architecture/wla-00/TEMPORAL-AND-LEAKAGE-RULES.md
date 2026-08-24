# WLA-00 Temporal and Leakage Rules

Status: `PROPOSED`

## 1. Clock model

All instants use timezone-aware UTC. Source precision and clock-health metadata
are preserved. The following clocks are distinct:

| Clock | Meaning |
| --- | --- |
| `occurred_at_utc` | When the represented source-domain event occurred |
| `observed_at_utc` | When the authoritative producer first observed it |
| `source_published_at_utc` | When the producer made the event available on the approved export |
| `first_received_at_utc` | When WLA ingress first received the exported bytes |
| `ingested_at_utc` | When Journal durably accepted or quarantined those bytes |
| `learning_available_at_utc` | Earliest instant the validated artifact was legally eligible for learning use; never earlier than accepted ingestion and any additional policy gate |
| `maturity_at_utc` | Earliest instant an Outcome horizon can be complete |
| `sealed_at_utc` | When an Episode, Dataset, or manifest became immutable |
| `invalidated_at_utc` | When new use became prohibited; never backdated |

Required ordering under normal clocks is:

```text
occurred <= observed <= source_published <= first_received <= ingested <= learning_available
```

If domain semantics legitimately differ or clocks are uncertain, the event must
declare the reason, source precision, and uncertainty. An unexplained inversion
is quarantined. Ingestion code MUST NOT silently clamp, backdate, or rewrite
source timestamps. `learning_available_at_utc` is computed no earlier than the
maximum of source publication, first receipt, accepted ingestion, and any later
legal/policy availability constraint.

## 2. Bitemporal rule

WLA stores both:

- **valid time:** when a claim applies in the source domain; and
- **system/availability time:** when that version became legally knowable to WLA.

An as-of query selects the version whose `learning_available_at_utc` was eligible
at the requested cutoff. The currently latest corrected version is not
automatically visible in a historical replay.

## 3. Fact and Episode eligibility

- A Fact is eligible only after contract, provenance, integrity, and sequence
  validation.
- Episode membership uses a versioned policy, an explicit cutoff, deterministic
  ordering, and only eligible Facts available by the cutoff.
- Late Facts never mutate a sealed Episode. They may create a new Episode version
  or an invalidation/correction path.
- Missing sequence ranges and unresolved clock uncertainty remain visible in the
  Episode quality status.

## 4. Outcome Evidence and Outcome labeling

- Source-owned Outcome Evidence is an immutable Fact exported through the approved
  boundary. A learning-owned Outcome is a separate derived label; neither is a
  field backfilled into the original Alpha Fact.
- A label cannot mature before both its horizon and authoritative evidence are
  complete.
- Fills/rejects require source-owned execution evidence. Price touching a level
  is not proof of a fill.
- Multiple targets, stops, cancellations, partial fills, timeout/censoring, and
  unresolved broker evidence require explicit semantics.
- `PENDING`, `CENSORED`, and `UNKNOWN` samples are not silently mapped to loss,
  zero return, or negative class.
- Label-policy changes create new Outcome versions and new Dataset lineage.
- Every label records its policy owner/version, horizon start/end, finality rule,
  censoring rule, correction references, and `learning_available_at_utc`.

## 5. Point-in-time joins

For a row with decision cutoff `T`, every feature and linked claim must satisfy:

```text
learning_available_at_utc <= T
```

Join keys must include the correct entity, episode/lifecycle, source version, and
temporal interval. “Nearest” joins require a bounded, predeclared direction and
tolerance. Forward-looking nearest joins are prohibited.

Data availability from a file modification time, Git commit time, or current API
response is insufficient unless that time is the accepted source publication
clock.

## 6. Dataset splitting

Datasets MUST use:

- chronological train/validation/test boundaries;
- grouping that keeps the same Episode, lifecycle, trade, source event family,
  and duplicate/correction family in one partition;
- purge windows for samples whose feature or label intervals overlap a later
  partition;
- embargo after boundaries for declared horizon/dependency risk;
- frozen evaluation partitions not used for feature, label, or threshold design;
  and
- separate out-of-time evaluation when the protocol claims temporal robustness.

Random row splitting is forbidden. Cross-validation, walk-forward, and rolling
windows must fit all learned transforms separately within each training fold.

## 7. Transformation leakage controls

The following are fit on training data only:

- scaling, normalization, clipping bounds, and imputation;
- categorical vocabularies and encodings;
- feature selection and dimensionality reduction;
- resampling/class balancing;
- target transforms and calibration;
- threshold selection and early stopping; and
- retrieval corpora or embeddings used as model input.

Global statistics, future regime labels, final trade status, post-decision risk,
later reflections, dataset membership, and challenger/shadow outcomes are
forbidden features unless a separate point-in-time source proves they were
available at `T`.

## 8. Required leakage tests

| Test | Required result |
| --- | --- |
| Future-feature canary | Model/dataset build rejects a feature available after cutoff |
| Label-shift canary | Shifting outcomes into the future changes eligibility and exposes no earlier label |
| Late-arrival fixture | Earlier replay remains unchanged; new replay sees the late event only after availability |
| Revision fixture | Historical replay selects the then-available version, not latest revision |
| Duplicate/correction family split | All related records remain in one partition |
| Overlapping-horizon split | Purge/embargo removes cross-boundary dependency |
| Transform fit audit | Fit IDs and statistics reference training partition only |
| Timestamp parser | Naive, invalid-offset, DST-ambiguous, and inverted timestamps fail closed |
| Outcome authority test | Price touch without authoritative execution evidence cannot become a fill label |
| Unknown denominator test | Incomplete outcomes yield `NOT_MEASURED`, not a precision/win-rate value |
| Reflection exclusion test | Post-outcome reflection cannot enter pre-outcome features |
| Retrieval cutoff test | Adaptive-memory retrieval excludes documents unavailable at cutoff |

## 9. Reporting

Every metric reports numerator, denominator, eligibility policy, cutoff, horizon,
missingness/censoring, confidence or uncertainty, dataset/split digest, and code
revision. A metric without a matured denominator is `NOT_MEASURED`.
