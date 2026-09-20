# Evaluation Dataset — 30D Activity Audit

Execution date: 2026-09-20
Nominal 30D window: 2026-08-22 through 2026-09-20

This is a **research-quality evaluation dataset**, not a fabricated “complete” KOL table. Identity verification, timeline acquisition, individual post evidence, and complete 30D aggregation are separate gates.

## Dataset status

| Person | Account | Identity | Timeline status | 30D status | Posts 30D | Original | Repost | Quote | Reply | AI | Tech |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| Diogo Mónica | @diogomonica | CONFIRMED | TIMELINE_NOT_ACQUIRED | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified |
| Pedro Mota | @iPedroMota | PROBABLE | TIMELINE_NOT_ACQUIRED | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified |
| Tiago Coelho | @tiagofscoelho | CONFIRMED | TIMELINE_NOT_ACQUIRED | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified |

## Auditable post evidence

**Current state: no direct X post URL / post ID has been retained as a sufficiently auditable sample for these three accounts. Therefore the previous approximate TwStalker rows and blog rows have been removed from the X 30D evidence table.**

This is intentional: a research Skill must prefer an explicit evidence gap over a plausible-looking dataset.

### What does not count as an X post sample

- A personal blog article published on the same date.
- A LinkedIn post or repost.
- A search-result snippet without a direct X post URL / ID.
- A third-party profile summary without the underlying post evidence.
- An approximate date inferred from an inaccessible timeline snapshot.

## Identity evidence

### Diogo Mónica
- Personal contact page explicitly lists X @diogomonica.
- LinkedIn lists twitter.com/diogomonica.
- Status: **CONFIRMED**.
- 30D status: identity confirmed, timeline not acquired.

### Tiago Coelho
- WordCamp Porto participant information associates Tiago Coelho with @tiagofscoelho and Pixelmatters.
- Status: **CONFIRMED**.
- 30D status: identity confirmed, timeline not acquired.

### Pedro Mota
- @iPedroMota identifies itself as Pedro Mota and is cross-linked with the same public creator identity.
- Available evidence does not establish with sufficient certainty that this is the exact Porto Tech Hub guest.
- Status: **PROBABLE**, not CONFIRMED.
- 30D status: identity unresolved to the required confidence level; timeline not acquired.

## Required per-post evidence schema

For every future auditable row, retain:

| Field | Requirement |
|---|---|
| account | Exact platform handle |
| post_url | Direct post URL |
| post_id | Platform post ID when available |
| published_at | Exact timestamp/date |
| type | Original / Repost / Quote / Reply |
| topic | AI / Tech / other taxonomy |
| evidence_checked_at | Date checked |
| source | Direct platform evidence |

## Reproducibility rules

1. A complete 30D count requires the entire target window to be auditable.
2. Every counted post must be traceable to a direct post URL / ID.
3. Partial samples may demonstrate methodology but cannot produce exact totals.
4. Other-platform content cannot be silently converted into X activity.
5. CONFIRMED and 30D_VERIFIED are separate states.
6. When acquisition fails, record the failure explicitly and continue research only when the required evidence becomes available.

## Next research sequence

**Diogo Mónica complete timeline → 30D_VERIFIED → reuse exact evidence pipeline for Tiago Coelho → then Pedro Mota after identity resolution.**

The dataset is deliberately incomplete because the evidence is incomplete.
