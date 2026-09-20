<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> Case ID: 001_video-prompt-compression

> 🌐 **Read this in other languages:** 🇨🇳 [简体中文](README.zh-CN.md) &nbsp;|&nbsp; 🇹🇼 [繁體中文](README.zh-TW.md)

Compress video prompts into shorter, denser expressions while preserving action chains, temporal relationships, camera logic, and subject continuity.

## Case structure

~~~text
001_video-prompt-compression/
├── README.md / README.zh-CN.md / README.zh-TW.md — case overview
├── SKILL.md — core methodology
├── templates/ — reusable prompt templates
├── examples/ — examples and failure cases
├── evaluation/ — evaluation and reverse-expansion checks
└── assets/svg/case-logo.svg — case logo
~~~

## Use

Read SKILL.md for the methodology; use templates/ for repeatable prompt structures; use examples/ for reference cases; use evaluation/ for testing and failure analysis.

## Core boundary

Do not collapse a continuous action sequence into a single result verb. The goal is to compress the expression, not to remove the action semantics the video needs to convey.