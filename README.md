<div align="center">

<img src="assets/logo.svg" alt="Qiqu.Lab — 奇趣实验室" width="760">

<p>
<strong>A Creative AI Prompt Engineering Playground</strong><br>
<sub>A curated collection of practical AI Skills, Case Studies, templates, examples, and evaluation methods.</sub>
</p>

<p>
<a href="https://github.com/0xf4vul/Skills4QiquLab/stargazers"><img src="https://img.shields.io/github/stars/0xf4vul/Skills4QiquLab?style=flat-square&logo=github&label=stars" alt="GitHub stars"></a>
<a href="https://github.com/0xf4vul/Skills4QiquLab/commits/main"><img src="https://img.shields.io/github/last-commit/0xf4vul/Skills4QiquLab?style=flat-square&label=last%20commit" alt="Last commit"></a>
<a href="https://github.com/0xf4vul/Skills4QiquLab/issues"><img src="https://img.shields.io/github/issues/0xf4vul/Skills4QiquLab?style=flat-square&label=issues" alt="Issues"></a>
<a href="https://github.com/0xf4vul/Skills4QiquLab/blob/main/LICENSE"><img src="https://img.shields.io/github/license/0xf4vul/Skills4QiquLab?style=flat-square&label=license" alt="License"></a>
</p>

</div>

> 🌐 **Read this in other languages:** [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

# Qiqu.Lab — A Creative AI Prompt Engineering Playground

Qiqu.Lab is an open, practical laboratory for turning AI workflows into **reusable Skills, complete Cases, ready-to-use Templates, examples, and evaluation methods**.

The goal is simple: **capture what works → structure it → test it → iterate it → reuse it.**

<table>
<tr>
<td align="center" width="20%"><h2>⚡</h2><b>Core Skills</b><br><sub>Reusable methods</sub></td>
<td align="center" width="20%"><h2>▣</h2><b>Skill Cases</b><br><sub>Complete workflows</sub></td>
<td align="center" width="20%"><h2>▤</h2><b>Templates</b><br><sub>Ready to use</sub></td>
<td align="center" width="20%"><h2>💡</h2><b>Examples</b><br><sub>Practical patterns</sub></td>
<td align="center" width="20%"><h2>▥</h2><b>Evaluation</b><br><sub>Test & improve</sub></td>
</tr>
</table>

## 🚀 Quick Start

**1. Explore a methodology** → open [skills/](skills/) or [skills.md](skills.md)

**2. Use a complete Skill Case** → open [cases/](cases/) and choose the numbered Case

**3. Build your own** → start with [skills/skill-builder.md](skills/skill-builder.md) and [templates/skill-template.md](templates/skill-template.md)

### Featured Case

**001 · Video Prompt Compression**  
Compress video prompts while protecting **action chains, temporal relationships, camera logic, and subject continuity**.

→ [cases/001_video-prompt-compression/](cases/001_video-prompt-compression/)

## 🧩 Architecture

~~~text
Core Skill
   ↓
Skill Case
   ↓
Template → Example → Evaluation
   ↓
Iteration
~~~

- **Core Skills** — portable methodology
- **Skill Cases** — complete, self-contained implementations
- **Templates** — reusable structures
- **Examples** — practical and failure cases
- **Evaluation** — semantic fidelity, execution quality, and regression checks

## 📁 Repository Structure

~~~text
Skills4QiquLab/
├── README.md
├── README.zh-CN.md
├── README.zh-TW.md
├── skills.md
├── skills/
├── templates/
└── cases/
    └── 001_video-prompt-compression/
        ├── README.md
        ├── SKILL.md
        ├── templates/
        ├── examples/
        ├── evaluation/
        └── assets/
~~~

### Case Naming Convention

All Cases under cases/ use:

~~~text
NNN_skill-name/
~~~

**001_video-prompt-compression → 002_xxx → 003_xxx → …**

The three-digit prefix records creation order and is mandatory for every new Case.

## 🛠 Design Principles

**Methodology ↔ Implementation** — keep portable Skills separate from concrete Cases.  
**Meaning before compression** — never shorten a prompt by deleting essential semantic constraints.  
**Evaluation first** — examples and failure cases are part of the engineering loop.  
**Iterate continuously** — every Case should remain testable and improvable.

## 📚 Index

- [Skills Index](skills.md)
- [Core Skills](skills/)
- [Skill Cases](cases/)
- [Global Templates](templates/)
- [001 · Video Prompt Compression](cases/001_video-prompt-compression/)

## 📄 License

MIT License — see [LICENSE](LICENSE).

<div align="center">
<sub>Built as an experimental, practical AI Skill laboratory.</sub>
</div>