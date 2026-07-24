# Navier–Stokes 方程存在性與光滑性(Navier–Stokes Existence and Smoothness)

> 描述流體運動的基本方程,其三維解是否永遠保持光滑,還是會在有限時間內「爆破」?

| | |
|---|---|
| **領域** | 偏微分方程 Partial Differential Equations(MSC 35Q30, 76D05) |
| **提出** | 方程源於 Navier(1822)與 Stokes(1845);千禧年問題由 C. Fefferman 於 2000 年正式陳述 |
| **狀態** | 未解決 |
| **懸賞** | 千禧年大獎 100 萬美元(Clay Mathematics Institute, 2000) |

## 問題陳述

**直觀版**:把一杯水攪動後放著,描述它每一點流速的方程就是 Navier–Stokes 方程。問題是:從任何平滑的初始流場出發,流速會不會在某個瞬間、某個點變成無限大(形成奇點 singularity)?如果永遠不會,方程就「行為良好」;如果會,表示這個被工程界天天使用的方程在數學上可能自我崩壞。

**正式版**:考慮 $\mathbb{R}^3$ 上不可壓縮 Navier–Stokes 方程

$$\partial_t u + (u \cdot \nabla)u = -\nabla p + \nu \Delta u, \qquad \nabla \cdot u = 0,$$

其中 $u(x,t)$ 為速度場、$p$ 為壓力、$\nu > 0$ 為黏滯係數。Clay 官方題目(Fefferman 陳述)要求證明以下二者之一:

1. **存在性與光滑性**:對任意光滑、能量有限(或週期性)的初始資料 $u_0$,存在全域光滑解;或
2. **爆破(blow-up)**:存在光滑初始資料,其解在有限時間 $T^* < \infty$ 內失去光滑性。

## 背景與重要性

Navier–Stokes 方程是流體力學的基礎,支撐天氣預報、航太設計、血流模擬。Leray(1934)證明了弱解(weak solutions)全域存在,但弱解可能不唯一、不光滑;二維情形已於 1960 年代由 Ladyzhenskaya 等人完全解決(全域光滑)。三維的困難在於:方程的自然守恆量(能量)相對於方程的尺度變換是**超臨界(supercritical)**的——已知的先驗估計不足以控制小尺度行為。這個問題因此成為超臨界 PDE 正則性理論的試金石,其解決預期會帶動整個非線性 PDE、湍流理論的方法革新。

## 目前狀態

