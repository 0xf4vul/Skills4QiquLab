# Source-to-KOL Research

## Mission

把用户提供的名单、网页、文章、社交媒体内容、视频/播客、PDF、截图、文件或一条链接转化为可信、可复核、可排序的 KOL / 专业信息源清单。

核心链路：

**任意输入源 → 提取人物/账号 → 去重与实体解析 → 候选账号 → 身份证据 → 账号状态 → 30D 活跃度 → 内容主题 → 信息源价值**

本 Skill 的对象是信息源账号的可验证性与可用性，不是对人物本人进行能力、地位或价值判断。

## Use when

- 从文章、Podcast、活动页、会议页、新闻、报告、PDF、视频描述中提取人物
- 从一条社交平台内容中发现潜在 KOL
- 从用户粘贴的文本、截图、文件或链接中提取人物、作者、被提及者、嘉宾、专家
- 确认某个账号是否属于指定人物
- 按近 30 天发帖量整理账号活跃度
- 区分高频发布与高信息密度
- 建立长期可维护的信息源名单

## Input model

本 Skill 不绑定任何单一网站。输入可以是 URL、社交内容、视频/音频、代码/技术内容、文档、图片或用户直接输入。

## Discovery modes

### Mode A — Person list

**人物名单 → 候选账号 → 身份核验 → 30D → 内容信号 → 信息源筛选**

### Mode B — Source-to-KOL

**内容源 → 提取人物 → 判断角色 → 去重 → 身份核验 → 账号核验 → 30D → 内容信号 → 信息源筛选**

人物提取至少区分：author / guest / mention / quote / reply / collaborator / speaker / contributor。

不要把所有出现的人自动视为 KOL。

### Mode C — Account list

**账号列表 → 账号归属 → 人物身份 → 30D → 内容信号 → 信息源筛选**

## KOL qualification

“KOL”在本 Skill 中不是粉丝数阈值，而是可作为某一主题长期信息源的人或账号。

不要仅凭粉丝数、点赞数或搜索排名把一个人判定为 KOL。

## Identity rules

### Source priority

**用户指定原始内容 / 官方页面 > 个人官网 > 公司/机构官网 > 目标平台本人主页 > 官方 LinkedIn/GitHub > 可信媒体 > 第三方聚合站**

用户提供的原始内容是发现来源；身份是否成立仍需独立证据。

### Candidate matching

至少执行多路径搜索：姓名 + 平台、姓名 + 公司、姓名 + 职位、姓名 + 项目 / 个人网站、site:目标平台 + 姓名、候选账号 + 公司 / 个人官网。

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

30D 统计必须经过“时间线完整性闸门”。身份确认不等于时间线可审计。

### Timeline status

- **TIMELINE_ACQUIRED**：目标平台在整个窗口内的逐条时间线已取得并可复核。
- **TIMELINE_PARTIAL**：只能取得窗口中的部分内容，不能推出完整总量。
- **TIMELINE_NOT_ACQUIRED**：无法取得可审计的目标时间线。
- **30D_VERIFIED**：已取得完整时间线，并完成 Posts / Original / Repost / Quote / Reply 分类与复核。

只有 **30D_VERIFIED** 才允许填写精确的 posts_30d 等完整统计值。

如果平台无法可靠读取完整时间线，写 **Unverified**，不得用搜索结果数量、粉丝变化或第三方摘要推算。

## Content signal

对最近 30 天可验证内容进行主题标注：

**AI / Software Engineering / Startup / VC / Cybersecurity / Crypto-Web3 / Product / Design-UX / Technology / Business / Education / Personal / Other**

样本不完整时明确标记 **partial**，不要把观察样本当成完整时间线。

## Information-source assessment

只评价账号作为信息源的表现：更新是否持续、原创内容是否充足、主题是否相关、是否具有稳定的信息增量、是否值得作为长期信息源。

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
| platform | 目标平台 |
| handle | 平台账号 |
| account_url | 账号 URL |
| status | 身份核验状态 |
| evidence | 身份证据 |
| checked_at | 核验日期 |
| posts_30d | 近30天总发帖 |
| original_30d | 近30天原创 |
| activity | 活跃度 |
| topics | 主要主题 |
| signal | 信息源判断 |
| notes | 异常或限制 |

## Workflow

**任意来源 → 提取人物/账号 → 角色识别 → 实体解析 → 候选账号 → 身份核验 → 账号状态 → 完整时间线 → 30D统计 → 内容分类 → 信息源筛选 → 审计**

### Timeline completeness gate

先取得目标平台完整时间线 → 判断 Timeline status → 逐条记录直接帖子 URL / post ID、发布时间、类型与主题 → 完成完整性检查 → 仅在 30D_VERIFIED 时汇总精确总量。

**关键顺序：时间线取得 → 完整性确认 → 单条证据 → 分类 → 汇总。**

不能用搜索结果数量、第三方摘要、粉丝变化、博客发布日期或其他平台内容替代目标平台帖子证据。

## Output contract

默认输出四张表：

### 1. Discovery & identity

| # | Person | Discovery source | Role | Platform | Account | Status | Evidence |
|---:|---|---|---|---|---|---|---|

### 2. 30D activity

| # | Person | Platform | Account | Posts | Original | Repost | Activity |
|---:|---|---|---|---:|---:|---:|---:|

### 3. Content signal

| Person | Platform | AI % | Tech % | Original % | Main topics | Sample |
|---|---|---:|---:|---:|---|---|

### 4. Final shortlist

| Person | Platform | Account | 30D Posts | Signal | Level | Reason |
|---|---|---|---:|---|---|---|

最终 shortlist 只允许 **CONFIRMED / PROBABLE** 账号进入；如果用户要求严格名单，则默认只允许 CONFIRMED。

## Failure modes

- Same-name collision
- Role mismatch
- Source-to-person leakage
- Platform lock-in
- Historical-account bias
- Frequency illusion
- Search-count inference
- Partial-timeline bias
- Identity leakage
- Person-ranking drift
- Source contamination

## Hard rules

**1. 先确定“来源中的角色”，再确定“是不是这个人”。**

**2. 先验证身份，再统计活动。**

**3. 不绑定任何单一平台；输入平台只是发现入口，不是 Skill 边界。**

**4. 未确认账号不得进入正式推荐名单。**

**5. 无法完整统计时使用 Unverified，不估算。**

**6. 30D Posts 与信息源价值必须分栏。**

**7. 排序对象是信息源，不是人物本人。**

**8. 用户给出的固定名单与后续发现名单必须分开；除非用户要求合并，不得擅自扩名单。**

**9. 30D 证据必须能回溯到目标平台的直接帖子 URL / post ID；无法回溯的内容不能进入可审计帖子样本。**

**10. 其他平台内容可以作为身份或内容发现证据，但不得转换成目标平台的 30D 帖子记录。**

**11. CONFIRMED 只表示身份成立；30D_VERIFIED 才表示活动统计成立。两者不得混用。**

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

## 30D Activity Audit Dataset

Case 002 includes a real evaluation dataset at `evaluation/30d-activity-audit.md`. It distinguishes identity verification, timeline acquisition, per-post evidence, and complete 30-day aggregation.

A complete 30D number may only be written when the entire target window is auditable. Partial timeline snapshots must use **Unverified** for totals and **Partial** for topic ratios.