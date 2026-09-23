# Case 008 · IP Visual Evolution Engine

**Turn one person's identity, ability, values and growth story into a sustainable, continuously-evolving visual IP — then compress it into a 6-frame Xiaohongshu / WeChat Xiaolvshu narrative and a portable X.com Banner.**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

## What it does

Most personal-IP visual work is produced image by image: one avatar today, one poster tomorrow, one banner the day after — each with a brand-new prompt, character redesign and style. The result looks like six posters from six different designers.

This Engine turns that into a reusable pipeline: define the **Visual IP DNA** and **Continuity Contract** once, then let every image be the **next state transition of the same IP state machine**, not a new creation.

**Output**: six 3:4 vertical "six-shot" knowledge cards (one continuous cinematic take) + one X.com-ready banner master (FRAME 06 adapted to 1500×500).

## Pipeline

```
Identity → Visual IP DNA → Continuity Contract → Six-Frame State Machine
        → Platform Adapter → Banner Adapter → Vision QC
```

## Six-Frame State Machine

| Frame | Stage | State transition |
|---|---|---|
| 01 | MASTER | Establish the whole visual world |
| 02 | IDENTITY | Profession → Core Ability → Visual Metaphor |
| 03 | EVOLUTION | `CHAOS→FLOW→SYSTEM→SILENCE→PRESENCE` |
| 04 | CONTINUITY | Identity + Motion + World continuity |
| 05 | ENTROPY / WEIGHT | Entropy down, visual weight redistributed |
| 06 | PRESENCE / BANNER | Final hero, X.com 1500×500 ready |

## Platform Adapters (each fully self-contained)

| Platform | Continuity method | Strategy |
|---|---|---|
| Seedream | Multi-reference / sequential | Full Creative Brief + reference image |
| GPT | Conversational layered edit | `KEEP EXACTLY` / `CHANGE ONLY` |
| Grok | Continuous visual director | Frame-to-frame narrative + explicit frame numbering |
| Gemini | Reference + conversation | Previous image as primary reference + character naming + five dimensions |

Open any adapter file and you can run the whole 6-frame flow with that platform alone:

- [`references/adapters/seedream.md`](references/adapters/seedream.md)
- [`references/adapters/gpt.md`](references/adapters/gpt.md)
- [`references/adapters/grok.md`](references/adapters/grok.md)
- [`references/adapters/gemini.md`](references/adapters/gemini.md)

## How to start

1. Fill [`templates/fill-in-sheet.md`](templates/fill-in-sheet.md) (or reuse the worked example [`examples/zhuji-mao/`](examples/zhuji-mao/)).
2. Pick a platform adapter and generate frame by frame: MASTER → 02–05.
3. Finish with the **Banner Adapter** (in [`SKILL.md`](SKILL.md) §7) to adapt FRAME 06 to X.com 1500×500.
4. Run [`evaluation/evaluation-schema.json`](evaluation/evaluation-schema.json); repair the broken frame locally if below threshold.

## Files

- `SKILL.md` — Engine core: formula, pipeline, DNA, Continuity Contract, six-frame state machine, adapter selection, Banner Adapter, QC, evaluation.
- `references/adapters/*.md` — four self-contained platform flows.
- `templates/fill-in-sheet.md` — one-time DNA definition (blank).
- `examples/zhuji-mao/` — worked "Zhuji Mao" (筑基猫) values.
- `evaluation/evaluation-schema.json` — heuristic local evaluation.

## Core formula

`IP VISUAL EVOLUTION = Identity Continuity × Narrative Continuity × Motion Continuity × Entropy Gradient × Visual Weight × Spatial Continuity × Aura Refinement × Platform Adaptation`

**Change the subject. Keep the Engine.**
