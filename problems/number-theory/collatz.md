# 考拉茲猜想(Collatz Conjecture,又稱 3n+1 問題)

> 從任何正整數出發,反覆做「偶數除以 2、奇數乘 3 加 1」,是否最後必定掉到 1?

| | |
|---|---|
| **領域** | 數論 Number Theory(兼涉動力系統、遍歷理論) |
| **提出** | 約 1937 年,Lothar Collatz |
| **狀態** | 未解決 |
| **懸賞** | Erdős 曾懸賞 500 美元;日本 Bakuage 公司 2021 年懸賞 1.2 億日圓(約 100 萬美元) |

## 問題陳述

**直觀版**:取任一正整數。偶數就砍半,奇數就乘 3 加 1,一直重複。例如 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1。猜想:不論從哪個正整數出發,都會走到 1。

**正式版**:定義 Collatz 映射 $T:\mathbb{Z}^+\to\mathbb{Z}^+$:

$$T(n)=\begin{cases}n/2,&n\equiv 0\pmod 2\\ 3n+1,&n\equiv 1\pmod 2\end{cases}$$

猜想:對每個 $n\in\mathbb{Z}^+$,存在 $k$ 使得 $T^{(k)}(n)=1$。等價地說:軌道不存在發散到無窮的情形,也不存在 $1\to 4\to 2\to 1$ 以外的循環(cycle)。

## 背景與重要性

一般認為由 Lothar Collatz 於 1930 年代提出,1950 年代起在數學圈流傳(亦稱 Syracuse 問題、Ulam 問題、Hasse 演算法)。它的重要性不在於結論本身,而在於它暴露了現有數學工具的極限:一個小學生能懂的迭代規則,混合了乘法結構($3n+1$)與二進位結構(除以 2),而數論目前幾乎沒有同時掌控這兩種結構的工具。Erdős 曾說「數學還沒準備好面對這種問題」。此外 Conway(1972)證明 Collatz 型迭代的廣義版本是不可判定的(undecidable),說明這類問題與可計算性理論有深刻聯繫;猜想本身也是遍歷理論、隨機模型(3-adic 隨機漫步)方法的試金石。

## 目前狀態

截至 2026 年 7 月:猜想對「幾乎所有」起點成立(Tao 2019,對數密度意義下),且已用超級電腦驗證到 $2^{71}\approx 2.36\times 10^{21}$ 以下所有起點都收斂到 1(Barina 2025)。但「幾乎所有」與「所有」之間有本質鴻溝:目前沒有任何已知方法能排除(a)某條發散軌道、(b)某個未知的巨大循環。驗證上限同時給出循環長度的下界——任何非平凡循環必須極長(此類下界隨驗證範圍推進,方法源自 Eliahou 1993)。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 約 1937 | 提出問題 | Lothar Collatz |
| 1972 | 證明廣義 Collatz 函數的停機問題不可判定 | John Conway |
| 1976 | 幾乎所有 $n$(自然密度 1)的軌道會降到 $n$ 以下 | Riho Terras |
| 1993 | 由驗證範圍導出非平凡循環長度下界的方法 | Shalom Eliahou |
| 2019 | 幾乎所有軌道達到「幾乎有界」的值:對任意 $f(N)\to\infty$,幾乎所有 $N$(對數密度)滿足 $\min$ 軌道值 $\le f(N)$。[arXiv:1909.03562](https://arxiv.org/abs/1909.03562),2022 年刊於 [Forum of Mathematics, Pi](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F) | Terence Tao |
| 2020 | GPU 分散式驗證至 $2^{68}$(刊於 J. of Supercomputing) | David Barina |
| 2025 | 驗證上限推進至 $2^{71}$,並發現 4 個新的 path record;動用歐洲多台超級電腦、GPU 加速達 1335 倍。[專案頁](https://pcbarina.fit.vutbr.cz/)、[論文資訊](https://www.fit.vut.cz/research/result/c197809/.en) | David Barina 團隊 |
| 2025–2026 | Collatz Conjecture Challenge 啟動:逐篇形式化 Collatz 文獻,截至 2026 年中已完成 1/363 篇,Tao 2022 論文的形式化已進入待審核(ready for audit)階段。[ccchallenge.org](https://ccchallenge.org/) | 開源社群 |

## 主要研究方法

- **機率/遍歷方法**:把軌道視為偏隨機漫步(奇數步乘 $3/2$ 期望下降),Tao 的突破即是把 3-adic 隨機漫步的特徵函數估計做到極致。優:對「幾乎所有」陳述威力最強;劣:天生無法覆蓋測度零的例外集,而猜想恰恰要求零例外。
- **循環排除(數論方法)**:用線性型對數下界(Baker 理論)與計算驗證範圍,排除短循環、給出循環長度下界。優:結果無條件;劣:只碰得到循環,碰不到發散軌道。
- **計算驗證**:GPU + 超級電腦推進驗證上限。優:提供下界輸入、可能找到反例;劣:若猜想為真,永遠驗證不完。
- **可計算性視角**:Conway 的不可判定性結果暗示「不存在一刀切的通用算法」,但不代表 Collatz 本身不可判定——它只是警告不要期待太一般的方法。

## AI 可以怎麼幫忙

- **形式化(Lean)現況**:[ccchallenge.org](https://ccchallenge.org/) 正逐篇形式化 371 篇 Collatz 文獻(透過 GitHub org `ccchallenge-org` 與 Discord 協作),Tao 的主定理形式化已待審核。這是 LLM 輔助形式化(自動補證明、翻譯紙本論證)的理想試場;值得注意的是,已有形式化嘗試在過程中抓出紙本論證的錯誤步驟,顯示「形式化即審查」的價值。
- **大規模計算**:Barina 的驗證程式碼是開源的;可貢獻演算法改進(例如更好的查表/篩法)、或把驗證帳本(哪些區間誰驗過)做成可重現的公開資料集。
- **本 repo 可做的事**:(1)整理「驗證上限 ↔ 循環長度下界」的換算表並隨新驗證更新;(2)追蹤 ccchallenge 的形式化進度並鏡像其論文清單;(3)用統計模型對 path record、停止時間分佈做可重現的實驗筆記;(4)維護「錯誤證明清單」——arXiv 與網路上每年出現多篇宣稱證明,整理常見錯誤模式本身就有教育價值。

## 關鍵文獻與資源

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562](https://arxiv.org/abs/1909.03562);作者的[部落格導讀](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/)
- Jeffrey Lagarias(編),*The Ultimate Challenge: The 3x+1 Problem*(AMS, 2010)——標準綜述文集
- David Barina, [Convergence verification of the Collatz problem](https://pcbarina.fit.vutbr.cz/)——驗證專案首頁($2^{71}$)
- [The Collatz Conjecture Challenge](https://ccchallenge.org/)——Collatz 文獻形式化開源計畫
- Terence Tao 演講影片:[Almost all Collatz orbits attain almost bounded values](https://www.youtube.com/watch?v=k-dtx8s2ehM)
