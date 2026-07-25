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
| [黎曼猜想 Riemann Hypothesis](problems/millennium/riemann-hypothesis/) | 數論/分析 | 未解決 |
| [P vs NP](problems/millennium/p-vs-np/) | 計算複雜度 | 未解決 |
| [Birch–Swinnerton-Dyer 猜想](problems/millennium/birch-swinnerton-dyer/) | 數論/代數幾何 | 未解決 |
| [Hodge 猜想](problems/millennium/hodge-conjecture/) | 代數幾何 | 未解決 |
| [Navier–Stokes 存在性與光滑性](problems/millennium/navier-stokes/) | 偏微分方程 | 未解決 |
| [Yang–Mills 存在性與質量間隙](problems/millennium/yang-mills/) | 數學物理 | 未解決 |
| [龐加萊猜想 Poincaré Conjecture](problems/millennium/poincare-conjecture/) | 拓樸 | ✅ 已解決(Perelman, 2003) |

### 其他著名難題

| 難題 | 領域 | 狀態 |
|---|---|---|
| [哥德巴赫猜想 Goldbach Conjecture](problems/number-theory/goldbach/) | 數論 | 未解決 |
| [孿生質數猜想 Twin Prime Conjecture](problems/number-theory/twin-primes/) | 數論 | 未解決 |
| [Collatz 猜想(3n+1)](problems/number-theory/collatz/) | 數論/動態系統 | 未解決 |
| [掛谷猜想 Kakeya Conjecture](problems/analysis/kakeya/) | 調和分析/幾何測度論 | 部分解決(3 維情形於 2025 年證明) |

### 更多難題:總目錄

上面兩張表只是深度檔案層。**[catalog/ 未解難題總目錄](catalog/)** 以領域分檔收錄了 **246 題**(數論、代數、幾何拓樸、分析 PDE、組合圖論、邏輯集合論、計算複雜度、機率動態物理),外加[著名難題名單總覽](catalog/famous-lists.md)(希爾伯特 23 題、Smale 18 題、Landau 4 題逐題現況)。每題狀態經網路查證,2020 年代的重大變動(如掛谷 3 維已證、雅可比猜想 2026 年宣稱反例)都已標註。

## 專案結構

```
catalog/     未解難題總目錄:一題一列的百科索引層(246 題)
problems/    深度檔案層:一題一資料夾(格式見 problems/_template/README.md)
taxonomy/    數學研究領域的分類地圖(MSC)
ai/          AI 如何協助數學研究的方法論與工具
```

## 如何參與

見 [CONTRIBUTING.md](CONTRIBUTING.md)。新增難題、補充最新進展、修正錯誤、翻譯,都歡迎。

## Security & Privacy / 安全與隱私聲明

This is a documentation-only repository: it contains no executable application code, collects no data, and stores no credentials. Every push and pull request is scanned for accidentally committed secrets by CI ([Gitleaks](https://github.com/gitleaks/gitleaks)), with a weekly full-history scan. If you find leaked credentials or private information anywhere in this repository or its history, please report it by opening a GitHub issue (or, for sensitive reports, via the repository owner's GitHub profile contact) — do not post the leaked value itself in the issue.

本專案為純文件知識庫:不含可執行的應用程式碼、不蒐集資料、不儲存任何憑證。所有 push 與 pull request 均由 CI(Gitleaks)自動掃描是否誤提交金鑰,並每週對完整歷史全面掃描一次。若你在本 repo 或其歷史中發現外洩的憑證或私人資訊,請開 GitHub issue 回報(敏感內容請改走 repo 擁有者 GitHub 個人頁的聯絡方式),並請勿在 issue 中貼出外洩內容本身。

Contributors: never commit API keys, tokens, private file paths (e.g. `/Users/<name>/...`), or personal contact information. See [CONTRIBUTING.md](CONTRIBUTING.md).

給貢獻者:請勿提交 API 金鑰、token、私人檔案路徑(如 `/Users/<name>/...`)或個人聯絡資訊。詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

內容採 [CC BY 4.0](LICENSE) 授權。**例外**:`taxonomy/msc/` 目錄收錄的 MSC2020 分類資料 © Mathematical Reviews(AMS)與 zbMATH,依 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 散布,詳見 [taxonomy/msc/LICENSE-MSC.md](taxonomy/msc/LICENSE-MSC.md)。
