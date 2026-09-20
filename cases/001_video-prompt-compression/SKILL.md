# Video Prompt Compression

## Mission

压缩视频生成 Prompt，同时保留生成结果真正依赖的视觉与时间语义。

## Use when

- Prompt 存在重复、冗余或低信息密度表达
- 需要缩短 Prompt 以便维护、迁移或复用

## Do not use when

- 所谓冗余实际上描述了独立动作
- 文本包含关键时间关系、转场、镜头运动或因果依赖
- 进一步压缩会破坏动作连续性或表达意图

## Semantic priority

**时间关系 > 动作因果 > 主体身份 > 镜头逻辑 > 空间构图 > 外观细节 > 装饰性形容词**

## Procedure

1. 解析主体、初始状态、动作链、时间、镜头、环境、风格、音频与限制条件。
2. 区分硬约束与装饰性语言。
3. 只合并语义等价、不会改变动作链的表达。
4. 保留必要的时间标记、因果关系和镜头连续性。
5. 对压缩结果进行反向展开，检查原始语义是否仍可恢复。

## Compression levels

- **L0**：仅清理明显重复。
- **L1**：合并同义与装饰性表达；默认等级。
- **L2**：重写为高密度表达，但保留完整动作链。
- **L3**：极限压缩；仅在明确允许损失次要细节时使用。

## Critical boundary

例如：

reaches → grips → lifts → pauses → brings to lips

不能在没有授权的情况下直接压成：

drinks

因为动作过程、因果关系和时间结构已经丢失。

## Output contract

输出：

1. 压缩后的 Prompt
2. 保留的关键语义
3. 被合并或删除的冗余
4. 如存在风险，指出压缩边界

## Failure modes

- Verb collapse：多个动作被压成一个结果动词
- Time deletion：时间顺序消失
- Camera ambiguity：镜头行为被省略
- Cause deletion：动作因果关系消失
- False continuity：原本不连续的动作被强行连接
- Decorative over-preservation：装饰词保留过多，真正语义反而被挤压

## Evaluation

**语义保真 / 动作连续性 / 时间一致性 / 镜头连续性 / 因果关系 / 可执行性 / 压缩收益**

## Model adaptation

模型差异只进入适配层；不得为了模型习惯改变核心语义。适配时可调整时间表达、镜头术语、密度与约束写法。
