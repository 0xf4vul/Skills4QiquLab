<div align="center">

<img src="assets/svg/case-logo.svg" alt="007 — X Cover & Copy Studio" width="620">

# 007 — X Cover & Copy Studio

</div>

Other languages: [简体中文](README.zh-CN.md) · standalone repo: [0xf4vul/x-cover-copy-studio](https://github.com/0xf4vul/x-cover-copy-studio)

> Distilled from a 2026-09-22 production session: turn **one listy tweet** into two
> launch-ready X.com posters (2.41:1 retro-paper + 16:9 dark index) **and one tweet
> variant** that keeps the original skeleton but swaps every hook line.

## Highlights

- **Reference-image deconstruction first.** Batch-read competitor posters with a vision
  model into a fixed field schema (copy / hex / type scale / ratio / layout / ornament),
  then design from the summed language — never from vibes.
- **HTML → Playwright 2x pipeline.** payload.json + token templates → exact 4000×1660 /
  3200×1800 PNGs. Byte-deterministic modulo sub-pixel noise (verified <0.05 % diff).
- **Hard row contracts, no silent残图.** paper caps at 7 rows, dark at 7+1 cards;
  overflow or missing fields exit non-zero with split/downgrade advice (failure injection tested).
- **Forced QA loop on every render.** crop-based pixel/vision checks: row count, footer clipping,
  occlusion, tofu, display-weight font — FAIL loops back to the layout budget.
- **Variant copy = keep skeleton, swap flesh.** Emoji hook → numbered value lines → save-CTA
  structure preserved; hooks/benefit-phrasings rewritten; facts (domains, counts) untouchable;
  advertising-law absolute terms stripped ("最吸睛" banned).

## Structure

| Path | What it holds |
|---|---|
| `SKILL.md` | Agent workflow: fit-gate → deconstruct → copy → payload → render → QA → budget |
| `templates/` | `poster-paper.html` (2000×830), `poster-dark.html` (1600×900), token slots |
| `scripts/` | `render.py` (payload→PNG), `qa_render.py` (QA crops + checklist) |
| `references/` | design recipes, copy formulas, **fit-guide.md** (when NOT to use) |
| `examples/case-pinterest-tools/` | 7 ref posters, 2 final PNGs, original + variant tweet, replayable payloads |
| `evaluation/` | checklist; scoring schema `../evaluation-schema.json` |
| `_meta.json` | machine-readable spec: contracts, palettes, runtime, license |

## Quick start

```bash
cd examples/case-pinterest-tools
python3 ../../scripts/render.py payload.paper.json out/   # 4000x1660
python3 ../../scripts/render.py payload.dark.json  out/   # 3200x1800
python3 ../../scripts/qa_render.py out/*.png              # QA crops
```

Requirements: `playwright` CLI + chromium; Google Fonts reachable (Noto Sans SC 900 /
IBM Plex Mono / Noto Color Emoji — the emoji family must stay explicit on Linux).

## Testing log (v1.1.0, 2026-09-22)

L1 replay exact sizes ✅ · L2 fresh topic no-code ✅ · L3 8-row/9-card/missing-field hard-fail ✅ ·
L5 45-char domain wraps without collapse ✅ · idempotency 0.019/255 MAD ✅ · no absolute paths in package ✅ ·
L4 invocation: accepted in fresh session incl. AD-law self-edit ✅

## License

Output assets: unlimited commercial use, no attribution required.
Source project: see [LICENSE.md](LICENSE.md) — no verbatim resale of the engine itself.
