# MathUniverse 數學世界

**English** | [繁體中文](README.md)

> Using open source and AI to systematically document, analyze, and track the hardest problems in mathematics.

The knowledge base itself is written primarily in Traditional Chinese, with English terminology alongside. This page is an English guide to what is here.

## What this project does

Modern mathematics is divided into more than 6,000 research topics under the [MSC classification](taxonomy/msc-overview.md), and scattered among them are a set of world-class open problems. This project does three things:

1. **Document**: build a structured file for each problem — statement, background, current status, timeline of progress, key references.
2. **Track**: use AI to continuously collect and verify new research (papers, preprints, community news) so the content stays alive.
3. **Open**: all content is open source (CC BY 4.0), so anyone can discover, learn about, and take part in these major questions.

We do not claim that AI has solved any open problem. This is a knowledge base and collaboration space where human and AI effort accumulate in one place.

### Three layers

| Layer | Location | Size (2026-07) | What it is |
|---|---|---|---|
| 🗺 Map | [`taxonomy/`](taxonomy/) | Full MSC 2020 tree, **6,006 entries** | The coordinate system for the whole landscape of mathematical research |
| 📇 Index | [`catalog/`](catalog/) | **246 problems** across 8 fields + 4 famous lists | An encyclopedic index of well-known problems, one row each, status verified |
| 📚 Deep | [`problems/`](problems/) | **11 problems** (growing) | One folder per problem: statement, timeline, references, directions for AI collaboration |

Once an index entry has gathered enough material it is "promoted" to a deep-layer folder. The goal is to tag every index entry with its MSC code so the three layers link together. See the [roadmap](ROADMAP.md).

## Problem overview

### Millennium Prize Problems

Seven problems posed by the Clay Mathematics Institute in 2000, each carrying a US$1 million prize.

| Problem | Field | Status |
|---|---|---|
| [Riemann Hypothesis](problems/millennium/riemann-hypothesis/) | Number theory / analysis | Open |
| [P vs NP](problems/millennium/p-vs-np/) | Computational complexity | Open |
| [Birch–Swinnerton-Dyer Conjecture](problems/millennium/birch-swinnerton-dyer/) | Number theory / algebraic geometry | Open |
| [Hodge Conjecture](problems/millennium/hodge-conjecture/) | Algebraic geometry | Open |
| [Navier–Stokes Existence and Smoothness](problems/millennium/navier-stokes/) | Partial differential equations | Open |
| [Yang–Mills Existence and Mass Gap](problems/millennium/yang-mills/) | Mathematical physics | Open |
| [Poincaré Conjecture](problems/millennium/poincare-conjecture/) | Topology | ✅ Solved (Perelman, 2003) |

### Other famous problems

| Problem | Field | Status |
|---|---|---|
| [Goldbach Conjecture](problems/number-theory/goldbach/) | Number theory | Open |
| [Twin Prime Conjecture](problems/number-theory/twin-primes/) | Number theory | Open |
| [Collatz Conjecture (3n+1)](problems/number-theory/collatz/) | Number theory / dynamical systems | Open |
| [Kakeya Conjecture](problems/analysis/kakeya/) | Harmonic analysis / geometric measure theory | Partially solved (3-dimensional case proved in 2025) |

### More problems: the full catalog

The two tables above cover only the deep layer. **[The catalog/ index of open problems](catalog/)** lists **246 problems** in per-field files (number theory, algebra, geometry and topology, analysis and PDE, combinatorics and graph theory, logic and set theory, computational complexity, probability / dynamics / physics), plus an [overview of famous problem lists](catalog/famous-lists.md) (Hilbert's 23, Smale's 18, Landau's 4, each with its current status). Every status has been checked against online sources, and major changes from the 2020s are marked (for example, Kakeya proved in 3 dimensions, and a claimed counterexample to the Jacobian conjecture in 2026).

## Project structure

```
catalog/       Index layer: catalog of open problems, one row each (246; format in catalog/_format.md)
problems/      Deep layer: one folder per problem (format in problems/_template/README.md)
taxonomy/      Map layer: MSC overview + msc/ full classification tree (6,006 entries; license below)
ai/            Methodology for how AI can assist mathematical research
tools/         Data engineering scripts (e.g. tools/msc/generate.py, the classification tree generator)
ROADMAP.md     Project vision and roadmap
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New problems, updates on recent progress, corrections, and translations are all welcome.

## Security & Privacy

This is a documentation-only repository: it contains no executable application code, collects no data, and stores no credentials. Every push and pull request is scanned for accidentally committed secrets by CI ([Gitleaks](https://github.com/gitleaks/gitleaks)), with a weekly full-history scan. If you find leaked credentials or private information anywhere in this repository or its history, please report it by opening a GitHub issue (or, for sensitive reports, via the repository owner's GitHub profile contact) — do not post the leaked value itself in the issue.

Contributors: never commit API keys, tokens, private file paths (e.g. `/Users/<name>/...`), or personal contact information. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Content is licensed under [CC BY 4.0](LICENSE). **Exception**: the MSC2020 classification data in `taxonomy/msc/` is © Mathematical Reviews (AMS) and zbMATH, distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/); see [taxonomy/msc/LICENSE-MSC.md](taxonomy/msc/LICENSE-MSC.md).
