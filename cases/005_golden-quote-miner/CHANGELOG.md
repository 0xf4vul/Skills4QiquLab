# Changelog · golden-quote-miner

## 1.1.0 — 2026-09-22

### 新增
- 新增 `scripts/selftest.py`（示例长文跑通 / JSON 合法 / 边界输入不崩 / stdin 管道，共 11 项断言）与 `requirements.txt`（零第三方依赖，纯标准库）
- 与 skills-export 商业化打包对齐版本号（功能脚本 `scan.py` 无改动）

## 1.0.0 — 2026-09-22

### 新增
- 从 `infographic-maker` 的观点蒸馏层提纯为独立技能，剥离写作/排版/配图约束
- SKILL.md：金句四维度定义 + 四层筛选漏斗 + 八型句式骨架 + 固定输出表格 + 原创模式 + 6 条质量红线 + 自检清单
- `references/quote-patterns.md`：八型公式与正反例、失效原因、打磨五步（砍/换/短/收/读）
- `references/scoring-rubric.md`：四层漏斗逐层打分细则（含传播力排序权重公式）
- `references/ai-flavor-blacklist.md`：AI 味 / 鸡汤黑名单，含脚本抓不到的 5 类结构模式
- `scripts/scan.py` + `scripts/lexicon.json`：候选扫描器 CLI，支持文件/stdin、Markdown 与 JSON 双输出、`--explain` 打印规则
- `examples/`：样稿 + 提炼模式案例 + 原创模式案例
- README / CHANGELOG / LICENSE(MIT) / _meta.json 工程元信息齐备

### 验证
- 样稿 19 句扫描：正确把「在这个充满不确定性的时代…」判为 AI 腔（−4.0）、「时间会给你答案…」判为陈词（−3.0）
