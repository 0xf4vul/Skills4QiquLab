# Changelog — 006 imagegen-textless-composite

## 1.1.0 (2026-09-22)
- 初版入库 Skills4QiquLab，作为 Case 006。
- 方法：图像模型只出**无字底图**，全部中文与数字由 Pillow 精确叠加。
- 脚本：`render_card.py`（声明式卡片渲染器，含字号自适应 / minimax 均衡折行 / 自动纵向流动）、`find_font.py`（跨平台中文字体探测 + 私有区对照识别豆腐块）、`strip_watermark.py`（去水印 crop/patch 双模式）、`selftest.py`（14 项断言）。
- 固定 14 项回归断言：字体探测、找到的字体确实含汉字、豆腐块识别器不误判纯拉丁字体（5 个真实拉丁字体反例）、端到端渲染、输出尺寸、极端长文案不崩、长文案未溢出右边界、去水印两模式、尺寸变化正确、半透明图层 alpha 回归（防「RGB 上 alpha 被静默丢弃」再次发生）。
- 三条排版护栏与三个必踩坑（RGB 半透明失效 / 双色渐变当压暗条刷白 / 底图主体与标题区打架）随 SKILL.md 一并入库。
