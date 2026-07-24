# 數學世界 MathUniverse

> 用開源與 AI 的力量,系統性記錄、分析、追蹤這個世界上最困難的數學問題。

**English summary**: *MathUniverse* (數學世界, "Math World") is an open-source, AI-assisted knowledge base that documents the world's hardest open problems in mathematics — their statements, history, current status, and the latest research developments — written primarily in Traditional Chinese with English terminology. Contributions welcome.

## 這個專案在做什麼

現代數學依 [MSC 分類](taxonomy/msc-overview.md)已細分出超過 6,000 個研究主題,其中散布著一批世界級的未解難題。這個專案要做三件事:

1. **記錄**:為每個難題建立一份結構化檔案 —— 問題陳述、背景、目前狀態、進展時間線、關鍵文獻。
2. **追蹤**:用 AI 持續蒐集並查證最新研究進展(論文、預印本、學界動態),保持內容是活的。
3. **開放**:所有內容開源(CC BY 4.0),讓任何人都能認識、學習、參與這些數學界的重大議題。

我們不宣稱 AI 已經解決任何未解問題;這裡是知識庫與協作平台,讓人類與 AI 的力量在同一個地方累積。

## 難題總表

### 千禧年大獎難題(Millennium Prize Problems)

克雷數學研究所於 2000 年提出的七大難題,每題懸賞 100 萬美元。

| 難題 | 領域 | 狀態 |
|---|---|---|
| [黎曼猜想 Riemann Hypothesis](problems/millennium/riemann-hypothesis.md) | 數論/分析 | 未解決 |
| [P vs NP](problems/millennium/p-vs-np.md) | 計算複雜度 | 未解決 |
| [Birch–Swinnerton-Dyer 猜想](problems/millennium/birch-swinnerton-dyer.md) | 數論/代數幾何 | 未解決 |
| [Hodge 猜想](problems/millennium/hodge-conjecture.md) | 代數幾何 | 未解決 |
| [Navier–Stokes 存在性與光滑性](problems/millennium/navier-stokes.md) | 偏微分方程 | 未解決 |
| [Yang–Mills 存在性與質量間隙](problems/millennium/yang-mills.md) | 數學物理 | 未解決 |
| [龐加萊猜想 Poincaré Conjecture](problems/millennium/poincare-conjecture.md) | 拓樸 | ✅ 已解決(Perelman, 2003) |

### 其他著名難題

| 難題 | 領域 | 狀態 |
|---|---|---|
| [哥德巴赫猜想 Goldbach Conjecture](problems/number-theory/goldbach.md) | 數論 | 未解決 |
| [孿生質數猜想 Twin Prime Conjecture](problems/number-theory/twin-primes.md) | 數論 | 未解決 |
| [Collatz 猜想(3n+1)](problems/number-theory/collatz.md) | 數論/動態系統 | 未解決 |
| [掛谷猜想 Kakeya Conjecture](problems/analysis/kakeya.md) | 調和分析/幾何測度論 | 部分解決(3 維情形於 2025 年證明) |

## 專案結構

```
taxonomy/    數學研究領域的分類地圖(MSC)
problems/    每個難題一份結構化檔案(格式見 problems/_template.md)
ai/          AI 如何協助數學研究的方法論與工具
```

## 如何參與

見 [CONTRIBUTING.md](CONTRIBUTING.md)。新增難題、補充最新進展、修正錯誤、翻譯,都歡迎。

## 授權

內容採 [CC BY 4.0](LICENSE) 授權。
