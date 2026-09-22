<div align="center">

<img src="assets/svg/case-logo.svg" alt="006 — Textless Backdrop + Precise Type Overlay" width="620">

# 006 — Textless Backdrop + Precise Type Overlay

</div>

> Other languages: [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

Turn any image request that needs Chinese headlines, key numbers, or set styling into a composite: the model produces a **wordless backdrop**, then Pillow overlays the type with pixel-perfect accuracy. Use it for WeChat covers, Xiaohongshu / Xiaolüshu cards, posters, quote cards, and data-result cards.

## Highlights

- **The model draws the picture; scripts draw the text.** Asking an image model to render Chinese headlines reliably produces broken glyphs and wrong digits — a `$0.71` off by one is a hard defect on a cover. Overlaying with Pillow makes numbers 100% accurate and fonts never break.
- **Declarative card renderer.** The spec is plain JSON, coordinates written on a 1080-wide baseline and scaled to any canvas. Guardrails: font auto-fit, minimax balanced wrapping (shorten the *longest* line), and automatic vertical flow.
- **Cross-platform font finder.** Detects a real Chinese font and verifies it actually contains CJK glyphs (uses private-area codepoint `U+E000` to catch tofu blocks). Override with `SKILL_FONT` or `--font`.
- **Watermark stripper.** Model output carries a fixed "AI generated" watermark bottom-right; crop it, or patch it with a blurred average-color mask when it cannot be cropped.
- **Palette anchoring.** Lock four hex values before generation so the overlaid type always sits on the account's color board instead of fighting the base.

## Structure

| Path | What it holds |
|---|---|
| `SKILL.md` | Full method: palette lock, wordless base, watermark strip, type overlay, three pitfalls, delivery shape |
| `scripts/render_card.py` | Declarative card renderer — `--demo`, `--dump-spec`, `--spec`; guardrails built in |
| `scripts/find_font.py` | Cross-platform CJK font detection + tofu detection |
| `scripts/strip_watermark.py` | Watermark CLI — `crop` / `patch` modes |
| `scripts/selftest.py` | Environment self-check (14 assertions) |
| `references/pillow-recipes.md` | `overlay` / `band` / `side_dark` / `cover` / `pill` / `text` full source + layout cheat-sheet |
| `examples/01-step5-material-pack.md` | Full run: one WeChat article → 6 dual-platform assets |
| `examples/demo-card.json` | Editable spec template |
| `examples/demo-card.png` | `--demo` output |
| `templates/` | Card brief template |
| `evaluation/` | Acceptance checklist |
| `assets/svg/case-logo.svg` | Case logo |

## How to use

Requires Python 3 and Pillow (`pip install pillow`). Managed Python 3.13 ships without Pillow — use the prepared venv, or `python -m venv` then `pip install pillow` (through the `http://127.0.0.1:7890` proxy).

**Lock palette → generate wordless base → strip watermark → overlay type → verify.**

```bash
pip install pillow
python scripts/selftest.py                               # confirm env (14 assertions)
python scripts/render_card.py --demo -o demo.png         # pure-code render, no image model needed
python scripts/render_card.py --dump-spec > my-card.json
python scripts/render_card.py --spec my-card.json -o out.png
```

Flags: `--demo` render a sample card · `--dump-spec` export the template spec · `--spec` render from a JSON spec · `--font` override the font path · `--out` output path.

The scripts do **deterministic assembly only** — computing layout, fitting font size, compositing layers. Creative judgment (palette, metaphor, copy) stays with the caller.

## Three hard constraints

- The image-model prompt MUST include: `Absolutely no text, no letters, no words, no numbers, no watermark, no logo`.
- All Chinese and digits are overlaid by Pillow; never ask the model to render Chinese headlines.
- Semi-transparent elements go on an RGBA layer then `alpha_composite`; a darkening band uses solid color + alpha mask, never a dark→white gradient.

## Core principle

The model is responsible for the picture; the script is responsible for the text. What is *drawn* (not generated) is what stays correct — a digit wrong by one is a hard defect on a cover.

## Provenance

Extracted from a 2026-09-22 WeChat → Xiaolüshu dual-platform material-pack run (after `wechat-xiaolushu-material-pack` shipped): the "wordless base + precise overlay" step was peeled out as a standalone method. MIT License.
