# Video Prompt Compression

## Purpose
Compress video prompts while preserving the temporal and visual semantics required for a coherent clip.

## Critical boundary

**Do not optimize for the shortest possible prompt. Optimize for the shortest prompt that still preserves the video's meaning.**

Video is different from a static image: action order, duration, transitions, camera movement, subject continuity, and cause/effect relationships can carry meaning. If these are compressed too aggressively, motion may become abrupt, contradictory, or semantically incomplete.

## Use when
A video prompt is verbose or repetitive and needs to become easier to maintain or adapt.

## Do not use when
The apparent redundancy actually describes distinct beats, transitions, camera movement, timing, or dependencies.

## Preserve at minimum
Subject identity / action / action order / temporal relationships / camera behavior / scene continuity / critical style or physical constraints.

## Compression workflow
Parse → mark semantic units → classify hard vs decorative language → merge only equivalent units → preserve temporal markers → validate the resulting action chain.

## Action-chain test
Before compression:
`A → transition → B → reaction → C`

After compression, the chain must still be recoverable. If it becomes ambiguous, compression went too far.

## Model adaptation
Different video models may respond differently to density, explicit timing, camera terminology, and negative constraints. Keep the semantic core stable; place model-specific wording in an adaptation layer rather than changing the meaning.

## Failure modes
- Over-compression removes a critical action.
- Multiple actions collapse into one unnatural motion.
- Camera movement disappears.
- Temporal ordering becomes ambiguous.
- Character/object continuity is lost.
- A transition is mistaken for decoration.

## Evaluation
Semantic preservation / temporal coherence / action continuity / camera continuity / output usefulness / compression ratio.
