<div align="center">

<img src="assets/svg/case-logo.svg" alt="004 — Pencil Sketch Art" width="620">

# 004 — Pencil Sketch Art

</div>

> Other languages: [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

Turn any subject, description, or abstract concept into a graphite pencil sketch — delivered as a single image, independent of any layout or infographic pipeline.

## Highlights

- **Abstract concepts get translated, not described.** "Burnout culture" cannot be drawn; a man sprinting on a treadmill plugged into a spinning wall clock can. Five worked translations ship in `references/prompt-library.md`.
- **Six stroke presets.** Line art / hatched tonal / charcoal rough / pencil wash / urban scene / conceptual metaphor.
- **Two runnable scripts.** `build_prompt.py` assembles the prompt and hard-rejects baked-in text longer than 8 characters. `crop.py` locates the subject by per-row ink density, so a cover can be re-cropped to any ratio without regenerating — and without ever looking at the image.
- **Text never enters the prompt.** Figures are generated wordless; copy is overlaid in layout. Baked-in text is the single most common way an otherwise good sketch is ruined.
- **Paper, never white.** Cream paper grain is the fastest signal separating a sketch from digital painting.

## Structure

| Path | What it holds |
|---|---|
| `SKILL.md` | Full method: subject decision, aspect rules, stroke presets, prompt assembly, 8-item self-check |
| `scripts/build_prompt.py` | Prompt constructor — `--list` for presets; validates text length, aspect, accent, lighting |
| `scripts/crop.py` | Ink-profile cropper — `--ratio`, `--top-safe`, `--bottom-safe`, `--dry-run` |
| `scripts/presets.json` | Preset data: stroke / medium / shading / composition / negatives. Tune the data, not the code |
| `references/prompt-library.md` | Concept → object translations, per-subject prompt patterns |
| `references/style-tokens.md` | Nine token buckets: medium / stroke / light / paper / color / quality / negative / aspect / params |
| `references/troubleshooting.md` | 16 failure modes → root cause → fix |
| `examples/` | Four full cases, including an eight-card quote series |
| `templates/` | Sketch brief template |
| `assets/gallery/` | Published output |

## How to use

Requires Python 3. `build_prompt.py` has no third-party dependencies; `crop.py` needs `pip install pillow`.

**Name the subject → pick an aspect → pick a stroke → build the prompt → generate → crop → self-check.**

```bash
python scripts/build_prompt.py --list
python scripts/build_prompt.py -s "a paper boat drifting on a sea of folded resumes" -p 3 -a portrait
python scripts/crop.py --in raw.png --ratio 2.35 --bottom-safe 0.26 --width 900 --out cover.png
```

Flags: `-s` subject · `-p` stroke (1-6, key, or Chinese name) · `-a` aspect · `--accent` accent color · `--light` light source · `-t` in-image text (≤8 chars) · `-o` output file.

The scripts do **deterministic assembly only** — joining tokens, computing size, validating length. Creative judgment stays with the caller.

## Three hard constraints

- In-image text **≤ 8 characters**; longer copy always goes on a wordless base image and gets overlaid in layout
- **At most one** low-saturation hue; background must be paper tone; **pure white is forbidden**
- Generation params fixed at `quality=high`, `style=natural` (vivid destroys graphite texture)

## Publish ratios

WeChat cover **2.35** (900×383) · article body **≤1080 wide** · Xiaohongshu **3:4** · Channels **9:16** · quote card **2:3**

## Core principle

Subtract, don't add. What is *missing* from a drawing usually carries the meaning — the abacus lies face-down, the water meter is absent, the desk lamp is switched off.

## Provenance

Extracted from `infographic-maker`: the hand-drawn style layer was peeled off its layout and composition constraints so it can run standalone. The source skill is unchanged. MIT License.
