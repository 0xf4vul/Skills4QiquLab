# 示例 4 · 成套金句卡配图（8 张一次跑完）

**任务**：给 8 张金句卡的中间留白各配一张无字素描底图，文字走排版叠加。

## 一、先给每张定意象，不要边想边跑

把每句金句拆成「一句话能画出来的东西」，抽象概念必须落到**具象物件 + 一个动作**：

| 金句 | 意象 | 落点 |
|------|------|------|
| 便宜到你不再算它的价钱 | 掌心一枚硬币 + **倒扣的算盘**（珠子滑出） | 扣下算盘 = 不再计算 |
| 自来水…不会想这一捧水多少钱 | 手在老水龙头下接水，**没有水表** | 缺一件东西，也是画面 |
| 你看到的是它在干活，后台是 Token 流动 | 伏案**背影** + 身后管道里流动的颗粒 | 前景静 / 背景动，一句话的两个半句各占一层 |
| Bug 修好了才让人早下班 | 关掉的台灯 + 指向六点的挂钟 + 空杯 | 「早下班」翻译成三件静物 |
| 每一步都不难，凑在一起就是一个下午 | 一级级小台阶通向窗口夕阳 + 长斜影 | 影子 = 时间流逝 |
| 只三件事：做完 / 花钱 / 自己修 | 桌上**三样东西**：锤子、硬币、针线卷 | 数字 → 物件个数 |
| 花同样的钱买到更聪明的智能 | 老天平：一端一枚硬币，另一端一只大灯泡 | 天平天生就是「性价比」 |
| 端起一碗热气腾腾的未来 | 双手捧碗 + 细排线画热气 | 直取原句意象即可 |

口诀：**算盘要扣下、水表要缺席、灯要关掉**——画面里的「减法」往往比「加法」更贴合金句。

## 二、批量构造 prompt

```python
import subprocess, sys, os
PY = sys.executable
jobs = [('01', '<英文主体>', 'conceptual'), ('06', '<英文主体>', 'hatched-tonal')]
for key, subject, preset in jobs:
    r = subprocess.run([PY, 'build_prompt.py', '-s', subject, '-p', preset, '-a', 'square'],
                       capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print('FAIL', key, r.stderr); continue   # 必看 stderr，否则静默拿到空串
    body = r.stdout.split('=== PROMPT ===')[1].strip()
    open(f'prompts/{key}.txt', 'w', encoding='utf-8').write(body)
```

坑：`-p hatched` 是错的，key 是 `hatched-tonal`。写错时 stdout 为空、只有 stderr 有提示，批量脚本里不打印 stderr 就会得到 8 个空文件。**必查 `returncode`**。

## 三、生图

统一 `square` 1024²（卡片内插画区用 1:1 最好排），`quality=high`、`style=natural`。可并行发多个 ImageGen 调用，4 张一批。

已有合适的旧图就复用（本项目 02 直接复用了上一轮的水龙头图），能省一次生图。

## 四、嵌进卡片的 CSS 要点

```css
.card{ aspect-ratio:2/3; display:flex; flex-direction:column }  /* 3/4 太矮，插画会被压成条 */
.art { flex:1 1 auto; min-height:130px; margin:16px 0 10px; overflow:hidden }
.art img{
  width:100%; height:100%; object-fit:cover;
  mask-image:radial-gradient(ellipse at center,#000 76%,rgba(0,0,0,0) 100%);
}
```

- 用 `flex:1` 吃掉中间剩余空间，别给固定高度——卡片宽度会随栅格变。
- `object-fit:cover` 正好裁掉概念隐喻预设「上三分之一留白」里用不上的部分；反过来如果构图主体贴边，就换 `contain`。
- **radial mask 是关键**：图的纸色和卡片的纸色不可能完全同值，硬边会露出一圈方框。让边缘渐隐到透明，图片就「长」在纸上了。

## 五、纪律

- 图内**零文字**，金句一律走 HTML/CSS 排版叠加，不塞进 prompt 赌模型。
- 成套出图时保持预设一致（本例概念隐喻 ×6 + 排线明暗 ×2），混太多笔触会像拼贴。
- 看不到的图不替它写自检报告——要么切多模态看，要么请用户看一眼再说。
