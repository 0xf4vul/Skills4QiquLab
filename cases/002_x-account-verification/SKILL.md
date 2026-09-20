# Source-to-KOL Discovery & Account Verification

## Mission

把用户提供的名单、网页、文章、社交媒体内容、视频/播客、PDF、截图、文件或一条链接转化为可信、可复核、可排序的 KOL / 专业信息源清单。

核心链路：

**任意输入源 → 提取人物/账号 → 去重与实体解析 → 候选账号 → 身份证据 → 账号状态 → 30D 活跃度 → 内容主题 → 信息源价值**

本 Skill 的对象是信息源账号的可验证性与可用性，不是对人物本人进行能力、地位或价值判断。

## Use when

- 从文章、Podcast、活动页、会议页、新闻、报告、PDF、视频描述中提取人物
- 从一条 X / LinkedIn / YouTube / Reddit / Instagram / Threads 等内容中发现潜在 KOL
- 从用户粘贴的文本、截图、文件或链接中提取人物、作者、被提及者、嘉宾、专家
- 确认某个账号是否属于指定人物
- 按近 30 天发帖量整理账号活跃度
- 区分高频发布与高信息密度
- 建立长期可维护的信息源名单

## Input model

本 Skill 不绑定任何单一网站。输入可以是：

| 输入类型 | 典型来源 | 可提取对象 |
|---|---|---|
| URL | 文章 / 活动页 / 公司页 / 新闻 / 博客 | 作者、嘉宾、专家、被引用者 |
| 社交内容 | X、LinkedIn、Reddit、Instagram、Threads 等 | 作者、提及者、回复者、引用者 |
| 视频/音频 | YouTube、播客页、节目简介 | 主播、嘉宾、专家、出镜者 |
| 代码/技术内容 | GitHub、GitLab、技术博客 | 作者、维护者、贡献者 |
| 文档 | PDF、Markdown、Word、网页文档 | 作者、演讲者、引用专家 |
| 图片 | 截图、海报、信息图 | 人名、账号、机构、来源 |
| 用户直接输入 | 粘贴文本、名单、账号、描述 | 按上下文解析实体 |

如果用户提供的是具体 URL，先读取用户提供的内容，再决定是否需要外部搜索补证据；不要因为输入是某个平台就把 Skill 限制在该平台。

## Discovery modes

### Mode A — Person list

**人物名单 → 候选账号 → 身份核验 → 30D → 内容信号 → 信息源筛选**

适用于文章、活动页、Podcast 嘉宾列表等。

### Mode B — Source-to-KOL

**内容源 → 提取人物 → 判断角色 → 去重 → 身份核验 → 账号核验 → 30D → 内容信号 → 信息源筛选**

适用于一条 X / LinkedIn / Reddit 内容、Thread、视频、文章、采访、播客、论坛讨论、报告等。

人物提取至少区分：

- author：内容作者
- guest：嘉宾
- mention：被提及者
- quote：被引用者
- reply：回复者
- collaborator：共同创作者
- speaker：演讲者
- contributor：贡献者

不要把所有出现的人自动视为 KOL。

### Mode C — Account list

**账号列表 → 账号归属 → 人物身份 → 30D → 内容信号 → 信息源筛选**

适用于用户直接给出一批账号。

## KOL qualification

“KOL”在本 Skill 中不是粉丝数阈值，而是可作为某一主题长期信息源的人或账号。

候选进入验证层前至少满足一种信号：

- 在输入内容中承担作者/嘉宾/专家/演讲者等明确角色
- 被多个可信来源明确识别为某领域专业人士
- 具有持续公开输出
- 用户明确指定其为目标人物/账号

不要仅凭粉丝数、点赞数或搜索排名把一个人判定为 KOL。

## Identity rules

### Source priority

**用户指定原始内容 / 官方页面 > 个人官网 > 公司/机构官网 > 目标平台本人主页 > 官方 LinkedIn/GitHub > 可信媒体 > 第三方聚合站**

用户提供的原始内容是发现来源；身份是否成立仍需独立证据。

### Candidate matching

至少执行多路径搜索：

1. 姓名 + 平台
2. 姓名 + 公司
3. 姓名 + 职位
4. 姓名 + 项目 / 个人网站
5. site:目标平台 + 姓名
6. 反向搜索：候选账号 + 公司 / 个人官网

常见姓名必须加入公司、城市、职位、项目等消歧条件。

### Verification status

- **CONFIRMED**：官方直接链接，或至少两项强身份信号一致。
- **PROBABLE**：多项身份信息高度一致，但缺少直接官方链接。
- **UNVERIFIED**：存在候选账号，但无法可靠证明归属。
- **NOT_FOUND**：当前检索范围没有找到可靠候选。
- **WRONG_PERSON**：候选账号存在，但证据显示属于其他人。

禁止为了填满表格而强行选择候选账号。

## Activity window

以执行日为基准：

**执行日 − 30 天 ≤ 发布时间 ≤ 执行日**

记录：

- posts_30d：原创 + 转发 + Quote + Reply
- original_30d
- repost_30d
- quote_30d
- reply_30d

如果平台无法可靠读取完整时间线，写 **Unverified**，不得用搜索结果数量、粉丝变化或第三方摘要推算。

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

样本不完整时明确标记 **partial**，不要把观察样本当成完整时间线。

## Information-source assessment

只评价账号作为信息源的表现：

