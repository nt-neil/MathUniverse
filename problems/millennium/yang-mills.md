# Yang–Mills 存在性與質量間隙(Yang–Mills Existence and Mass Gap)

> 為描述強交互作用的量子規範場論建立嚴格的數學基礎,並證明其激發態能量有一個嚴格為正的下界(質量間隙)。

| | |
|---|---|
| **領域** | 數學物理 Mathematical Physics / 構造性量子場論 Constructive QFT(MSC 81T13, 81T08) |
| **提出** | Yang–Mills 理論源於楊振寧與 Mills(1954);千禧年問題由 A. Jaffe 與 E. Witten 於 2000 年正式陳述 |
| **狀態** | 未解決 |
| **懸賞** | 千禧年大獎 100 萬美元(Clay Mathematics Institute, 2000) |

## 問題陳述

**直觀版**:物理學家用 Yang–Mills 規範場論(量子色動力學的骨架)成功預測強交互作用的實驗結果,但這套理論至今只有物理層次的操作規則,沒有數學上嚴格的定義。此外有一個奇特現象:雖然古典 Yang–Mills 場的波是無質量的(像光),量子化之後最輕的粒子(膠球 glueball)卻有正質量——低能激發「憑空」獲得質量。問題要求:(1) 嚴格定義這個理論;(2) 證明這個質量確實存在。

**正式版**(Jaffe–Witten 陳述):對任意緊緻單李群 $G$(如 $SU(3)$),證明 $\mathbb{R}^4$ 上存在滿足 Wightman 公理(或等價的 Osterwalder–Schrader 公理)的非平凡量子 Yang–Mills 理論,且其 Hamiltonian $H$ 的譜滿足**質量間隙**:

$$\mathrm{spec}(H) \subseteq \{0\} \cup [\Delta, \infty), \quad \Delta > 0,$$

即真空之上的最低激發能量嚴格為正。

## 背景與重要性

Yang–Mills 理論是粒子物理標準模型的數學骨架;$SU(3)$ 情形即量子色動力學(QCD),描述夸克與膠子。質量間隙與**色禁閉(confinement)**、強交互作用的短程性直接相關——物理上由實驗與格點數值計算(lattice QCD)強烈支持(SU(3) 膠球質量約 1.5 GeV),但都不是數學證明。此問題的本質困難是:四維的量子場論從未被嚴格構造過任何有交互作用的例子(構造性場論在 2、3 維成功,4 維始終卡關)。解決它意味著為量子場論這整個物理框架第一次建立四維的嚴格數學地基。

## 目前狀態

截至 2026 年 7 月:未解決,且被普遍認為是七個千禧年問題中「連問題本身都需要先建立定義」的一題。已知:

