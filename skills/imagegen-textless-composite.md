# Textless Backdrop + Precise Type Overlay

## Purpose
Turn any image request that needs Chinese headlines, key numbers, or set styling into a composite: the model produces a wordless backdrop, then Pillow overlays the type with pixel-perfect accuracy. Numbers stay 100% correct and fonts never break.

## Critical boundary

**The image model never renders text. Copy and digits are overlaid later with Pillow.**

Asking a model to draw Chinese headlines or numbers produces broken glyphs, dropped strokes, and wrong digits — a `$0.71` off by one is a hard defect on a cover. Generate a wordless base, then place the type in layout.

## Use when
A cover, card, poster, or quote card needs a Chinese headline, a key number (price, score, percentage), or a consistent palette across a set of assets.

## Do not use when
The deliverable is a pure atmospheric illustration, a wordless sketch, or an abstract texture — there is nothing to overlay, so just generate directly.

## Workflow
Lock the palette → generate a wordless base → strip the watermark → overlay the type → verify.

### Lock the palette
Fix four hex values before generation so the overlay always sits on the account color board:
- Deep `#0E1A2E` (base) · Accent `#E8A33D` (amber) · Positive `#5CD6A6` (mint, advantage only) · Ink `#F4F6FA` (near-white, secondary `#96A8C6`).
Write the palette into the base-image prompt, or the model's colors will drift and the overlay will not hold.

### Generate a wordless base
Three-part prompt: subject + scene/atmosphere + texture/style, ending with a mandatory negative block:
`Absolutely no text, no letters, no words, no numbers, no watermark, no logo.`
Pick size by placement: `1536x1024` (landscape cover) · `1024x1024` (square) · `1024x1536` (portrait card), `quality=high`.

### Strip the watermark
Model output carries a fixed "AI generated" watermark bottom-right (~90×60 px). Crop it when possible; when it cannot be cropped, patch with a blurred average-color mask from the area above-left (`scripts/strip_watermark.py`).

### Overlay the type
Use `scripts/render_card.py` (declarative) or write your own from `references/pillow-recipes.md`. The spec is plain JSON on a 1080-wide baseline, scaled to any canvas. Guardrails: font auto-fit, minimax balanced wrapping, automatic vertical flow. Bold comes from `stroke_width` on a real font, not a separate bold font file.

### Verify
Every number traces to a source · font size ≥ 24px and contrast sufficient (add a dark band if needed) · a set shares base/accent/font/metaphor · watermark fully removed.

## Three hard constraints
- The image-model prompt MUST include: `Absolutely no text, no letters, no words, no numbers, no watermark, no logo`.
- All Chinese and digits are overlaid by Pillow — never ask the model to render Chinese headlines.
- Semi-transparent elements go on an RGBA layer then `alpha_composite`; a darkening band uses solid color + alpha mask, never a dark→white gradient (which whites out the bottom).

## Failure modes
- Garbled baked-in text — remove it from the prompt; overlay in layout.
- Wrong number on the card — verify every digit against the source before delivery.
- Tofu / missing glyphs — `find_font.py` detects a real CJK font and flags tofu via the `U+E000` private-area probe; override with `SKILL_FONT` or `--font`.
- Palette drift — re-lock the four hex values and put them in the base prompt.
- Watermark visible — crop, or patch with the blurred average-color mask.
- Low-contrast text — add a solid-color + alpha-mask dark band, not a gradient.
- Text overflow — the renderer auto-fits and flows; for extreme copy, run `--demo` first.
- Inconsistent set — reuse one spec base across the set.

## Evaluation
Wordless base / number accuracy / font integrity / palette anchoring / watermark removed / contrast / no overflow / set consistency.

## Full case
Method detail, scripts, references, and a full worked example: [cases/006_imagegen-textless-composite/](../cases/006_imagegen-textless-composite/)
