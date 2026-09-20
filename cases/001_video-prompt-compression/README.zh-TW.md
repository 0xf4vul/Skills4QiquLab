<div align="center">

<img src="assets/svg/case-logo.svg" alt="001 — Video Prompt Compression" width="620">

# 001 — Video Prompt Compression

</div>

> Case ID: 001_video-prompt-compression

> 🌐 **其他語言：** 🇬🇧 [English](README.md) &nbsp;|&nbsp; 🇨🇳 [简体中文](README.zh-CN.md)

將影片提示詞壓縮為更短、更高密度的表達，同時保護動作鏈、時間關係、鏡頭邏輯與主體連續性。

## Case 結構

~~~text
001_video-prompt-compression/
├── README.md / README.zh-CN.md / README.zh-TW.md — Case 說明
├── SKILL.md — 核心方法
├── templates/ — 可複用提示詞範本
├── examples/ — 範例與失敗案例
├── evaluation/ — 評測與反向展開檢查
└── assets/svg/case-logo.svg — Case Logo
~~~

## 使用

直接閱讀 SKILL.md；需要範本時進入 templates/；需要測試時進入 examples/ 與 evaluation/。

## 核心邊界

不要將連續動作簡單折疊成一個結果動詞。壓縮的是表達方式，而不是影片需要表達的動作語義。