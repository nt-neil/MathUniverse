# Hodge 猜想(Hodge Conjecture)

> 在光滑複射影簇上,拓撲/分析手段找到的「看起來像代數的」上同調類,是否真的都來自代數子簇?

| | |
|---|---|
| **領域** | 代數幾何 Algebraic Geometry(Hodge 理論、算術幾何交界) |
| **提出** | 1950 年,W. V. D. Hodge(ICM 演講);現代形式經 Grothendieck 等修正 |
| **狀態** | 未解決(低維與特殊簇類有部分結果) |
| **懸賞** | 千禧年大獎 100 萬美元(Clay Mathematics Institute) |

## 問題陳述

**直觀版**:一個光滑複射影簇 $X$ 的拓撲(奇異上同調)可以用微分形式分解成不同「型」的部分(Hodge 分解)。代數子簇的基本類永遠落在特定的型 $(p,p)$ 且是有理係數類。Hodge 猜想問的是**逆命題**:每一個落在對的位置的有理上同調類,是否都能寫成代數子簇類的有理線性組合?換句話說:線性代數與微分形式層次的「必要條件」,是否已經是「充分條件」?這是「拓撲能否看見代數」的核心問題。

**正式版**:設 $X$ 為光滑複射影簇,定義 Hodge 類
$$\mathrm{Hdg}^{p}(X) = H^{2p}(X,\mathbb{Q}) \cap H^{p,p}(X).$$
猜想:每個 $\alpha \in \mathrm{Hdg}^p(X)$ 都是代數餘圈類(algebraic cycle classes)$[Z_i]$ 的 $\mathbb{Q}$-線性組合,即餘圈類映射
$$CH^p(X)\otimes\mathbb{Q} \longrightarrow \mathrm{Hdg}^p(X)$$
是滿射。注意:必須用 $\mathbb{Q}$ 係數——整係數版本已被 Atiyah–Hirzebruch(1961)否證。

## 背景與重要性

Hodge 在 1930–40 年代發展了調和形式理論(Hodge theory),1950 年 ICM 演講中提出此問題。它位於代數幾何的心臟:代數餘圈(algebraic cycles)是我們最不理解的物件,而 Hodge 猜想是「用可計算的線性資料刻劃它們」的最大膽宣言。它與 Grothendieck 的 motives 理論、Tate 猜想(有限域上的算術類比)、Bloch–Beilinson 濾過等深層結構互為表裡;許多算術幾何定理(如 Mordell 猜想的某些證明策略)在「假設 Hodge 猜想」下會有概念性簡化。反方向的證據也重要:Voisin(2002)證明 Kähler 流形上自然的推廣形式是錯的,顯示猜想若成立,理由必須是射影代數簇特有的。

## 目前狀態

截至 2026 年中:

