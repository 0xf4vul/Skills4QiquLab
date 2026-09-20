# Prompt Compression

## Purpose
Compress a prompt while preserving the user's intent, hard constraints, important relationships, and output semantics.

## Use when
A prompt is repetitive, verbose, or contains redundant wording.

## Do not use when
Compression would remove information needed to express temporal relationships, causal relationships, spatial relationships, character consistency, safety constraints, or other semantics.

## Workflow
1. Extract the task goal.
2. Separate hard constraints from descriptive decoration.
3. Detect duplicated or low-information wording.
4. Merge equivalent constraints.
5. Preserve ordering and dependencies where they carry meaning.
6. Re-read the compressed prompt against the original.
7. If any important semantic relationship is lost, restore it.

## Output contract
Return the compressed prompt and, when useful, a short preservation note.

## Failure modes
- Over-compression makes the prompt shorter but less executable.
- Removing transition words can break temporal logic.
- Merging separate actions can change the intended sequence.
- Removing camera or spatial constraints can change the visual result.

## Evaluation
Intent preservation / hard-constraint preservation / relationship preservation / execution clarity / length reduction.