截至 2026 年 7 月:未解決。學界目前的主流猜測傾向**爆破存在**(即答案是否定方向),主要基於:(1) Tao 對「平均化」Navier–Stokes 方程構造出有限時間爆破,顯示僅靠能量估計與一般結構不可能證明正則性;(2) 相關的 3D Euler 方程(無黏性)已有愈來越完整的爆破結果(Elgindi;Chen–Hou 的計算機輔助證明);(3) 2025 年起,以神經網路系統性尋找**不穩定自相似奇點(unstable self-similar singularities)**的計畫取得高精度候選解,被視為通往計算機輔助爆破證明的可行路徑。但 Navier–Stokes 本身(有黏性、無邊界)的爆破仍未被證明。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1934 | 弱解全域存在(Leray–Hopf 弱解) | J. Leray |
| 1960s | 二維情形完全解決(全域光滑) | O. Ladyzhenskaya 等 |
| 1982 | 部分正則性:適當弱解的奇點集一維拋物 Hausdorff 測度為零 | Caffarelli, Kohn, Nirenberg |
| 2014 | Luo–Hou 數值發現 3D Euler 邊界附近的自相似爆破情境 | G. Luo, T. Hou |
| 2016 | 平均化 Navier–Stokes 方程的有限時間爆破;提出「以流體自建計算機」的爆破綱領。[arXiv:1402.0290](https://arxiv.org/abs/1402.0290) | T. Tao |
| 2019 | Leray 弱解在能量空間中不唯一(convex integration 方法,Annals of Math.) | T. Buckmaster, V. Vicol |
| 2021 | 3D Euler 在 $C^{1,\alpha}$ 速度場類中的有限時間爆破 | T. Elgindi |
| 2022–2023 | 帶邊界 3D 軸對稱 Euler 的近自相似爆破之計算機輔助證明。[arXiv:2210.07191](https://arxiv.org/abs/2210.07191) | J. Chen, T. Hou |
| 2024 | 廣義軸對稱 Navier–Stokes(分數次耗散等推廣族)的近自相似爆破研究。[arXiv:2405.10916](https://arxiv.org/abs/2405.10916)(預印本) | T. Hou 等 |
| 2025 | **「Discovery of Unstable Singularities」**:DeepMind 與 NYU、Stanford、Brown 等合作,用 PINN 類神經網路以接近機器精度系統性找出 IPM、Boussinesq、帶邊界 3D Euler 等方程的多族不穩定自相似奇點,發現不穩定度與尺度參數 $\lambda$ 的經驗規律;被視為通往計算機輔助證明的重要一步。[arXiv:2509.14185](https://arxiv.org/abs/2509.14185)(預印本);報導見 [Quanta Magazine](https://www.quantamagazine.org/using-ai-mathematicians-find-hidden-glitches-in-fluid-equations-20260109/) | Y. Wang, T. Buckmaster, J. Gómez-Serrano, C.-Y. Lai, P. Kohli 等(Google DeepMind 合作團隊) |
| 2025 | 後續工作:以神經網路把不穩定奇點的尖銳梯度解析到機器精度,強化候選解作為嚴格證明輸入的可用性。[arXiv:2511.22819](https://arxiv.org/abs/2511.22819)(預印本) | 同系列團隊 |

## 主要研究方法

- **先驗估計與部分正則性**:延續 Caffarelli–Kohn–Nirenberg 路線,縮小可能奇點集。優:無條件的正面結果;劣:超臨界性使其距全域正則仍遠。
- **自相似爆破構造 + 計算機輔助證明**:先數值找出(近)自相似奇點剖面,再用區間算術嚴格驗證(Chen–Hou 對 Euler 的路線)。優:對 Euler 已成功;劣:Navier–Stokes 的黏性項排除了最簡單的自相似情境(Nečas 等的排除定理),必須使用不穩定或非自相似機制,而不穩定奇點對數值方法極端敏感——這正是 2025 年神經網路方法的切入點。
- **Convex integration**:構造粗糙弱解、證明不唯一性(Buckmaster–Vicol)。優:徹底改變了弱解圖景;劣:產生的解非物理、無法直接觸及光滑解的爆破。
- **Tao 的綱領**:在流體方程中嵌入「自我複製的計算機制」,讓流體自己觸發尺度愈來愈小的爆破級聯。概念上有力,但完整實作極為困難。

## AI 可以怎麼幫忙

- **形式化現況**:Navier–Stokes 的基礎(如 Leray 理論)尚無完整 Lean/Coq 形式化;Lean 的 mathlib 對 PDE 的支援仍在建設期。短期內形式化不是此題主戰場;計算機輔助部分靠的是**區間算術驗證**(interval arithmetic),而非證明助理。
- **ML 輔助探索(已實證有效)**:2025 年 DeepMind 合作團隊用高精度 PINN(物理資訊神經網路)+ 二階最佳化(Gauss–Newton)找不穩定自相似奇點([arXiv:2509.14185](https://arxiv.org/abs/2509.14185)),是「AI 找候選解 → 人類/區間算術完成嚴格證明」流水線的代表案例。此路線目前對帶邊界 Euler、Boussinesq、IPM 有效;對完整 Navier–Stokes 仍是開放挑戰。
- **本 repo 可做的事**:
  - 重現小規模 PINN 求自相似剖面的實驗(先做 1D 模型方程如 Burgers、CCF 模型,驗證方法論)。
  - 整理「已知爆破結果一覽表」:哪個方程、哪種資料類、穩定/不穩定、是否有嚴格證明——目前文獻分散,系統性整理有真實價值。
  - 追蹤 2509.14185 系列的後續(是否有人把候選奇點轉成嚴格的計算機輔助證明),維護進展時間線。

## 關鍵文獻與資源

- Clay 官方問題陳述(C. Fefferman):https://www.claymath.org/millennium/navier-stokes-equation/
- T. Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation":https://arxiv.org/abs/1402.0290
- J. Chen, T. Hou, 帶邊界軸對稱 Euler 爆破的計算機輔助證明:https://arxiv.org/abs/2210.07191
- DeepMind 合作團隊, "Discovery of Unstable Singularities"(2025, 預印本):https://arxiv.org/abs/2509.14185;官方部落格:https://deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/
- Quanta Magazine 報導(2026-01):https://www.quantamagazine.org/using-ai-mathematicians-find-hidden-glitches-in-fluid-equations-20260109/
- T. Tao 部落格中關於超臨界性與爆破綱領的多篇文章:https://terrytao.wordpress.com/
