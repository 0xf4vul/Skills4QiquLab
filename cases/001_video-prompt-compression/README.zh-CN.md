<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> Case ID: 001_video-prompt-compression

> 🌐 **其他语言：** 🇬🇧 [English](README.md) &nbsp;|&nbsp; 🇹🇼 [繁體中文](README.zh-TW.md)

将视频提示词压缩为更短、更高密度的表达，同时保护动作链、时间关系、镜头逻辑与主体连续性。

## Case 结构

~~~text
001_video-prompt-compression/
├── README.md / README.zh-CN.md / README.zh-TW.md — Case 说明
├── SKILL.md — 核心方法
├── templates/ — 可复用提示词模板
├── examples/ — 示例与失败案例
├── evaluation/ — 评测与反向展开检查
└── assets/svg/case-logo.svg — Case Logo
~~~

## 使用

直接阅读 SKILL.md；需要模板时进入 templates/；需要测试时进入 examples/ 与 evaluation/。

## 核心边界

不要把连续动作简单折叠成一个结果动词。压缩的是表达方式，而不是视频需要表达的动作语义。