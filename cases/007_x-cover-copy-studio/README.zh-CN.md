<div align="center">

<img src="assets/svg/case-logo.svg" alt="007 — X Cover & Copy Studio" width="620">

</div>

> 其他语言: [English](README.md)

# 007 — X 推文封面海报 + 文案变体工坊

> 本目录是 Case 内嵌副本，与独立仓库 [0xf4vul/x-cover-copy-studio](https://github.com/0xf4vul/x-cover-copy-studio) 同步（源: 2026-09-22 会话实战提炼，v1.1.0）。适用边界与质量杠杆见 `references/fit-guide.md`。

# x-cover-copy-studio

X.com(Twitter) 推文封面海报 + 文案变体的一站式商用 Skill 工程。

## 目录

```
x-cover-copy-studio/
├── SKILL.md                      # Agent 工作流(安装后即插即用)
├── README.md / LICENSE.md
├── templates/                    # 双主题 token 模板(可直接改 CSS)
│   ├── poster-paper.html        # 2.41:1 复古纸感横幅
│   └── poster-dark.html         # 16:9 深色图鉴卡片
├── scripts/
│   ├── render.py                # payload.json → 2x PNG(Playwright)
│   └── qa_render.py             # 强制质检裁片 + 踩坑清单
├── references/
│   ├── design-language.md       # 配色/字体/纹理/布局预算配方
│   ├── copy-formulas.md         # 钩子库/改写句式/红线
│   └── fit-guide.md             # 适用情况/使用边界/质量杠杆/调用门禁
└── examples/case-pinterest-tools/
    ├── refs/*.jpg               # 7 张风格参考图(输入侧引用示例)
    ├── out/*.png                # 2 张成图(输出侧引用示例)
    ├── tweet-original.md        # 原推文
    ├── tweet-variant.md         # 变体推文
    └── payload.{paper,dark}.json# 可直接重放的渲染参数
```

## 快速开始

```bash
cd examples/case-pinterest-tools
python3 ../../scripts/render.py payload.paper.json ./regen   # → poster-paper@2x.png
python3 ../../scripts/render.py payload.dark.json  ./regen   # → poster-dark@2x.png
python3 ../../scripts/qa_render.py regen/*.png               # 质检裁片
```

安装为 QwenWork Skill:
将整个目录放入 `.qwenwork/skills/x-cover-copy-studio/`(项目级)或
`~/.config/qwenwork/skills/x-cover-copy-studio/`(全局), 重启 QwenWork 生效。

## 环境要求

- `playwright` CLI + chromium(沙箱内版本目录错位时:
  `ln -s <已装版本目录> /opt/playwright-browsers/chromium_<缺失版本>`, 并以真实 chrome 路径补一个
  `chrome-headless-shell` 软链)
- 可访问 Google Fonts(Noto Sans SC 900 / IBM Plex Mono / Noto Color Emoji)
- 质检推荐搭配 media-read skill(`describe.py --high-res` 复核裁片)

## 已验证的坑(务必先读)

1. **列表溢出挤飞 footer** — `.main` 必须固定高度并列入布局预算(design-language.md §五)
2. **emoji tofu** — 显式引入 Noto Color Emoji
3. **webfont 未加载出细体** — 渲染前 wait 7s
4. **2x 高清** — `body{zoom:2}` + viewport 加倍, 不改图片本身尺寸语义

## 商用授权(简述)

产出物(海报/文案)可无限商用、投放、修改、转售交付; 源码工程本身**不可**原样转卖/开源分发。
全文见 LICENSE.md。


## 测试日志 v1.1.0 (2026-09-22)

| 层级 | 用例 | 结果 |
|---|---|---|
| L1 复原 | 双 payload 重放出图, 尺寸/比例校验 | PASS |
| L2 通用 | 全新主题(行前清单 5 条)零改码出图 | PASS |
| L3 故障注入 | paper 8 行 / dark 9 卡 / 缺字段 | 全部硬拦截 rc=1 |
| L4 唤起 | 新会话触发(需 QwenWork 重启 + 新聊天加载 skills) | 待用户验收 |
| L5 对抗 | 45 字符超长域名 + 加长描述 | PASS: 域名自动换行, 布局不塌 |
| 合规 | name=目录, 触发词覆盖中英, frontmatter 仅规范字段, 包内无绝对路径 | PASS |
| 幂等 | 连续两次渲染像素差 0.019/255(<0.05% 面积) | PASS(子像素噪声级) |