- 更新是否持续
- 原创内容是否充足
- 主题是否与用户目标相关
- 是否具有稳定的信息增量
- 是否值得作为长期信息源

建议等级：

**A — 建议关注 / B — 可以关注 / C — 观察 / D — 不作为主要信息源**

等级针对信息源，不针对人物本人。

## Evidence model

每个实体至少保存：

| 字段 | 内容 |
|---|---|
| source_url | 发现该人物/账号的原始来源 |
| discovery_type | author / guest / mention / quote / reply / speaker / contributor |
| person | 人物姓名 |
| organization | 公司/机构 |
| role | 职位 |
| platform | X / LinkedIn / YouTube / GitHub / Reddit / etc. |
| handle | 平台账号 |
| account_url | 账号 URL |
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

### Phase 0 — Ingest

读取用户提供的 URL、文本、图片、文件或账号列表 → 判断输入类型 → 保存原始来源。

### Phase 1 — Extract

从内容中提取人物、账号、作者、嘉宾、专家、提及者等 → 标记 discovery_type → 去重。

### Phase 2 — Resolve entities

姓名标准化 → 机构/职位/城市补全 → 合并同一人物的不同写法 → 保留原始名称。

### Phase 3 — Discover candidates

多平台搜索 → 收集候选账号 → 不因单一同名结果直接确认。

### Phase 4 — Verify identity

官网 / 原始内容 / 公司 / 平台主页 / LinkedIn / GitHub 等交叉验证 → 排除同名账号。

### Phase 5 — Verify account state

确认账号可访问、身份信息一致、是否明显停用或长期无更新。

### Phase 6 — Count 30D activity

按平台可见时间线逐条检查 → 记录总量与内容类型 → 时间线不完整则 Unverified。

### Phase 7 — Analyze signal

计算原创率 → 标注 AI / Tech / 目标主题 → 识别高频低信号账号。

### Phase 8 — Rank information sources

先按身份可信度过滤 → 再按活动 → 再结合原创率、主题相关性和稳定信息增量 → 输出信息源等级。

### Phase 9 — Audit

重点复查：高排名账号、低置信度账号、常见姓名、跨平台同名账号、异常高活跃账号。

## Output contract

默认输出四张表：

### 1. Discovery & identity

| # | Person | Discovery source | Role | Platform | Account | Status | Evidence |
|---:|---|---|---|---|---|---|---|

### 2. 30D activity

| # | Person | Platform | Account | Posts | Original | Repost | Activity |
|---:|---|---|---|---:|---:|---:|---|

按 Posts ↓ 排序；无法完整统计时使用 Unverified。

### 3. Content signal

| Person | Platform | AI % | Tech % | Original % | Main topics | Sample |
|---|---|---:|---:|---:|---|---|

### 4. Final shortlist

| Person | Platform | Account | 30D Posts | Signal | Level | Reason |
|---|---|---|---:|---|---|---|

最终 shortlist 只允许 **CONFIRMED / PROBABLE** 账号进入；如果用户要求严格名单，则默认只允许 CONFIRMED。

## Failure modes

- **Same-name collision**：同名账号误认为本人。
- **Role mismatch**：公司或职位不一致。
- **Source-to-person leakage**：内容中出现的人被自动当成专家/KOL。
- **Platform lock-in**：输入是 X 就只搜索 X，忽略其他平台证据。
- **Historical-account bias**：历史发帖很多，但近期不活跃。
- **Frequency illusion**：发帖很多，但主要是低信息量转发。
- **Search-count inference**：用搜索结果数量推算 30D 发帖。
- **Partial-timeline bias**：时间线不完整却给出精确数字。
- **Identity leakage**：候选账号直接进入正式名单。
- **Person-ranking drift**：把信息源排序变成人物能力评价。
- **Source contamination**：后续搜索发现的人物未经用户授权被加入固定名单。

## Hard rules

**1. 先确定“来源中的角色”，再确定“是不是这个人”。**

**2. 先验证身份，再统计活动。**

**3. 不绑定 X；输入平台只是发现入口，不是 Skill 边界。**

**4. 未确认账号不得进入正式推荐名单。**

**5. 无法完整统计时使用 Unverified，不估算。**

**6. 30D Posts 与信息源价值必须分栏。**

**7. 排序对象是信息源，不是人物本人。**

**8. 用户给出的固定名单与后续发现名单必须分开；除非用户要求合并，不得擅自扩名单。**

## Evaluation

- 人物提取准确率
- discovery_type 准确率
- 身份匹配准确率
- 同名误匹配率
- 跨平台实体解析准确率
- 证据完整性
- 30D 统计可复核性
- 原创率计算准确性
- AI/Tech 分类一致性
- 排序可解释性
- 对不确定性的诚实标记
- 对输入来源的覆盖能力

## One-line workflow

**任意来源 → 提取人物/账号 → 角色识别 → 实体解析 → 候选账号 → 身份核验 → 30D统计 → 内容分类 → 信息源筛选 → 审计**


## 30D Activity Audit Dataset

Case 002 includes a real evaluation dataset at `evaluation/30d-activity-audit.md`. It distinguishes observed posts from complete 30-day totals and preserves identity evidence, source type, classification, and completeness.

A complete 30D number may only be written when the entire target window is auditable. Partial timeline snapshots must use **Unverified** for totals and **Partial** for topic ratios.
