<div align="center">

<img src="assets/svg/case-logo.svg" alt="005 — Golden Quote Miner" width="620">

# 005 — Golden Quote Miner

</div>

> Other languages: [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

Turn a long piece of content into 5-12 sentences that **survive on their own, separated from the source**. Plain text deliverable — no layout, no image pipeline.

## Highlights

- **Four-stage funnel.** Candidate scan → density filter → four-axis tension scoring → context-independence check. Each stage has an explicit rejection rule; nothing is picked by feel.
- **`scan.py` runs stage one.** Sentence splitting, judgment-word / AI-flavor / cliché tagging, position and length weighting, ranking. Markdown and JSON output, stdin supported.
- **Eight sentence skeletons.** Counter-intuitive reversal / essence exposed / pain point / contrast gap / number compression / redefinition / stance declaration / lingering aftertaste — each with examples, counter-examples, and failure causes.
- **Original mode.** Given a topic instead of a source text, it first locates the reader's concrete situation, then writes the sentence they would not say out loud.
- **Spread is computable.** `reversal×1.3 + sting×1.2 + resonance×1.0 + aftertaste×0.8 − length penalty`. Ranking has a basis.

## Structure

| Path | What it holds |
|---|---|
| `SKILL.md` | Full method: four defining dimensions, four-stage funnel, eight skeletons, six red lines, five-step polish |
| `scripts/scan.py` | Stage-one scanner — `--top` `--all` `--json` `--explain` |
| `scripts/lexicon.json` | Lexicon data: judgment words / AI flavor / clichés / soft markers. Tune weights here, not in code |
| `references/quote-patterns.md` | Eight skeletons with examples and counter-examples |
| `references/scoring-rubric.md` | Stage-by-stage rules, spread formula, and documented script blind spots |
| `references/ai-flavor-blacklist.md` | AI-flavor word list plus 5 structural patterns regex cannot catch |
| `examples/sample-article.txt` | Test source |
| `examples/01-article-extract.md` | Full extraction case with before/after rewrite trace |
| `examples/02-original-mode.md` | Original-mode case |
| `templates/` | Output template |
| `assets/gallery/` | Published output (quote cards) |

## How to use

**Locate the core conflict → run the funnel → rewrite against a skeleton → tag each line → sort by spread.**

```bash
python scripts/scan.py article.txt --top 12
python scripts/scan.py article.txt --all --json
python scripts/scan.py --explain
```

## ⚠️ The one thing that matters: stage one is a sieve, not a judge

After the script runs, **you must manually sweep for parallel constructions.**

Observed: the script's top-ranked line was "听起来很唬人，但其实很简单" (4.5) — a transitional sentence, rejected by hand.

Meanwhile one of the strongest lines in the article:

> 你看到的是它在埋头干活，后台发生的是 Token 持续流动。

28 characters, mid-paragraph, zero judgment words — the script scored it 1.5 and it **never entered the candidate pool**. It was recovered by hand.

Lines that win through parallelism and imagery are invisible to regex. Manual sweep patterns: `不是…是` / `你看到的…后台发生的是` / `有人…有人`.

## Six red lines

1. No empty uplift, no motivational filler
2. No AI triads (three-part parallelism, symmetry addiction)
3. No exclamation-mark padding
4. No aphorism voice, no faux famous-quote tone
5. **Never use an attributed quote you cannot source**
6. 12-40 characters per line; longer gets cut

## Five-step polish

**Cut → swap → shorten → land → read aloud.**

Cut subordinate clauses, swap abstract nouns, compress to the shortest form, land on a strong final syllable, then read it out loud — a line that trips on the tongue trips the reader too.

## Provenance

Extracted from `infographic-maker`, which only had "distill 3-7 key points". This version expands opinion distillation into a full quote production line. The source skill is unchanged. MIT License.
