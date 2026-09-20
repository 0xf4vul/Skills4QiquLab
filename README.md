# Skills4QiquLab

> A practical lab for reusable AI Skills, prompt workflows, model adapters, examples, and evaluation patterns.

Skills4QiquLab is a flat, practical collection of reusable AI Skills. The goal is not to collect prompts, but to turn repeated AI work into explicit, testable, portable workflows.

## Core loop

**Problem → Skill → Template → Example → Evaluation → Iteration**

## What is a Skill?

A Skill is a reusable instruction layer that helps an AI consistently perform a class of tasks. A good Skill captures the task boundary, reasoning workflow, constraints, output contract, failure modes, and adaptation rules.

## Repository map

- [skills.md](skills.md) — Skill index and selection guide
- [templates.md](templates.md) — reusable Skill-authoring templates
- [skills/](skills/) — individual Skills
- [examples/](examples/) — compact before/after examples and evaluation cases

## Current Skills

| Skill | Purpose |
|---|---|
| Prompt Compression | Compress prompts without destroying semantic constraints |
| Prompt Optimization | Improve prompts while preserving user intent |
| Prompt Reverse Engineering | Recover reusable structure from strong prompts |
| Video Prompt Compression | Reduce video prompts while preserving temporal semantics |
| Video Prompt Optimization | Improve video prompts for clarity and model execution |
| Web Research | Turn open-ended research into a structured evidence workflow |
| X Research | Research people, accounts, and topics on X |
| Skill Builder | Design, test, and iterate reusable Skills |

## Design principles

**Useful over comprehensive** — each Skill should solve a real recurring problem.

**Semantic preservation over maximum compression** — shorter is not automatically better.

**Model-aware, model-agnostic where possible** — preserve a stable core and isolate model-specific adaptation.

**Examples over claims** — show original input, transformation, output, and evaluation.

**Failure modes are first-class** — document when a Skill should not be used and what can go wrong.

**Flat by default** — avoid deep folder hierarchies until scale actually requires them.

## Roadmap

`V1 Skill Collection → V2 Skill Registry → V3 Evaluation / Benchmark → V4 Web Interface → V5 Skill Ecosystem`

## License

MIT
