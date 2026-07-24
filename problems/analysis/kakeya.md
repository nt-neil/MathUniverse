# 掛谷猜想(Kakeya Conjecture)

> 在 $n$ 維空間中,一個包含「每個方向的單位線段」的集合,可以小到什麼程度?猜想:它的維數必須是滿的 $n$。

| | |
|---|---|
| **領域** | 分析 Analysis(調和分析、幾何測度論) |
| **提出** | 1917 年掛谷宗一(Sōichi Kakeya)提出針問題;集合維數猜想成形於 1970 年代 |
| **狀態** | 部分解決($n=2$ 於 1971、$n=3$ 於 2025 解決;$n\ge 4$ 仍開放) |
| **懸賞** | 無正式懸賞 |

## 問題陳述

**直觀版**:掛谷的原始問題是「一根單位長的針,在平面上掉頭 180 度,最少要掃過多大面積?」Besicovitch 給出驚人答案:面積可以任意小,甚至存在測度為零、卻包含所有方向單位線段的集合(Besicovitch 集/掛谷集)。於是問題變成:這種集合雖然體積可以是零,它有沒有辦法在「維數」上也很小?猜想說不行——它看起來再稀疏,維數都必須是滿的。

**正式版**:稱 $E\subseteq\mathbb{R}^n$ 為掛谷集(Kakeya set),若對每個方向 $\omega\in S^{n-1}$,$E$ 都包含一條方向為 $\omega$ 的單位線段。**掛谷集合猜想**:每個 $\mathbb{R}^n$ 中的掛谷集,其 Hausdorff 維數與 Minkowski 維數皆等於 $n$:

$$\dim_H(E)=\dim_M(E)=n.$$

另有更強的「掛谷極大函數猜想」(Kakeya maximal function conjecture),涉及管狀鄰域的重疊估計,在 $n\ge 3$ 仍屬開放。

## 背景與重要性

掛谷猜想是調和分析「猜想塔」的地基:它被限制猜想(restriction conjecture)、Bochner–Riesz 猜想、局部光滑化(local smoothing)猜想等所蘊含,反過來這些關於 Fourier 變換的核心開放問題都「至少和掛谷一樣難」。它同時連結疊加原理下的 PDE 估計、關於 Dirichlet 多項式的 Montgomery 猜想(解析數論)、以及加法組合學(Bourgain、Katz–Tao 的和積方法)。2008 年 Dvir 用多項式方法幾頁解決有限體版本,更使它成為多項式方法、代數幾何工具進入分析的橋頭堡。

## 目前狀態

