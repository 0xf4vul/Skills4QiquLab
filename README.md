<div align="center">

<img src="assets/qiqulab-logo.svg" alt="Qiqu.Lab — 奇趣实验室" width="760">

# Skills4QiquLab

**A practical AI Skill repository for turning effective AI working methods into reusable Skills and supporting resources.**

<p>
  <img src="https://img.shields.io/github/stars/0xf4vul/Skills4QiquLab?style=flat-square&label=Stars">
  <img src="https://img.shields.io/github/forks/0xf4vul/Skills4QiquLab?style=flat-square&label=Forks">
  <img src="https://img.shields.io/badge/Skills-8-4c9aff?style=flat-square">
  <img src="https://img.shields.io/badge/Cases-2-7c5cff?style=flat-square">
  <img src="https://img.shields.io/github/license/0xf4vul/Skills4QiquLab?style=flat-square&label=License">
</p>

**English** · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

</div>

## Community

No standalone public group is currently listed. Use [Issues](https://github.com/0xf4vul/Skills4QiquLab/issues) for discussion, feedback, and requests; use [Pull Requests](https://github.com/0xf4vul/Skills4QiquLab/pulls) for contributions.

## New Skills

- [Video Prompt Compression](skills/video-prompt-compression.md) — compress video prompts while preserving action order, temporal relationships, camera behavior, and continuity.
- [Video Prompt Optimization](skills/video-prompt-optimization.md) — improve video prompt execution across action, timing, camera, and subject continuity.
- [X Research](skills/x-research.md) — make X-account and information-source research reproducible and evidence-based.

## Featured Projects

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="cases/001_video-prompt-compression/"><img src="cases/001_video-prompt-compression/assets/svg/case-logo.svg" alt="Video Prompt Compression" width="88%"></a>
<br><strong>Video Prompt Compression</strong><br>
Compress video prompts without collapsing meaningful action chains, temporal relationships, camera logic, or subject continuity.
<br><a href="cases/001_video-prompt-compression/">Case</a> · <a href="skills/video-prompt-compression.md">Skill</a>
</td>
<td width="50%" valign="top" align="center">
<a href="cases/002_source-to-kol-research/"><img src="cases/002_source-to-kol-research/assets/svg/case-logo.svg" alt="Source-to-KOL Research" width="88%"></a>
<br><strong>Source-to-KOL Research</strong><br>
Turn arbitrary inputs into a verifiable, auditable research workflow for KOLs and information sources.
<br><a href="cases/002_source-to-kol-research/">Case</a> · <a href="skills/x-research.md">Skill</a>
</td>
</tr>
</table>

## Skill Entry

| | Skill | What it does |
|---|---|---|
| 🧩 | [Prompt Compression](skills/prompt-compression.md) | Reduce prompt redundancy while preserving intent and hard constraints |
| ✨ | [Prompt Optimization](skills/prompt-optimization.md) | Improve clarity, structure, and execution reliability |
| 🔬 | [Prompt Reverse Engineering](skills/prompt-reverse-engineering.md) | Extract reusable decision structures from strong prompts |
| 🎬 | [Video Prompt Compression](skills/video-prompt-compression.md) | Compress video prompts while preserving temporal semantics |
| 🎥 | [Video Prompt Optimization](skills/video-prompt-optimization.md) | Improve action, timing, camera, and subject continuity |
| 🌐 | [Web Research](skills/web-research.md) | Turn open questions into traceable, cross-checked evidence |
| 𝕏 | [X Research](skills/x-research.md) | Research X accounts, people, posts, and recent activity |
| 🛠️ | [Skill Builder](skills/skill-builder.md) | Turn repeated work into reusable, testable Skills |

→ [Full Skill Index](skills.md)

## How to Use the Library

The repository has two layers: **Core Skills** provide reusable methods; **Skill Cases** package those methods into complete, executable examples.

**Choose a Skill → open its Skill file → follow its Workflow → use templates/examples → run Evaluation → adapt and reuse.**

Every Skill should expose the same practical contract:

| Skill | Purpose | Workflow | Evaluation |
|---|---|---|---|
| Prompt Compression | Preserve intent while removing redundancy | Extract goal → constraints → redundancy → merge → validate | Intent / constraints / relationships / clarity / reduction |
| Prompt Optimization | Improve execution without changing intent | Intent → constraints → ambiguity → restructure → validate | Fidelity / coverage / ambiguity / robustness |
| Prompt Reverse Engineering | Convert strong prompts into reusable structures | Observe → variables → structure → template → test | Transferability / control / clarity |
| Video Prompt Compression | Shorten video prompts without losing motion semantics | Parse → semantic units → classify → merge → validate | Semantics / temporal coherence / action continuity |
| Video Prompt Optimization | Make video actions and camera instructions executable | Intent → subject → action → time → camera → constraints | Action / timing / camera / consistency |
| Web Research | Produce traceable answers from open questions | Scope → search → filter → cross-check → synthesize → cite | Relevance / source quality / freshness / citation |
| X Research | Verify and analyze X activity with explicit criteria | Discover → verify → inspect → filter → compare | Identity / recency / evidence / consistency |
| Skill Builder | Turn repeated work into maintainable Skills | Trigger → boundaries → workflow → contract → tests → iterate | Consistency / transferability / inspectability |

For a complete applied workflow, go to [cases/](cases/). For creating a new Skill, start with [Skill Builder](skills/skill-builder.md) and [templates/skill-template.md](templates/skill-template.md).

## Disclaimer

This repository is for learning, experimentation, and reusable AI workflow practice. Examples and third-party references remain subject to their original sources, licenses, and platform rules. Verify applicable rights before commercial use.

## Star History

[![Star History](https://api.star-history.com/svg?repos=0xf4vul/Skills4QiquLab&type=Date)](https://star-history.com/#0xf4vul/Skills4QiquLab&Date)

## License

[MIT License](LICENSE)
