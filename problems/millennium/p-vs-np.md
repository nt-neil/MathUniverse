# P vs NP 問題(P versus NP Problem)

> 「能快速驗證答案的問題,是否也都能快速找到答案?」

| | |
|---|---|
| **領域** | 計算複雜度理論 Computational Complexity(MSC 68Q15) |
| **提出** | 1971 年 Stephen Cook 正式提出;Leonid Levin 於蘇聯獨立提出 |
| **狀態** | 未解決 |
| **懸賞** | 千禧年大獎 100 萬美元(Clay Mathematics Institute, 2000) |

## 問題陳述

**直觀版**:有些問題「驗證一個候選解」很容易,但「從頭找到解」似乎很難。例如數獨:給你一個填好的盤面,檢查它對不對只要幾秒;但從空盤面解出來可能要想很久。P vs NP 問的是:這種「找解比驗證難」的現象是本質的,還是只因為我們還沒找到聰明的演算法?

**正式版**:令 $P$ 為確定性圖靈機在多項式時間內可判定的語言類,$NP$ 為非確定性圖靈機在多項式時間內可判定的語言類(等價地:存在多項式時間可驗證的證書 certificate 的語言類)。問:

$$P \stackrel{?}{=} NP$$

已知 $P \subseteq NP$。若存在任一 NP 完全(NP-complete)問題(如 SAT)屬於 $P$,則 $P = NP$;反之,只要證明 SAT 沒有多項式時間演算法,即得 $P \neq NP$。

## 背景與重要性

Cook(1971)證明了 SAT 是 NP 完全的(Cook–Levin 定理),Karp(1972)接著列出 21 個 NP 完全問題,顯示排程、圖著色、整數規劃等大量實際問題彼此「一樣難」。今天已知的 NP 完全問題數以千計,遍布最佳化、生物資訊、經濟學。

重要性:若 $P = NP$ 且演算法實用,現代密碼學(依賴單向函數)將崩塌,同時最佳化與自動定理證明會發生革命;若 $P \neq NP$(多數專家的預期),則確立了「創造性搜尋本質上比驗證難」,並為密碼學提供地基。此問題也是理解「證明的難度」本身的核心——它與數理邏輯的有界算術(bounded arithmetic)、證明複雜度(proof complexity)深度相連。

## 目前狀態

截至 2026 年 7 月:未解決,且已知三大障礙(barriers)說明現有技術不足——

- **相對化障礙**(Baker–Gill–Solovay, 1975):對角化類技術無法區分 P 與 NP。
- **自然證明障礙**(Razborov–Rudich, 1994):在合理密碼學假設下,「自然」的電路下界證法行不通。
- **代數化障礙**(Aaronson–Wigderson, 2008):結合代數技巧的相對化推廣同樣受限。

