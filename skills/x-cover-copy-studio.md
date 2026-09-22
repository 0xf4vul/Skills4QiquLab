# X Cover & Copy Studio

> Skill Entry · 完整版（模板/脚本/例图/测试）见 [Case 007](../cases/007_x-cover-copy-studio/)

## 触发
给一条**清单体推文**（编号列表/工具合集），要「X 封面 / 推广海报 / 配图 / 推文变体」。
数不出 "1. 2. 3..." 的叙事推文不走本 Skill（见 fit-guide 门禁）。

## 核心流程
0. 门禁: ≤7 行→paper；7+1→dark；8–14 拆分或换 dark；≥15 拒绝模具
1. 参考图解构（如有）: vision 模型按 字段 schema 输出 → 提炼共同设计语言
2. 写变体: 骨架保留（emoji 钩子→数字承诺→编号列表→收藏 CTA），血肉全换（隐喻/句式/损失厌恶）
3. payload.json → `render.py`（HTML token 填充 → body zoom:2 → Playwright 2x）
4. 质检回路（强制）: 行完整性 / footer / 遮挡 / tofu / 字体权重 → FAIL 回布局预算

## 契约与红线
- paper ≤7 行、dark ≤7+1 卡，超限硬 FAIL 绝不静默裁切
- 域名、数量、功能事实不改写；禁广告法绝对化词（最/第一/唯一）
- webfont 等待 ≥7s；Linux 必须显式 Noto Color Emoji
- 比例: 2.41:1（4000×1660，贴参考风格）/ 16:9（3200×1800，时间流安全线）

## 质量杠杆
条目 8–14 字 · 域名 ≤20 字符（自动换行上限 45+ 仍安全）· emoji ≤3 ·
双色纪律（墨 + 红 + 琥珀）· 行数 5–7 最饱满