截至 2026 年 7 月:
- $n=2$:已解決(Davies 1971)。
- $n=3$:**已解決**。Hong Wang(王虹)與 Joshua Zahl 於 2025 年 2 月 24 日貼出 127 頁預印本 [arXiv:2502.17655](https://arxiv.org/abs/2502.17655),證明 $\mathbb{R}^3$ 中每個掛谷集的 Hausdorff 與 Minkowski 維數皆為 3。**注意:截至查證時(2026-07)該文仍是 arXiv 預印本、未見正式期刊發表**,但已被 Tao 等專家詳細檢視並公開講解,學界普遍接受;Hong Wang 並於 2026 年 7 月獲頒 Fields 獎,得獎工作正是此結果。
- $n\ge 4$:**開放**。已知下界遠低於 $n$(Wolff 型 $(n+2)/2$ 與 Katz–Tao 加法組合改進)。專家(如 Tao)評估:induction on scales 等框架可望推廣,但高維的個案分析(plany/grainy 結構分類)複雜度大增,非自動延伸。
- 更強的極大函數版本與其下游(restriction、Bochner–Riesz)在 $n\ge 3$ 仍開放;3 維集合猜想的解決被視為攻向這些猜想的新起點。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1917 | 提出針問題 | 掛谷宗一 |
| 1919–1928 | 構造測度為零的掛谷集;針問題答案為「面積可任意小」 | Abram Besicovitch |
| 1971 | $n=2$ 情形解決:平面掛谷集維數為 2 | Roy Davies |
| 1995 | $n=3$ 下界 $5/2$(hairbrush 論證);一般維下界 $(n+2)/2$ | Thomas Wolff |
| 1999–2002 | 突破 $5/2$:下界 $2.500000001$;加法組合方法進入 | Katz–Łaba–Tao、Bourgain、Katz–Tao |
| 2008 | 有限體掛谷猜想以多項式方法完全解決 | Zeev Dvir |
| 2019 | $n=3$ 下界 $2.5+\varepsilon$(具體常數) | Nets Katz、Joshua Zahl |
| 2022–2026 | 證明 sticky Kakeya 猜想(3 維關鍵特例),刊於 [JAMS](https://www.ams.org/journals/jams/)(2026);另證 $\mathbb{R}^3$ 掛谷集 Assouad 維數結果(Inventiones Math., 2025) | Hong Wang、Joshua Zahl |
| 2025-02 | **證明 3 維掛谷集合猜想**(預印本):[arXiv:2502.17655](https://arxiv.org/abs/2502.17655);[Tao 的技術導讀](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/);[Quanta 報導](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/) | Hong Wang、Joshua Zahl |
| 2026-07 | Hong Wang 以掛谷工作獲頒 Fields 獎(ICM 2026,費城):[Simons Foundation 公告](https://www.simonsfoundation.org/2026/07/23/2026-fields-medals-awarded-to-four-of-worlds-top-mathematicians/)、[NPR 報導](https://www.npr.org/2026/07/23/g-s1-135032/in-a-first-chinese-woman-wins-the-prestigious-fields-medal) | IMU |

## 主要研究方法

- **幾何組合(Wang–Zahl 路線)**:induction on scales + 對「幾乎反例」的結構分類(sticky/plany/grainy),證明反例若存在必具剛性結構,再逐一排除。3 維成功的關鍵;推廣到高維是當前主攻方向,難點在結構分類的組合爆炸。
- **加法組合/和積估計**(Bourgain、Katz–Tao):把線段重疊翻譯成和集–差集問題。曾給出高維最好下界之一,可望與新方法結合。
- **多項式方法**(Dvir、Guth):有限體情形的完勝工具,啟發了 polynomial partitioning(Guth–Katz),後者已是 restriction 理論的標準武器;但在 $\mathbb{R}^n$ 掛谷本體上尚未單獨制勝。
- **極大函數/振盪積分路線**:直接攻 Kakeya 極大不等式與 restriction 猜想,回頭蘊含集合猜想。難度更高,但回報是整座猜想塔。

## AI 可以怎麼幫忙

- **形式化現況**:掛谷猜想(即使 2 維情形)尚無已知的完整 Lean/Coq 形式化;Mathlib 已有 Hausdorff 測度與 Hausdorff 維數的基礎建設,因此「形式化掛谷集定義與 2 維 Davies 定理」是一個現實可行、尚無人完成的目標;長期而言 Wang–Zahl 證明(127 頁、高度組合)是形式化審查的高價值標的——尤其在其仍未正式發表的現階段,形式化等於獨立驗證。
- **與調和分析的關聯**:掛谷位於 restriction–Bochner–Riesz–local smoothing 蘊含網的底層,LLM 適合做的是把這張蘊含圖(誰蘊含誰、在哪個維度、出自哪篇論文)整理成可機讀、可查證的資料結構——目前這些關係散落在綜述與民間傳承中。
- **本 repo 可做的事**:(1)維護上述「猜想蘊含圖」與各維度最佳已知下界表(附出處);(2)追蹤 arXiv:2502.17655 的審查/發表狀態與高維推廣的新預印本;(3)整理入門讀物路徑(見下)並撰寫中文導讀;(4)有限體掛谷(Dvir 證明只需線性代數與多項式)適合做成 Lean 練習專案與教學材料。

## 關鍵文獻與資源

- Hong Wang, Joshua Zahl, *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions*, [arXiv:2502.17655](https://arxiv.org/abs/2502.17655)(預印本)
- Terence Tao, [The three-dimensional Kakeya conjecture, after Wang and Zahl](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/)——最好的技術導讀
- [Introduction to the proof of the Kakeya conjecture](https://arxiv.org/pdf/2505.07695)(arXiv:2505.07695)與 Bourbaki 式講稿 [The Kakeya conjecture, after Wang and Zahl](https://arxiv.org/html/2604.03416v1)(arXiv:2604.03416)——證明的兩篇綜述
- [A Survey of the Kakeya conjecture, 2000–2025](https://arxiv.org/pdf/2512.09397)(arXiv:2512.09397)——四分之一世紀進展總覽
- 科普:[Quanta Magazine 報導](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/)、[IAS: A Three-Dimensional Breakthrough](https://www.ias.edu/ideas/three-dimensional-breakthrough)
