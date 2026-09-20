# 30D Activity Evaluation Checklist

## Identity gate
- [x] Identity evidence is recorded before activity analysis.
- [x] CONFIRMED and PROBABLE are separated.
- [x] Name matching alone never confirms an account.

## Timeline acquisition gate
- [x] Execution date and exact 30D window are explicit.
- [x] Timeline acquisition is a separate gate from identity verification.
- [x] Timeline status uses TIMELINE_ACQUIRED / TIMELINE_PARTIAL / TIMELINE_NOT_ACQUIRED / 30D_VERIFIED.
- [x] A complete count requires the entire target window to be auditable.

## Per-post evidence gate
- [x] Every counted post must retain a direct platform post URL and/or post ID.
- [x] Exact timestamp/date is retained.
- [x] Original / Repost / Quote / Reply are separate fields.
- [x] Topic classification is attached to the individual evidence row.
- [x] Other-platform content is never converted into target-platform activity.

## Content gate
- [x] AI and Tech ratios are marked Partial when the sample is incomplete.
- [x] Search-result counts, follower counts, blog dates, and third-party summaries are never used as posting estimates.
- [x] Missing values remain missing rather than being fabricated.

## Acceptance criterion
**Only 30D_VERIFIED may output an exact posts_30d / original_30d / repost_30d / quote_30d / reply_30d count.** Otherwise use Unverified or Partial.