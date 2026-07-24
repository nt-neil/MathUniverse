# Birch–Swinnerton-Dyer 猜想(Birch and Swinnerton-Dyer Conjecture)

> 一條橢圓曲線上有理點的「多寡」(Mordell–Weil 秩),可以從它的 L 函數在 $s=1$ 處的解析行為讀出來。

| | |
|---|---|
| **領域** | 數論 Number Theory(算術幾何 Arithmetic Geometry) |
| **提出** | 1960 年代初,Bryan Birch 與 Peter Swinnerton-Dyer(基於 EDSAC 電腦計算) |
| **狀態** | 部分解決(解析秩 0 與 1 的情形已知;一般情形未解決) |
| **懸賞** | 千禧年大獎 100 萬美元(Clay Mathematics Institute) |

## 問題陳述

**直觀版**:橢圓曲線 $E: y^2 = x^3 + ax + b$($a,b \in \mathbb{Q}$)上的有理點構成一個有限生成交換群 $E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus T$(Mordell–Weil 定理),其中 $r$ 稱為秩(rank)。另一方面,把曲線在每個質數 $p$ 模 $p$ 後數點數,可以拼出一個解析物件——L 函數 $L(E,s)$。BSD 猜想說:**這個純解析的函數在 $s=1$ 處消失的階數,恰好等於代數上定義的秩 $r$**。粗略地說:局部(mod $p$)資訊的統計行為,決定了全域有理解的多寡。

**正式版(秩部分)**:
$$\operatorname{ord}_{s=1} L(E,s) = \operatorname{rank}\, E(\mathbb{Q}).$$

