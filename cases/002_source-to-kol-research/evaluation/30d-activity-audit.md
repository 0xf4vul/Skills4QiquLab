# Evaluation Dataset — 30D Activity Audit

Execution date: 2026-09-20
Nominal 30D window: 2026-08-22 through 2026-09-20

This is a research-quality evaluation dataset for Source-to-KOL Research. Identity verification, timeline acquisition, individual post evidence, and complete 30D aggregation are separate gates.

## Dataset status

| Person | Account | Identity | Platform | Timeline status | 30D status |
|---|---|---|---|---|---|
| Diogo Mónica | @diogomonica | CONFIRMED | X | TIMELINE_NOT_ACQUIRED | Unverified |
| Pedro Mota | @iPedroMota | PROBABLE | X | TIMELINE_NOT_ACQUIRED | Unverified |
| Tiago Coelho | @tiagofscoelho | CONFIRMED | X | TIMELINE_NOT_ACQUIRED | Unverified |

## Evidence rule

No direct post URL / post ID has been retained as a sufficiently auditable sample for these accounts. Therefore no exact 30D count is claimed.

This is intentional: a research Skill must prefer an explicit evidence gap over a plausible-looking dataset.

## What does not count as platform-post evidence

- A personal blog article published on the same date.
- A LinkedIn post or repost.
- A search-result snippet without a direct post URL / ID.
- A third-party profile summary without the underlying post evidence.
- An approximate date inferred from an inaccessible timeline snapshot.

## Required per-post evidence schema

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
4. Other-platform content cannot be silently converted into target-platform activity.
5. CONFIRMED and 30D_VERIFIED are separate states.
6. When acquisition fails, record the failure explicitly.

## Next research sequence

**Diogo Mónica complete timeline → 30D_VERIFIED → reuse the same evidence pipeline for Tiago Coelho → then Pedro Mota after identity resolution.**