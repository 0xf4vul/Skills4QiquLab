<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> Read this in other languages: [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

Compress video prompts without removing the action, timing, camera, or continuity information that the generation result depends on.

## Highlights

- **Semantic-preserving compression** — reduces redundancy without collapsing meaningful actions.
- **Temporal-aware** — preserves order, duration, pauses, transitions, and causal relationships.
- **Camera-aware** — treats camera movement and shot continuity as first-class constraints.
- **Reverse-expansion evaluation** — expands the compressed prompt to test whether critical source semantics remain recoverable.
- **Failure-case driven** — includes explicit failure patterns such as verb collapse, time deletion, and false continuity.

## Project Structure

| Path | Description |
|---|---|
| `SKILL.md` | Core compression method, boundaries, workflow, output contract, and failure modes |
| `templates/` | Reusable Skill and video-prompt templates |
| `examples/` | Basic cases, continuous-action cases, and failure cases |
| `evaluation/` | Evaluation rubric and reverse-expansion checks |
| `assets/svg/` | Case logo and reusable SVG assets |

## Usage

**Read SKILL.md → choose a template → reference an example → compress → run evaluation → reuse**

For the complete method, see [SKILL.md](SKILL.md). For evaluation, see [evaluation/](evaluation/). For reusable starting points, see [templates/](templates/).

## Boundary

Do not remove action semantics, temporal relationships, camera behavior, causal dependencies, or continuity constraints merely to make a prompt shorter.