無條件電路下界仍停在很弱的層級(對一般電路,NP 問題的已知下界僅約 $5n$ 級別的線性下界)。近年重心轉向**元複雜度(meta-complexity)**——研究「判斷一個問題有多難」這件事本身的複雜度(如 MCSP:最小電路大小問題),以及**硬度放大(hardness magnification)**:證明看似溫和的下界即可放大成重大分離。2025 年 Ryan Williams 的時間—空間模擬結果則在 P vs PSPACE 方向帶來 50 年來首次實質推進。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1971–1973 | SAT 為 NP 完全(Cook–Levin 定理) | S. Cook;L. Levin |
| 1972 | 21 個 NP 完全問題 | R. Karp |
| 1975 | 相對化障礙 | Baker, Gill, Solovay |
| 1985 | 單調電路對 CLIQUE 的指數下界 | A. Razborov |
| 1994 | 自然證明障礙 | Razborov, Rudich |
| 2008 | 代數化障礙 | Aaronson, Wigderson |
| 2011 | $NEXP \not\subseteq ACC^0$(電路下界重要突破) | R. Williams |
| 2018–2022 | 元複雜度興起:MKTP/MCSP 的 worst-case 到 average-case 歸約、部分 MCSP 的 NP 難度 | S. Hirahara 等 |
| 2024 | Tree Evaluation 可在 $O(\log n \cdot \log\log n)$ 空間解(STOC 2024),成為後續模擬結果的引擎 | J. Cook, I. Mertz |
| 2025 | $\mathrm{TIME}[t] \subseteq \mathrm{SPACE}[O(\sqrt{t\log t})]$,STOC 2025 最佳論文;推得存在 $O(n)$ 空間可解、但多帶圖靈機需 $n^{2-\varepsilon}$ 時間的顯式問題,是 P vs PSPACE 方向的實質進展。[arXiv:2502.17779](https://arxiv.org/abs/2502.17779) | R. Williams |
| 2025 | Clay 研究所舉辦「P vs NP and Complexity Lower Bounds」專題研討會,聚焦電路下界、元複雜度、GCT 等路線的現況。[claymath.org](https://www.claymath.org/events/p-vs-np-and-complexity-lower-bounds/) | Clay Mathematics Institute |

## 主要研究方法

- **電路下界(circuit lower bounds)**:證明顯式函數需要超多項式大小電路(足以推出 $P \neq NP$ 的更強形式)。優:目標明確;劣:受自然證明障礙限制,數十年僅在受限電路類(AC⁰、ACC⁰、單調電路)有成果。
- **元複雜度(meta-complexity)**:研究 MCSP、Kolmogorov 複雜度變體(MKTP、$\text{K}^t$)的難度。優:繞開部分傳統障礙,且與單向函數存在性等密碼學基礎問題等價連動;劣:核心問題(MCSP 是否 NP 難)本身未解。
- **硬度放大(hardness magnification)**:顯示對稀疏問題的極弱下界即可推出重大分離。優:把目標「降價」;劣:所需的弱下界恰好落在現有技術的盲區(locality barrier)。
- **幾何複雜度理論(GCT, Mulmuley–Sohoni)**:用代數幾何與表示論攻永久式 vs 行列式($VP$ vs $VNP$)。優:原則上能繞過自然證明;劣:所需的表示論計算極深,短期難見效。
- **證明複雜度與有界算術**:研究「$P \neq NP$ 是否在弱算術系統中不可證」,將問題元數學化。

## AI 可以怎麼幫忙

- **形式化現況**:Cook–Levin 定理已有 Lean 4 形式化(社群多個版本,如基於 Turing machine 模型的形式化專案);複雜度類的系統性 Lean 庫仍在早期。將三大障礙定理(尤其 Baker–Gill–Solovay)形式化是可行的中期目標。
- **ML/LLM 輔助探索的已知嘗試**:尚無 AI 直接推進 P vs NP 的可信結果。相關的是 AI 輔助搜尋組合結構(如 FunSearch 在 cap set 問題上的成果)顯示「搜尋顯式構造/反例」是 AI 的強項——這對尋找更好的 SAT 演算法或受限電路類的顯式難函數可能有用。
- **本 repo 可做的事**:
  - 整理 NP 完全問題清單與歸約關係圖(資料整理,可自動抓 Karp 21 + 後續文獻)。
  - 追蹤元複雜度文獻(Hirahara、Oliveira、Santhanam 等人的新作)並維護註解書目。
  - 對小規模受限電路類跑窮舉/SAT solver 實驗,重現已知小電路下界(如特定函數的最小電路大小),建立可驗證的實驗基線。

## 關鍵文獻與資源

- Clay 官方問題描述(S. Cook 撰):https://www.claymath.org/millennium/p-vs-np/
- S. Aaronson, "P ?= NP" 綜述(2016):https://www.scottaaronson.com/papers/pnp.pdf
- R. Williams, "Simulating Time With Square-Root Space"(2025, STOC 2025 最佳論文):https://arxiv.org/abs/2502.17779
- J. Cook, I. Mertz, "Tree Evaluation is in Space O(log n · log log n)"(STOC 2024):https://eccc.weizmann.ac.il/report/2023/174/
- Simons Institute 元複雜度專題(2023 program 與後續演講):https://simons.berkeley.edu/programs/meta-complexity
- Clay 2025 研討會「P vs NP and Complexity Lower Bounds」:https://www.claymath.org/events/p-vs-np-and-complexity-lower-bounds/