- **低維情形**:2 維 Yang–Mills 可精確求解且嚴格構造完成;3 維有 Balaban 等人的紫外穩定性分析,以及近年隨機量子化(stochastic quantisation)路線(Chandra–Chevyrev–Hairer–Shen 對 2D/3D Yang–Mills 的 Langevin 動力學構造,2020–2022)的進展,但 3D 的完整構造與質量間隙也尚未完成。
- **4 維**:Balaban(1980s)與 Magnen–Rivasseau–Sénéor 對有限體積的紫外穩定性有部分結果,但連續極限、無限體積極限、質量間隙皆未達成。
- **格點路線的新動能**:Chatterjee 學派把格點 Yang–Mills 變成機率論的活躍領域——規範—弦對偶(gauge-string duality)、主迴圈方程(master loop equations)、Wilson 迴圈期望的精確漸近。Chatterjee 明確指出:質量間隙的核心步驟等價於證明大 $\beta$(弱耦合)下 Wilson 迴圈關聯的指數衰減,目前仍未解決。
- 近年出現多篇**宣稱完整解決**的預印本(例如 [arXiv:2506.00284](https://arxiv.org/abs/2506.00284) 宣稱構造 SU(3) 情形並證明質量間隙),均未經同行評審確認,學界未接受;引用時應以「未驗證聲明」看待。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1954 | 非阿貝爾規範場論提出 | 楊振寧, R. Mills |
| 1974 | 格點規範理論(lattice gauge theory),給出非微擾定義的候選 | K. Wilson |
| 1973–1979 | 漸近自由;2、3 維構造性場論成熟($P(\phi)_2$、$\phi^4_3$ 等) | Gross, Wilczek, Politzer;Glimm, Jaffe 等 |
| 1980s | 4 維格點 Yang–Mills 的紫外穩定性(有限體積) | T. Balaban;Magnen, Rivasseau, Sénéor |
| 2000 | 千禧年問題正式陳述 | A. Jaffe, E. Witten |
| 2015 | 格點規範理論的規範—弦對偶嚴格定理(強耦合區) | S. Chatterjee |
| 2016–2019 | 主迴圈方程(master loop equations)的嚴格推導與大 $N$ 分析 | Chatterjee, Jafarov |
| 2020–2022 | 2D/3D Yang–Mills 的隨機量子化(Langevin 動力學)構造。[arXiv:2006.04987](https://arxiv.org/abs/2006.04987) 等 | Chandra, Chevyrev, Hairer, Shen |
| 2023 | 有限 $N$ 主迴圈方程的新推導(幾何/動力學方法)。[arXiv:2309.07399](https://arxiv.org/abs/2309.07399)(預印本) | Shen, Smith, Zhu 等 |
| 2024 | 3D 格點 Yang–Mills 的新進展(與 Sky Cao 合作系列工作);Chatterjee 的公開綜述講義持續更新問題地圖。[講義](https://souravchatterjee.su.domains/beam-3dym-msri-trans.pdf) | S. Chatterjee, S. Cao |
| 2025 | Harvard 千禧年問題系列講座(2025-10-15),Chatterjee 主講,總結近十年令此題「重獲動能」的機率論進展。[活動頁](https://www.math.harvard.edu/event/millennium-prize-problems-lecture-sourav-chatterjee-yang-mills-existence-and-mass-gap) | S. Chatterjee / Harvard |

## 主要研究方法

- **構造性場論 / 重整化群(RG)**:沿 Balaban 路線做多尺度分析,嚴格控制連續極限。優:是「正統」路徑,低維已成功;劣:4 維的技術複雜度極高,數十年無人完成全程。
- **格點機率論(Chatterjee 學派)**:把格點 Yang–Mills 當作機率模型,研究 Wilson 迴圈、主迴圈方程、與弦論展開的對偶。優:定理紮實、工具(機率、隨機幾何)現代且活躍;劣:目前成果集中在強耦合區,質量間隙需要的弱耦合區指數衰減仍是關鍵未解步驟。
- **隨機量子化 / SPDE**:用隨機偏微分方程(Hairer 正則性結構等)定義規範場的動力學。優:2D/3D 已有嚴格構造,是近十年最亮眼的新工具;劣:4 維 Yang–Mills 的 SPDE 是臨界維度,現有理論不適用。
- **物理端輸入**:lattice QCD 數值、AdS/CFT 直覺提供「答案應該長什麼樣」的指引,但不構成證明。

## AI 可以怎麼幫忙

- **形式化現況**:此題距形式化最遠——連「要形式化的定理陳述」都依賴 Wightman/OS 公理框架,mathlib 目前只有測度論、泛函分析等底層積木;有零星社群嘗試在 Lean 中定義 Wightman 公理,尚無實質理論建構。可行的近期目標是形式化 2D Yang–Mills 或格點模型的基本性質。
- **ML/LLM 輔助的已知嘗試**:機器學習在 lattice QCD 有成熟應用(流模型 flow-based sampling 加速格點取樣,如 MIT–DeepMind 合作的系列工作),屬於物理數值端而非嚴格數學端;尚無 AI 直接推進構造性證明的案例。
- **本 repo 可做的事**:
  - 實作小規模格點規範理論($\mathbb{Z}_2$ 或 $U(1)$、小格點)的 Monte Carlo,數值觀察 Wilson 迴圈面積律/周長律轉變——這是理解質量間隙與禁閉的最佳動手入口。
  - 整理「宣稱解決此題的預印本」清單並記錄其已知問題,做成防誤導的追蹤頁(此題的可疑聲明特別多)。
  - 維護 Chatterjee 綜述、隨機量子化系列論文的閱讀筆記與依賴關係圖。

## 關鍵文獻與資源

- Clay 官方問題陳述(Jaffe–Witten):https://www.claymath.org/millennium/yang-mills-the-maths-gap/
- A. Jaffe, E. Witten, "Quantum Yang–Mills Theory"(官方問題文件):https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- S. Chatterjee, "Yang–Mills for probabilists" 及系列講義:https://souravchatterjee.su.domains/(含 [3D Yang–Mills 進展講義](https://souravchatterjee.su.domains/beam-3dym-msri-trans.pdf))
- Chandra, Chevyrev, Hairer, Shen, "Langevin dynamic for the 2D Yang–Mills measure":https://arxiv.org/abs/2006.04987
- Harvard 千禧年講座活動頁(2025):https://www.math.harvard.edu/event/millennium-prize-problems-lecture-sourav-chatterjee-yang-mills-existence-and-mass-gap
- 格點規範理論入門:M. Creutz, *Quarks, Gluons and Lattices*(Cambridge University Press)
