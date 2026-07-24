# 黎曼猜想(Riemann Hypothesis)

> 黎曼 zeta 函數的所有非平凡零點,實部是否都等於 1/2?這決定了質數分布的「誤差項」能有多小。

| | |
|---|---|
| **領域** | 數論 Number Theory / 解析數論 Analytic Number Theory |
| **提出** | 1859 年,Bernhard Riemann |
| **狀態** | 未解決 |
| **懸賞** | 千禧年大獎(Clay Mathematics Institute)100 萬美元;亦為希爾伯特第 8 問題的一部分 |

## 問題陳述

**直觀版**:質數在數線上的分布看似雜亂,但整體有規律(質數定理告訴我們 $x$ 以下約有 $x/\ln x$ 個質數)。黎曼猜想斷言這個規律的「誤差」小到不能再小——質數的分布與「隨機」的偏差被最強地控制住。這一切被編碼在一個複變函數的零點位置上。

**正式版**:黎曼 zeta 函數定義為
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \quad (\mathrm{Re}(s) > 1)$$
並可解析延拓(analytic continuation)到整個複平面($s=1$ 為極點)。已知 $\zeta$ 在負偶數 $-2, -4, \dots$ 有「平凡零點」。黎曼猜想:**所有非平凡零點 $\rho$ 都滿足 $\mathrm{Re}(\rho) = \tfrac{1}{2}$**(即落在「臨界線」critical line 上)。

等價形式之一(質數計數):對所有 $x \ge 2$,
$$|\pi(x) - \mathrm{Li}(x)| = O(\sqrt{x}\,\log x)$$

## 背景與重要性

Riemann 在 1859 年僅 8 頁的論文《論小於給定數值的質數個數》中提出此猜想,原意是研究質數計數函數 $\pi(x)$。1896 年 Hadamard 與 de la Vallée Poussin 利用「$\mathrm{Re}(s)=1$ 上無零點」證明了質數定理——零點位置與質數分布的深刻聯繫從此確立。

重要性:數論中有成百上千條定理是以「若黎曼猜想(或其推廣 GRH)成立」為前提證出的,包括質數分布、二次型、密碼學相關的演算法分析(如確定性質數判定的界)。此外,零點統計與隨機矩陣理論(random matrix theory)、量子混沌的驚人吻合,暗示它連結著遠超數論的結構。

## 目前狀態

截至 2026 年 7 月:未解決,也沒有被學界認可的接近完整證明的路線。已知:

- 無窮多個零點在臨界線上(Hardy 1914),且至少約 5/12(≈41.7%)的零點在線上。
- 數值驗證:虛部 $|\mathrm{Im}(\rho)| \le 3\times 10^{12}$ 範圍內的所有零點(超過 $10^{13}$ 個)都在臨界線上(Platt–Trudgian 2021)。
- 最新突破方向是「零點密度估計」(zero density estimates):即使不能證明零點都在線上,也要證明偏離臨界線的零點極其稀少。2024 年 Guth–Maynard 在此打破了 80 多年的紀錄(見下表)。

