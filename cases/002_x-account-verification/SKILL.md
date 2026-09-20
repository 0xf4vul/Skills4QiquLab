# X Account Verification & Activity Research

## Mission

把一个人物名单转化为可信、可复核、可排序的 X 信息源清单。

核心链路：

**人物 → 候选账号 → 身份证据 → 账号状态 → 30D 活跃度 → 内容主题 → 信息源价值**

本 Skill 的对象是 **X 账号作为信息源的可用性**，不是对人物本人进行评价。

## Use when

- 从文章、Podcast、活动或会议页面筛选嘉宾的 X 账号
- 需要确认某个 X handle 是否属于指定人物
- 需要按近 30 天发帖量整理账号活跃度
- 需要区分高频发帖与高信息密度
- 需要建立长期可维护的 X 信息源名单

## Do not use when

- 只需要搜索一个明确已知的 X handle
- 没有可靠的人物身份信息
- 无法访问足够的账号或身份资料，却要求给出精确的 30D 数字
- 目标是评价、排名人物本人，而不是筛选信息源

## Identity rules

### Source priority

**官方活动/文章 > 个人官网 > 公司官网 > X 主页 > 官方 LinkedIn/GitHub > 可信媒体 > 第三方聚合站**

用户指定的文章是主名单来源。其他来源只能用于交叉验证，不得未经说明擅自新增人物。

### Candidate matching

对每个人至少执行多路径搜索：

1. 姓名 + X / Twitter
2. 姓名 + 公司
3. 姓名 + 职位
4. 姓名 + 项目/个人网站
5. site:x.com + 姓名

常见姓名必须加入公司、城市或职位等消歧条件。

### Verification status

- **CONFIRMED**：有官方直接链接，或至少两项强身份证据一致。
- **PROBABLE**：多项身份信息高度一致，但缺少直接官方链接。
- **UNVERIFIED**：存在候选账号，但无法可靠证明归属。
- **NOT_FOUND**：没有找到可靠候选账号。
- **WRONG_PERSON**：找到同名账号，但证据显示属于其他人。

禁止为了填满表格而强行选择候选账号。

## Activity window

以执行日为基准，统计：

**执行日 − 30 天 ≤ 发布时间 ≤ 执行日**

记录：

- posts_30d：原创帖 + 转发 + Quote + Reply
- original_30d
- repost_30d
- quote_30d
- reply_30d

如果平台无法可靠读取完整时间线，写 **Unverified**，不得用搜索结果数量推算。

## Activity bands

| 近 30 天总发帖 | 活跃度 |
|---:|---|
| ≥100 | 极高 |
| 50–99 | 高 |
| 20–49 | 中高 |
| 5–19 | 中 |
| 1–4 | 低 |
| 0 | 不活跃 |

活跃度只描述发布行为，不代表内容质量。

## Content signal

对最近 30 天可验证内容进行主题标注：

**AI / Software Engineering / Startup / VC / Cybersecurity / Crypto-Web3 / Product / Design-UX / Technology / Business / Education / Personal / Other**

计算：

- original_ratio = original_30d / posts_30d
- ai_ratio = AI posts / observed posts
- tech_ratio = Tech posts / observed posts

当样本不完整时明确标记 partial。

## Information-source assessment

推荐只评价账号：

- 更新是否持续
- 原创内容是否充足
- AI/Tech 内容是否相关
- 是否具有稳定的信息增量
- 是否值得作为长期信息源

不要输出“最佳嘉宾”“最强专家”等人物评价。

建议等级：

**A — 建议关注 / B — 可以关注 / C — 观察 / D — 不作为主要信息源**

等级针对账号的信息源价值，不针对人物本人。

## Evidence model

每个账号必须保存：

| 字段 | 内容 |
|---|---|
| person | 嘉宾姓名 |
| organization | 公司/机构 |
| role | 职位 |
| x_handle | X handle |
| x_url | X URL |
| status | 身份核验状态 |
| evidence | 身份证据 |
| evidence_level | ★–★★★★★ |
| checked_at | 核验日期 |
| posts_30d | 近30天总发帖 |
| original_30d | 近30天原创 |
| activity | 活跃度 |
| topics | 主要主题 |
| signal | 信息源判断 |
| notes | 异常或限制 |

## Workflow

### Phase 1 — Build the source list

从用户指定的官方页面提取人物名单 → 去重 → 固定人数 → 保留原始来源。

### Phase 2 — Discover candidates

姓名搜索 → 公司/职位消歧 → site:x.com 搜索 → 收集候选 handle。

### Phase 3 — Verify identity

官网/X/公司/LinkedIn/GitHub 交叉验证 → 判断是否本人 → 排除同名账号。

### Phase 4 — Verify account state

确认账号可访问、是否明显停用、是否长期无更新。

### Phase 5 — Count 30D activity

按时间窗口逐条检查可见帖子 → 记录总量与内容类型 → 不完整则标记。

### Phase 6 — Analyze signal

计算原创率 → 标注 AI/Tech 主题 → 识别高频低信号账号。

### Phase 7 — Rank information sources

先按身份可信度过滤 → 再按 30D 活跃度 → 再结合原创率和主题相关性 → 输出信息源等级。

### Phase 8 — Audit

随机复查高排名账号、低置信度账号和同名高风险账号，确保排序没有建立在错误身份上。

## Output contract

默认输出四张表：

### 1. Identity verification

| # | Person | Organization | X | Status | Evidence |
|---:|---|---|---|---|---|

### 2. 30D activity

| # | Person | X | Posts | Original | Repost | Activity |
|---:|---|---|---:|---:|---:|---|

按 Posts ↓ 排序。

### 3. Content signal

| Person | AI % | Tech % | Original % | Main topics |
|---|---:|---:|---:|---|

### 4. Final shortlist

| Person | X | 30D Posts | Signal | Level | Recommendation reason |
|---|---|---:|---|---|---|

## Failure modes

- **Same-name collision**：同名账号误认为本人。
- **Role mismatch**：公司或职位不一致。
- **Historical-account bias**：历史发帖很多，但近期不活跃。
- **Frequency illusion**：发帖很多，但主要是低信息量转发。
- **Search-count inference**：用搜索结果数量推算 30D 发帖。
- **Partial-timeline bias**：时间线不完整却给出精确数字。
- **Identity leakage**：把候选账号直接写进正式推荐名单。
- **Person-ranking drift**：把信息源排序变成人物能力评价。

## Hard rules

**1. 身份证据优先于活跃度。**

**2. 未确认账号不得进入正式推荐名单。**

**3. 无法完整统计时使用 Unverified，不估算。**

**4. 30D Posts 与信息源价值必须分栏。**

**5. 排序对象是 X 信息源，不是人物本人。**

## Evaluation

- 身份匹配准确率
- 同名误匹配率
- 证据完整性
- 30D 统计可复核性
- 原创率计算准确性
- AI/Tech 分类一致性
- 排序可解释性
- 对不确定性的诚实标记

## One-line workflow

**官方名单 → 候选 X → 身份核验 → 排除同名 → 30D 统计 → 内容分类 → 活跃度排序 → 信息源筛选**
