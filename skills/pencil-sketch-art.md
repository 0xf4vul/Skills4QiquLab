# Pencil Sketch Art

## Purpose
Turn any subject, description, or abstract concept into a graphite pencil sketch that actually reads as hand-drawn.

## Critical boundary

**Text never goes into the image prompt. Copy is overlaid later in layout.**

Baking words into a generated sketch is the fastest way to ruin it: models render garbled glyphs, and you lose control of typography. Generate a wordless base image, then place the text in composition or layout.

## Use when
An article, card, cover, or post needs an illustration that feels drawn by hand rather than rendered.

## Do not use when
The deliverable needs precise information, legible labels, or a data story — that is an infographic, not a sketch.

## Three hard constraints
- Words inside the image: at most 8. Anything longer goes to layout.
- At most one low-saturation hue. Background must be paper tone, never pure white `#ffffff`.
- Generation parameters fixed: `quality=high`, `style=natural`. Vivid destroys graphite texture.

## Workflow
Name the subject → pick aspect → pick stroke preset → build the prompt → generate → crop to publish size → self-check.

## Concept translation
Abstract concepts cannot be drawn literally. Convert each into **one concrete object plus one action**: "involution" becomes a man running on a treadmill that is plugged into a spinning wall clock. The object carries the meaning; the action carries the tension.

## Stroke presets
Line art / hatched tonal / charcoal rough / pencil wash / scene perspective / conceptual metaphor.

## Aspect ratios
WeChat cover 2.35 (900×383) · article body ≤1080 wide · Xiaohongshu 3:4 · video cover 9:16 · quote card 2:3.

## Failure modes
- Looks photorealistic or 3D-rendered — strengthen the stroke tokens before adding more negative words.
- Background went pure white — the single fastest signal that it stopped being a sketch.
- Lines too clean and vector-like — add wobble and broken outlines.
- Text in the image is garbled — remove it from the prompt and overlay in layout.
- Subject crowds the title area — hanging or extending subjects (cords, pipes, trees) break top-padding constraints; locate a clean band instead of regenerating.

## Self-check
Reads as pencil at a glance / hatching visible / paper grain visible / lines wobble / no plastic or 3D feel / at most one hue / text ≤8 characters / background is paper tone / contrast is present / title area is clear.

## Evaluation
Hand-drawn fidelity / concept accuracy / composition cleanliness / title-area safety / publish-size readiness.

## Full case
Method detail, prompt library, scripts and published output: [cases/004_pencil-sketch-art/](../cases/004_pencil-sketch-art/)
