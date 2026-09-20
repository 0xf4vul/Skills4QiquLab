# Reverse-Expansion Evaluation

反向展开是本 Case 的核心评测：不要只问“压短了多少”，而要问“压缩后的 Prompt 能否重新展开出原始语义”。

## Procedure

**Compressed Prompt → Recover semantic commitments → Compare with Original**

逐项标记：

- **Preserved**：明确保留
- **Weakened**：仍存在，但精度下降
- **Lost**：无法可靠恢复
- **Invented**：压缩后出现原文没有的新语义

## Pass condition

核心的主体、动作、时间关系、因果关系和镜头逻辑不得出现 **Lost**；出现 **Invented** 时必须修订。