卡在哪裡:現有解析工具(如 Dirichlet 多項式的大值估計)本質上只能「限制」壞零點的數量,無法排除單一壞零點;缺少一個能解釋「為什麼實部必須是 1/2」的結構性機制(Hilbert–Pólya 式的自伴算子至今沒找到)。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1859 | 提出猜想 | B. Riemann |
| 1896 | 質數定理(零點不在 $\mathrm{Re}(s)=1$ 上) | Hadamard;de la Vallée Poussin |
| 1914 | 臨界線上有無窮多零點 | G. H. Hardy |
| 1942 | 臨界線上零點佔正比例 | A. Selberg |
| 1974 / 1989 | 比例提高到 1/3、再到 2/5 | N. Levinson;J. B. Conrey |
| 1940 | Ingham 零點密度估計(此後 80 餘年無人打破) | A. E. Ingham |
| 2021 | 數值驗證至 $|\mathrm{Im}| \le 3\times 10^{12}$([arXiv:2004.09765](https://arxiv.org/abs/2004.09765)) | D. Platt, T. Trudgian |
| 2024 | **Guth–Maynard**:Dirichlet 多項式新的大值估計,得零點密度 $N(\sigma,T) \le T^{30(1-\sigma)/13 + o(1)}$,首次突破 Ingham 1940 的界;並推出短區間($x^{17/30}$)質數漸近公式([arXiv:2405.20552](https://arxiv.org/abs/2405.20552),已刊於 Annals of Mathematics,[Oxford ORA 紀錄](https://ora.ox.ac.uk/objects/uuid:ad11b8bf-ad2b-4ebf-a627-647f023c378f);Tao 評為「顯著突破」,[Mathstodon](https://mathstodon.xyz/@tao/112557248794707738)) | L. Guth, J. Maynard |
| 2025 | zeta 與 L-函數理論(含黎曼猜想的正式陳述)完成 Lean/Mathlib 形式化([arXiv:2503.00959](https://arxiv.org/abs/2503.00959),刊於 [Annals of Formalized Mathematics](https://afm.episciences.org/15954)) | D. Loeffler, M. Stoll |

## 主要研究方法

- **解析方法(主流)**:零點密度估計、zeta 函數的矩(moments)、Dirichlet 多項式大值估計。優點:持續產出可證的部分結果(如 Guth–Maynard);缺點:普遍認為此路線本身到不了 RH 全解。
- **隨機矩陣理論**:Montgomery 對關聯猜想與 GUE 統計吻合(Odlyzko 數值驗證),Keating–Snaith 預測矩公式。提供極強的啟發與猜想,但目前無法回推證明。
- **Hilbert–Pólya 路線**:尋找一個自伴算子,其特徵值對應零點虛部,自伴性自動給出實部 1/2。相關嘗試包括 Connes 的非交換幾何框架、Berry–Keating 的量子混沌模型。結構優美但尚無落地。
- **等價判準**:Robin 判準($\sigma(n) < e^\gamma n \ln\ln n$ 對 $n>5040$)、Nyman–Beurling 判準等,把 RH 轉成初等或泛函分析語言;至今未因此變得更容易。

## AI 可以怎麼幫忙

- **形式化**:黎曼猜想的**陳述**已在 Lean 4 Mathlib 中正式定義(`RiemannHypothesis`,見 Loeffler–Stoll 2025,上表)。質數定理已由 PrimeNumberTheorem+ 專案(Kontorovich、Tao 等)在 Lean 中形式化。注意:網路上偶有「機器驗證的 RH 完整證明」之類文件流傳,均未被學界接受,應視為無效聲明。
- **機器學習輔助**:目前沒有已被認可的 ML 直接貢獻於 RH 的案例;可行方向是用 ML 探索零點統計、L-函數資料庫(LMFDB)中的模式。
- **本 repo 可做的事**:
  - 整理 RH 的等價陳述清單(Robin、Nyman–Beurling、Li 判準…)並逐一給出可計算的檢驗程式;
  - 對 Robin 判準做小範圍數值實驗(教學價值高、不會撞出新結果但能建立工具鏈);
  - 追蹤 Guth–Maynard 之後零點密度文獻的後續改進(2024–2026 已有多篇跟進的 arXiv 預印本);
  - 在 Lean 中練習陳述 RH 的等價形式,並與 Mathlib 的 `RiemannHypothesis` 定義對接。

## 關鍵文獻與資源

- Clay Mathematics Institute 官方問題頁:https://www.claymath.org/millennium/riemann-hypothesis/
- Guth & Maynard, *New large value estimates for Dirichlet polynomials*(2024):https://arxiv.org/abs/2405.20552
- Platt & Trudgian, *The Riemann hypothesis is true up to* $3\cdot 10^{12}$(2021):https://arxiv.org/abs/2004.09765
- Loeffler & Stoll, *Formalizing zeta and L-functions in Lean*(2025):https://arxiv.org/abs/2503.00959
- Bombieri 為 Clay 撰寫的官方問題描述(綜述);Conrey, *The Riemann Hypothesis*(AMS Notices 2003,可讀性高的綜述)
- LMFDB(L-函數與模形式資料庫):https://www.lmfdb.org/
