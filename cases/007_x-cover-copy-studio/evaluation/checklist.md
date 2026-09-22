# Evaluation Checklist — 007 X Cover & Copy Studio

score: weight-sum ≥ 80 / mode: heuristic-local

- [ ] (13) 列表/卡片行数完整，无静默裁切（对照 payload 条目数）
- [ ] (13) footer 区（胶囊标签 + 红色收藏横幅）完整，下缘有留白
- [ ] (12) 无互相遮挡：横幅盖列表行、水印残留 = 直接 FAIL
- [ ] (12) 无乱码方框；🍟👇🧷 等 emoji 彩色渲染
- [ ] (12) 标题为超粗黑体（webfont 竞态检查）
- [ ] (12) 无 `{ { TOKEN } }` 字面残留
- [ ] (13) 海报文案与原推事实一一对应（域名/数量）
- [ ] (13) 变体文案无广告法绝对化用语；未新增未经证实宣称
- [ ] (bonus) 同一 payload 连渲两次 MAD < 0.5

FAIL 处理顺序: 行高预算 → 裁片复跑 `qa_render.py` → 模板回退 → 重渲。
