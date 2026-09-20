# Video Prompt Optimization

## Purpose
Improve a video prompt so a model can execute the intended subject, action, camera, timing, and scene continuity more reliably.

## Workflow
Intent → subject continuity → action chain → temporal structure → camera → environment → style → constraints → validation.

## Core representation
`Subject + Action + Time + Camera + Context + Constraints`

## Important rule
Do not add motion merely because a prompt is a video prompt. Motion should express the intended visual meaning.

## Failure modes
Over-directed movement / contradictory camera instructions / unnecessary cinematic jargon / loss of subject identity / too many simultaneous actions.

## Evaluation
Action clarity / temporal coherence / camera coherence / subject consistency / model executability.
