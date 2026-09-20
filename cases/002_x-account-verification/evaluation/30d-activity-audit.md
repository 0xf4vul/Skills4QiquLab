# Evaluation Dataset — 30D Activity Audit

Execution date: 2026-09-20
Nominal 30D window: 2026-08-22 through 2026-09-20

This dataset separates verified identity, auditable observed posts, and complete 30D counts. An observed sample is never presented as a complete 30D count.

| Person | Account | Identity | 30D completeness | Posts 30D | Original | Repost | Quote | Reply | AI | Tech |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Diogo Mónica | @diogomonica | CONFIRMED | Partial / not exhaustive | Unverified | Unverified | Unverified | Unverified | Unverified | Partial | Partial |
| Pedro Mota | @iPedroMota | PROBABLE | Timeline not auditable | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified |
| Tiago Coelho | @tiagofscoelho | CONFIRMED | Timeline not auditable | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified | Unverified |

## Auditable observed-post sample

These rows are evidence samples, not exhaustive counts.

| Person | Account | Observed date | Type | Topic | Evidence |
|---|---|---|---|---|---|
| Diogo Mónica | @diogomonica | 2026-09-18 approx. | Original | Technology / AI | TwStalker timeline snapshot |
| Diogo Mónica | @diogomonica | 2026-09-18 approx. | Repost | Technology / Crypto | TwStalker timeline snapshot |
| Diogo Mónica | @diogomonica | 2026-09-03 approx. | Repost | Crypto / Technology | TwStalker timeline snapshot |
| Diogo Mónica | @diogomonica | 2026-09-03 approx. | Original | Technology / Business | TwStalker timeline snapshot |
| Diogo Mónica | @diogomonica | 2026-09-01 approx. | Repost | AI / Technology | TwStalker timeline snapshot |
| Diogo Mónica | @diogomonica | 2026-08-31 | Original | VC / Investing | Personal blog archive |
| Diogo Mónica | @diogomonica | 2026-08-28 | Original | Security / Technology | Personal blog archive |
| Pedro Mota | @iPedroMota | — | — | — | X profile identifiable; no auditable 30D timeline sample exposed |
| Tiago Coelho | @tiagofscoelho | — | — | — | Account identity corroborated; no auditable 30D timeline sample exposed |

## Identity evidence

### Diogo Mónica
- Personal contact page explicitly lists X @diogomonica.
- LinkedIn lists twitter.com/diogomonica.
- Independent profile data maps the same X username to Diogo Mónica.
- Status: CONFIRMED.

### Tiago Coelho
- WordCamp Porto participant listing associates Tiago Coelho with @tiagofscoelho and Pixelmatters.
- Independent profile data describes @tiagofscoelho as a Porto-based Tiago Coelho and CTO at Pixelmatters.
- Status: CONFIRMED.

### Pedro Mota
- X profile @iPedroMota exists and identifies itself as Pedro Mota with a YouTube link.
- The same ipedromota identity is used by a long-running YouTube channel and Instagram account.
- Available evidence does not establish that this Pedro Mota is the exact Porto Tech Hub guest with sufficient certainty.
- Status: PROBABLE, not CONFIRMED.

## Rules demonstrated

1. A blog post date is not automatically an X post date.
2. A third-party timeline snapshot can establish an observed post, but not a complete 30D total unless the entire window is auditable.
3. AI/Tech ratios remain Partial when only a sample is available.
4. No exact 30D count is inferred from follower counts, search-result counts, or third-party summaries.
5. PROBABLE accounts stay outside a strict confirmed-only shortlist.

## Reproducibility
- checked_at: 2026-09-20
- window_start: 2026-08-22
- window_end: 2026-09-20
- completeness: explicit per account
- evidence type: official profile / professional profile / third-party timeline / content archive

## External evidence
- https://diogomonica.com/contact
- https://www.linkedin.com/in/diogomonica
- https://blog.diogomonica.com/
- https://porto.wordcamp.org/2024/participantes/
- https://twitter.com/iPedroMota/with_replies
- https://socialblade.com/youtube/handle/ipedromota