- **普遍成立的部分**:$p=1$ 情形即 Lefschetz (1,1) 定理(1924),完全解決;由 hard Lefschetz 對偶,$\dim X \le 3$ 的所有情形成立。$H^{2\dim X -2}$(除數的對偶情形)也成立。
- **Abelian varieties**:歷來的試金石。Mattuck、Tate、Moonen–Zarhin 處理了大量情形,剩下的核心障礙是 **Weil 類**(Weil classes,Weil 1977 年指出的非平凡 Hodge 類)。Markman 以 hyperkähler 幾何(generalized Kummer 簇上的 hyperholomorphic sheaves)證明了 Weil 型 abelian fourfolds 在判別式 1 情形的 Weil 類代數性,並在後續工作([arXiv:2502.03415](https://arxiv.org/abs/2502.03415),2025,預印本)以 secant sheaves 方法推進到更一般的 Weil 型 $2n$-folds;結合 Moonen–Zarhin 的分類,**四維 abelian varieties 的 Hodge 猜想已(在預印本層面)完全落定**。這是數十年來最實質的進展。
- **卡在哪裡**:沒有任何構造代數餘圈的一般方法。已知的證明都是「在特殊幾何中湊出餘圈」;Cattani–Deligne–Kaplan(1995)證明 Hodge 軌跡(Hodge loci)是代數的,提供了間接證據,但從「軌跡代數」到「類代數」之間沒有橋。多數專家對猜想真偽並無共識,Voisin 等人公開表示過懷疑態度。
- **注意**:網路上流傳多篇宣稱「證明 Hodge 猜想」的預印本(preprints.org、viXra 等),均未通過同行審查,不應視為進展。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1924 | Lefschetz (1,1) 定理:$p=1$ 情形成立 | Lefschetz |
| 1950 | ICM 演講正式提出猜想 | Hodge |
| 1961 | 整係數版本的反例 | Atiyah, Hirzebruch |
| 1969 | 「一般 Hodge 猜想」的修正陳述 | Grothendieck |
| 1977 | 指出 Weil 型 abelian varieties 上的疑難 Hodge 類 | Weil |
| 1995 | Hodge loci 是代數子集(重要間接證據) | Cattani, Deligne, Kaplan |
| 1999 | Abelian fourfolds 例外 Hodge 類的分類 | Moonen, Zarhin |
| 2002 | Kähler 版本推廣不成立 | Voisin |
| 2022–25 | Weil 型 abelian fourfolds 的 Weil 類是代數的;推廣至 $2n$-folds(預印本) | Markman([arXiv:2502.03415](https://arxiv.org/abs/2502.03415)) |
| 2025 | 判別式 1 的 Weil fourfolds 經奇異 OG6 簇的另一條證明路線(預印本) | Floccari, Fu([arXiv:2504.13607](https://arxiv.org/abs/2504.13607)) |
| 2026 | Weil 型 abelian sixfolds 方向的後續工作(預印本) | [arXiv:2603.20268](https://arxiv.org/abs/2603.20268) |

## 主要研究方法

- **特殊簇類逐一攻克**:abelian varieties、hyperkähler 簇、K3 曲面的冪等。優點是可用額外對稱性(CM、monodromy)造餘圈;Markman 路線的成功顯示 hyperkähler 幾何是新的餘圈製造機。缺點:方法高度依賴特殊結構,不可能推廣到一般簇。
- **Hodge loci 與變動理論(variational approach)**:Cattani–Deligne–Kaplan 之後,研究 Hodge 類在族中如何變動(近年與 o-minimality、Bakker–Klingler–Tsimerman 的工作連結)。提供結構性理解,但尚未產生新的代數性結果。
- **Motives 與絕對 Hodge 類**:Deligne 證明 abelian varieties 的 Hodge 類都是「絕對 Hodge」(absolute Hodge),是介於「Hodge」與「代數」之間的中繼站。把「絕對 Hodge ⇒ 代數」補上就解決 abelian variety 情形,但這一步同樣無人知道怎麼做。
- **尋找反例**:對 $\dim \ge 4$ 的一般簇構造「無法用已知餘圈解釋」的 Hodge 類。目前沒有嚴肅的反例候選。

## AI 可以怎麼幫忙

- **形式化現況**:距離可形式化陳述仍遠——Lean 4 mathlib 尚無完整的複代數幾何 Hodge 理論(奇異上同調、de Rham 上同調已具雛形,但 Hodge 分解、代數餘圈類映射尚未形式化)。相較 BSD(陳述已接近可形式化),Hodge 猜想連「正確陳述所需的定義」都是 mathlib 的長期缺口,這本身是值得追蹤的指標。
- **機器學習嘗試**:尚無已知的 ML 直接攻擊;可行的近端方向是對特定族(如超曲面)的 Hodge 數與餘圈資料做模式探索,類似橢圓曲線 murmurations 的發現路徑。
- **本 repo 可做的事**:(1) 維護「已知成立的簇類清單」(依維度、簇類、證明方法分類),並持續更新 Markman 路線的預印本審查狀態;(2) 整理 Weil 類的具體矩陣表述,做成可計算的範例筆記;(3) 建立「宣稱證明」的闢謠清單(記錄常見錯誤模式),減少讀者被未審查預印本誤導。

## 關鍵文獻與資源

- Clay 官方問題描述(Deligne 撰寫):https://www.claymath.org/millennium/hodge-conjecture/
- Voisin, *Hodge Theory and Complex Algebraic Geometry* I & II(標準教材)
- Voisin, *Some aspects of the Hodge conjecture*, Jpn. J. Math. 2 (2007)(最佳綜述之一)
- Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds* — [arXiv:2502.03415](https://arxiv.org/abs/2502.03415)(預印本)
- Floccari–Fu, *The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties* — [arXiv:2504.13607](https://arxiv.org/abs/2504.13607)(預印本)
- Schnell 的課程講義(abelian varieties 的 Hodge 猜想):https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture28.pdf