**正式版(精細公式 / BSD formula)**:首項係數應滿足
$$\lim_{s\to 1}\frac{L(E,s)}{(s-1)^r} = \frac{\#\Sha(E)\cdot \Omega_E \cdot \mathrm{Reg}(E) \cdot \prod_p c_p}{(\# E(\mathbb{Q})_{\mathrm{tors}})^2},$$
其中 $\Sha(E)$ 是 Tate–Shafarevich 群(其有限性本身也是未解決的猜想)、$\mathrm{Reg}$ 是 regulator、$\Omega_E$ 是實週期、$c_p$ 是 Tamagawa 數。

## 背景與重要性

1960 年代 Birch 與 Swinnerton-Dyer 在劍橋用 EDSAC 電腦計算大量橢圓曲線的 $\prod_{p\le X} N_p/p$,觀察到其增長速率與秩相關,由此提出猜想。它是「L 函數的特殊值編碼算術資訊」這一整個綱領(包括 Bloch–Kato 猜想、Beilinson 猜想)的原型。橢圓曲線本身是密碼學(ECC)與 Fermat 大定理證明的核心物件;BSD 若成立,還會給出判定同餘數問題(congruent number problem)的有效演算法(經由 Tunnell 定理)。

## 目前狀態

截至 2026 年中:

- **解析秩 0 與 1**:由 Gross–Zagier(1986)+ Kolyvagin(1988–90),若 $\operatorname{ord}_{s=1}L(E,s) \le 1$,則秩部分成立且 $\Sha$ 有限。這是無條件的定理。
- **精細公式的 $p$-部分**:透過岩澤理論(Iwasawa theory),秩 0 情形(Skinner–Urban 主猜想)與秩 1 情形(Jetchev–Skinner–Wan 等)對大多數質數 $p$ 已證得 BSD 公式的 $p$-部分;結合 2-部分與 3-部分的專門工作,已知**無窮多條橢圓曲線(含非 CM 曲線)滿足完整的 BSD 公式**。
- **CM 曲線**:Burungale–Flach(2024)對一大類具複乘(CM)的曲線證明了完整 BSD(秩 $\le 1$ 時包括 $\Sha$ 有限性與精細公式,含 $p=2$)。
- **統計層面**:Bhargava–Shankar 等的平均秩工作 + Alexander Smith 的 $2^\infty$-Selmer 群結果,顯示「正比例的橢圓曲線滿足 BSD 秩部分」。
- **卡在哪裡**:解析秩 $\ge 2$ 時,完全沒有已知方法把 L 函數的高階零點與有理點聯繫起來(Gross–Zagier 只造得出一個 Heegner 點);$\Sha$ 的有限性在秩 $\ge 2$ 時一例都證不出來。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1922 | $E(\mathbb{Q})$ 有限生成 | Mordell |
| 1965 | 基於 EDSAC 計算提出猜想 | Birch, Swinnerton-Dyer |
| 1977 | CM 曲線:$L(E,1)\ne 0 \Rightarrow$ 秩 0 | Coates, Wiles |
| 1986 | Gross–Zagier 公式:$L'(E,1)$ 與 Heegner 點高度 | Gross, Zagier |
| 1988–90 | Euler 系統:解析秩 $\le 1$ 情形成立 | Kolyvagin(CM 情形 Rubin) |
| 1995–2001 | 模性定理 ⇒ $L(E,s)$ 對所有 $E/\mathbb{Q}$ 有解析延拓 | Wiles; Breuil–Conrad–Diamond–Taylor |
| 2014 | 岩澤主猜想(ordinary 情形)⇒ 秩 0 的 $p$-部分公式 | Skinner, Urban |
| 2017 | 秩 1 的 $p$-部分 BSD 公式(ordinary $p$) | Jetchev, Skinner, Wan([arXiv:1512.06894](https://arxiv.org/abs/1512.06894)) |
| 2017–24 | $2^\infty$-Selmer 群分布 ⇒ Goldfeld 猜想方向的重大進展 | A. Smith([arXiv:1702.02325](https://arxiv.org/abs/1702.02325)) |
| 2019–23 | 二次扭的 2-部分 BSD 公式;$p$-converse 定理 | C. Li 等([綜述](https://www.math.columbia.edu/~chaoli/BSD2.pdf));Burungale, Skinner, Tian |
| 2024 | CM 橢圓曲線的完整 BSD(一大類,含 $p=2$) | Burungale, Flach(Camb. J. Math. 12.2,[PDF](https://par.nsf.gov/servlets/purl/10609724)) |
| 2025 | Eisenstein 質數處的 Mazur 主猜想(Math. Ann.) | Castella, Grossi, Skinner |
| 2025 | Mazur–Tate 精細 BSD 型猜想的新進展(預印本) | [arXiv:2511.07203](https://arxiv.org/abs/2511.07203) |

## 主要研究方法

- **Heegner 點 + Euler 系統**(Gross–Zagier / Kolyvagin 路線):對秩 $\le 1$ 極其成功,但本質上只能產生一個點,對秩 $\ge 2$ 失效。
- **岩澤理論(Iwasawa theory)**:證明 $p$-adic L 函數與 Selmer 群的主猜想(main conjecture),把 BSD 公式一個質數一個質數地攻下。目前最有系統性產出的路線(Skinner–Urban、Wan、Castella–Grossi–Skinner 等),難點在小質數、supersingular 質數與 Eisenstein 質數等退化情形——這正是近年逐一被清除的戰場。
- **算術統計**(Bhargava 學派 + Smith):不解決單一曲線,而證明「幾乎所有 / 正比例」曲線滿足 BSD。優點是無條件、覆蓋面大;缺點是對任何指定曲線無效。
- **$p$-adic 方法與 $p$-converse**:從 Selmer 群的秩反推解析秩(Skinner、Burungale–Tian),補全雙向蘊涵。
- **秩 $\ge 2$**:目前無可行路線;被普遍視為需要全新想法(如高階導數的幾何詮釋)。

## AI 可以怎麼幫忙

- **形式化現況**:Lean 4 mathlib 已有 Weierstrass 曲線與其群律的完整形式化(Angdinata–Xu,[ITP 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol268-itp2023/LIPIcs.ITP.2023.6/LIPIcs.ITP.2023.6.pdf));Angdinata 正推進 Mordell–Weil 定理與 BSD 陳述本身的形式化。Google DeepMind 的 [formal-conjectures](https://github.com/google-deepmind/formal-conjectures/issues/1414) 專案已把 BSD 列為待形式化陳述。距離「形式化 Gross–Zagier」仍非常遙遠(需要模曲線、高度理論等大量前置)。
- **資料庫**:[LMFDB](https://www.lmfdb.org/) 收錄數百萬條橢圓曲線及其秩、L 函數、BSD 不變量的數值驗證,是機器學習實驗的現成資料集;已有用 ML 從係數預測秩的研究(如 He–Lee–Oliver 的 murmurations 現象,2023 起,正是從 LMFDB 資料中被發現的)。
- **本 repo 可做的事**:(1) 追蹤岩澤理論路線的論文並維護「哪些 $(E,p)$ 組合的 $p$-部分已證」的清單;(2) 用 LMFDB API 重現 murmurations 圖並整理成教學筆記;(3) 把 BSD 陳述所需的定義依賴圖(L 函數、Selmer 群、$\Sha$)整理成 mathlib 缺口清單。

## 關鍵文獻與資源

- Clay 官方問題描述(Wiles 撰寫):https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/
- Gross–Zagier, *Heegner points and derivatives of L-series*, Invent. Math. 84 (1986)
- Skinner–Urban, *The Iwasawa main conjectures for GL(2)*, Invent. Math. 195 (2014)
- Burungale–Flach, *The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication*, Camb. J. Math. 12.2 (2024) — [公開 PDF](https://par.nsf.gov/servlets/purl/10609724)
- Chao Li 的 BSD 2-部分綜述:https://www.math.columbia.edu/~chaoli/BSD2.pdf
- LMFDB 橢圓曲線資料庫:https://www.lmfdb.org/EllipticCurve/Q/
