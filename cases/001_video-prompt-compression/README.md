<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> Case ID: 001_video-prompt-compression

Compress video prompts into shorter, denser expressions while preserving action chains, temporal relationships, camera logic, and subject continuity.

## Case structure

**SKILL.md → templates → examples → evaluation → assets**

## Use

Read SKILL.md for the methodology; use templates/ for repeatable prompt structures; use examples/ for reference cases; use evaluation/ for testing and failure analysis.

## Naming & architecture

This Case lives at cases/001_video-prompt-compression/. All Cases use **three-digit sequential numbering + kebab-case names**, such as 001_video-prompt-compression, 002_xxx, and 003_xxx. The number indicates creation order and does not change the semantic name of the Skill.

## Core boundary

Do not collapse a continuous action sequence into a single result verb. The goal is to compress the expression, not to remove the action semantics the video needs to convey.
