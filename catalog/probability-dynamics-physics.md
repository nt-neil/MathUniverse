# 機率、動態系統與數學物理 Probability, Dynamical Systems & Mathematical Physics 未解難題目錄

> 收錄機率論(滲流、隨機矩陣、KPZ)、動態系統(遍歷理論、剛性、混沌)與數學物理(統計力學、量子混沌、構造性 QFT)的著名未解問題,含近年已解決者。

**主要來源**:
- [Wikipedia: List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)(Dynamical systems、Probability、Mathematical physics 段落)
- [Wikipedia: Percolation theory](https://en.wikipedia.org/wiki/Percolation_theory)、[Quantum chaos](https://en.wikipedia.org/wiki/Quantum_chaos) 等專題條目
- IMU 2022 Fields Medal(Duminil-Copin)頌詞:[The work of Hugo Duminil-Copin](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-hdc.pdf)

## 難題清單

### 數學物理與統計力學

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| 楊-米爾斯存在性與質量間隙(Yang–Mills Existence and Mass Gap) | 4 維楊-米爾斯量子場論是否嚴格存在且有質量間隙? | 2000(Clay 千禧年問題) | 未解 | [深度檔案](../problems/millennium/yang-mills/README.md) |
| 4 維構造性 QFT(Interacting QFT in 4D) | 能否嚴格構造任何非平凡的 4 維相互作用量子場論? | 1950 年代起 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Constructive_quantum_field_theory) |
| 希爾伯特第六問題:流體方程的推導(Hilbert's Sixth Problem: Derivation of Fluid Equations) | 能否從牛頓粒子力學經玻爾茲曼方程嚴格導出 Euler/Navier–Stokes 方程? | 1900(Hilbert) | ⚠️ 宣稱證明(2025,Deng–Hani–Ma 預印本宣稱完成推導鏈;數學界高度重視但仍在審查,另有物理詮釋面的批評) | [arXiv:2503.01800](https://arxiv.org/abs/2503.01800)、[批評:arXiv:2504.06297](https://arxiv.org/abs/2504.06297) |
| 玻爾茲曼-西奈遍歷假設(Boltzmann–Sinai Ergodic Hypothesis) | N 個硬球的氣體系統是否遍歷? | 1963(Sinai,溯源 Boltzmann 1870s) | 部分解決(Simányi 已證典型情形與多數配置;完整無條件證明仍待學界確認) | [Wikipedia](https://en.wikipedia.org/wiki/Ergodic_hypothesis) |
| 3 維 Ising 模型臨界指數(3D Ising Critical Exponents) | 嚴格證明 3 維 Ising 模型臨界指數存在並等於共形自舉(conformal bootstrap)之數值 | 1940 年代起 | 未解(共形自舉給出高精度數值,但無嚴格證明) | [Wikipedia](https://en.wikipedia.org/wiki/Ising_critical_exponents) |
| 4 維 Ising/φ⁴ 平凡性(Triviality of 4D Ising & φ⁴) | 4 維 Ising 與 φ⁴ 模型的尺度極限是否為高斯(平凡)場? | 1970 年代(溯源 Landau–Ginzburg) | ✅ 已解決(2021,Aizenman–Duminil-Copin,Annals of Mathematics) | [arXiv:1912.07973](https://arxiv.org/abs/1912.07973) |
| 臨界滲流的共形不變性(Conformal Invariance of Critical Percolation) | 三角格以外(如 Z² bond/site)的臨界滲流是否共形不變並收斂到 SLE₆? | 1994(Langlands 等)/2001(Smirnov 證三角格) | 部分解決(僅三角格 site percolation 已證) | [Wikipedia](https://en.wikipedia.org/wiki/Percolation_theory) |
| 3 維臨界滲流(Critical Percolation in 3D) | 證明 θ(p_c)=0(臨界點無無限簇)與 3≤d≤10 的臨界指數 | 1980 年代(Grimmett 等) | 未解(d≥11 已證平均場行為;slab 情形已證;3≤d≤10 全開放) | [Wikipedia](https://en.wikipedia.org/wiki/Percolation_critical_exponents) |
| 2D FK 滲流完整共形不變性(Full Conformal Invariance of Planar FK Percolation) | 1≤q≤4 的隨機簇模型尺度極限是否完全共形不變(收斂到 CLE)? | 1970 年代起 | 部分解決(旋轉不變性已證,見動態節;q=2 即 FK-Ising 共形不變性已證) | [arXiv:2012.11672](https://arxiv.org/abs/2012.11672) |
| 自我迴避隨機走臨界指數(Self-Avoiding Walk Critical Exponents) | 證明 2 維 SAW 的 ν=3/4、γ=43/32 並收斂到 SLE₈⧸₃;3 維指數亦全開放 | 1953(Flory)/1982(Nienhuis) | 未解(蜂巢格連結常數 √(2+√2) 已證(2012);d≥5 平均場已證;d=4 對數修正部分已證) | [Wikipedia](https://en.wikipedia.org/wiki/Self-avoiding_walk) |
| KPZ 普遍性猜想(KPZ Universality Conjecture) | 證明所有一維隨機增長模型(ballistic deposition、一般 corner growth 等)都收斂到 KPZ 不動點 | 1986(Kardar–Parisi–Zhang) | 部分解決(KPZ 方程與有限程 exclusion process 已證收斂,見動態節;一般模型全開放) | [Wikipedia](https://en.wikipedia.org/wiki/KPZ_fixed_point) |
| 隨機帶狀矩陣去局域化轉變(Random Band Matrix Delocalization Transition) | 證明帶寬 W 穿越臨界尺度時特徵向量的局域化/去局域化相變 | 1990 年代(Fyodorov–Mirlin 等) | 部分解決(2025:一維 W≫N^{1/2}、二維 W≥N^c 的去局域化與普遍性已證,預印本;互補的局域化端與臨界情形開放) | [arXiv:2503.07606](https://arxiv.org/abs/2503.07606)、[arXiv:2506.06441](https://arxiv.org/abs/2506.06441) |
| Anderson 模型擴展態(Extended States for the Anderson Model) | 證明 3 維弱無序 Anderson 模型存在絕對連續譜(擴展態) | 1958(Anderson) | 未解(強無序局域化已證;去局域化端無任何嚴格結果) | [Wikipedia](https://en.wikipedia.org/wiki/Anderson_localization) |
| Abelian 沙堆模型(Abelian Sandpile Model) | 證明雪崩分布的臨界指數與各維度的尺度極限行為 | 1987(Bak–Tang–Wiesenfeld)/1990(Dhar) | 部分解決(Z² 上終態的尺度極限與碎形結構已證,Pegden–Smart–Levine;雪崩指數開放) | [Wikipedia](https://en.wikipedia.org/wiki/Abelian_sandpile_model) |
| 馬可夫鏈 cutoff 現象(Cutoff Phenomenon) | 刻劃哪些馬可夫鏈族呈現 cutoff(Peres 的 product condition 猜想) | 1986(Aldous–Diaconis)/2004(Peres) | 部分解決(非負曲率鏈已證,Salez;一般判準開放) | [Wikipedia](https://en.wikipedia.org/wiki/Cutoff_(statistics)) |

### 動態系統

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Furstenberg ×2×3 猜想(Furstenberg ×2 ×3 Conjecture) | 圓周上同時對 ×2 與 ×3 不變的遍歷測度是否只有 Lebesgue 與原子測度? | 1967(Furstenberg) | 未解(正熵情形已證,Rudolph 1990) | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics) |
| Zimmer 綱領(Zimmer Program) | 高秩格在低維流形上的光滑作用必(近乎)平凡 | 1980 年代(Zimmer) | 部分解決(SL(n,Z) 與 cocompact 格已證,Brown–Fisher–Hurtado,Annals 2022;非一致格與其他半單群情形進行中) | [Wikipedia](https://en.wikipedia.org/wiki/Zimmer%27s_conjecture) |
| Sarnak Möbius 無關性猜想(Sarnak's Möbius Disjointness Conjecture) | Möbius 函數與所有零熵動態系統產生的序列無關 | 2010(Sarnak) | 未解(對數平均版與多類零熵系統已證;完整猜想開放) | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics) |
| 標準映射正熵問題(Positive Metric Entropy of the Chirikov Standard Map) | 證明 Chirikov 標準映射在某參數下有正 Lebesgue 測度的混沌集(正度量熵) | 1969(Chirikov)/1980 年代(Sinai 提問) | 未解(Berger–Turaev 證明了任意小擾動後可正熵,原映射開放) | [Wikipedia](https://en.wikipedia.org/wiki/Standard_map) |
| Palis 猜想(Palis Conjecture) | 典型動態系統只有有限個吸引子,且統計性質良好(SRB 測度) | 1995(Palis) | 未解(一維與部分雙曲情形有進展) | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics) |
| Arnold 擴散(Arnold Diffusion) | 近可積哈密頓系統中作用變數的大範圍漂移是否典型存在? | 1964(Arnold) | 部分解決(2.5 自由度凸哈密頓系統已證,Kaloshin–Zhang;一般情形開放) | [Wikipedia](https://en.wikipedia.org/wiki/Arnold_diffusion) |
| MLC 猜想(Mandelbrot Set Locally Connected) | Mandelbrot 集是否局部連通?(蘊涵雙曲性稠密) | 1980 年代(Douady–Hubbard) | 未解(無窮可重整化情形近年有進展,Dudko–Lyubich) | [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set) |
| Lorenz 吸引子的解析理論(Analytic Theory of the Lorenz Attractor) | 不依賴電腦輔助地證明經典 Lorenz 系統的奇異吸引子,並刻劃完整分岔與統計性質 | 1963(Lorenz)/1998(Smale 第 14 問題) | 部分解決(存在性已證,Tucker 2002,電腦輔助;純解析證明與完整統計理論開放) | [Wikipedia](https://en.wikipedia.org/wiki/Lorenz_system) |
| Fermi–Pasta–Ulam–Tsingou 問題(FPUT Paradox) | 嚴格解釋 FPUT 鏈的回歸現象與熱化時間尺度 | 1955(Fermi–Pasta–Ulam–Tsingou) | 未解(KAM/波湍流觀點有部分結果) | [Wikipedia](https://en.wikipedia.org/wiki/Fermi%E2%80%93Pasta%E2%80%93Ulam%E2%80%93Tsingou_problem) |
| Painlevé 猜想(Painlevé Conjecture) | n≥4 體問題存在非碰撞奇點(粒子有限時間跑到無窮遠) | 1895(Painlevé) | ✅ 已解決(n≥5 Xia 1992;n=4 Xue 2020,Acta Mathematica,完整解決) | [Acta Math. 224 (2020)](https://projecteuclid.org/journals/acta-mathematica/volume-224/issue-2/Non-collision-singularities-in-a-planar-4-body-problem/10.4310/ACTA.2020.v224.n2.a2.pdf) |
| 太陽系與 n 體長期穩定性(Long-term Stability of the Solar System / n-body Problem) | 太陽系(或典型 n 體系統)是否在天文時間尺度上穩定? | 18 世紀起(Laplace、Poincaré) | 未解(KAM 理論給出正測度穩定初值;數值顯示邊緣混沌) | [Wikipedia](https://en.wikipedia.org/wiki/Stability_of_the_Solar_System) |

### 量子混沌與譜理論

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Berry–Tabor 猜想(Berry–Tabor Conjecture) | 典型可積系統的量子能階間距服從 Poisson 統計 | 1977(Berry–Tabor) | 未解(特殊環面/橢圓的配對相關已證,Eskin–Margulis–Mozes 等) | [Wikipedia](https://en.wikipedia.org/wiki/Quantum_chaos) |
| Bohigas–Giannoni–Schmit 猜想(BGS Conjecture) | 混沌系統的量子能階統計服從隨機矩陣(GOE/GUE)分布 | 1984(Bohigas–Giannoni–Schmit) | 未解(僅啟發式的週期軌道理論支持) | [Wikipedia](https://en.wikipedia.org/wiki/Quantum_chaos) |
| 量子唯一遍歷性(Quantum Unique Ergodicity, QUE) | 負曲率流形上高能特徵函數是否等分布(無 scar)? | 1994(Rudnick–Sarnak) | 部分解決(算術情形已證,Lindenstrauss 2006、Holowinsky–Soundararajan 2010;一般負曲率流形開放) | [Wikipedia](https://en.wikipedia.org/wiki/Quantum_ergodicity) |

## 值得關注的動態

- **✅ 4 維 Ising/φ⁴ 平凡性獲證(2021)**:Aizenman 與 Duminil-Copin 證明 4 維(臨界維度)Ising 與 φ⁴ 模型的尺度極限為高斯場,解決半世紀懸案;發表於 Annals of Mathematics 194 (2021)。[arXiv:1912.07973](https://arxiv.org/abs/1912.07973)
- **KPZ 普遍性重大嚴格化(2021–2022)**:Quastel–Sarkar 證明 KPZ 方程與有限程 exclusion process 在 1:2:3 標度下收斂到 KPZ 不動點(J. Amer. Math. Soc., 2022)([arXiv:2008.06584](https://arxiv.org/abs/2008.06584));Dauvergne–Ortmann–Virág 的 directed landscape(Acta Math. 229, 2022)確立了完整的極限空間。一般增長模型的普遍性仍開放。
- **2D 臨界格點模型旋轉不變性(2020–,Fields Medal 2022)**:Duminil-Copin–Kozlowski–Krachun–Manolescu–Oulamara 證明 1≤q≤4 隨機簇模型大尺度旋轉不變性,是邁向完整共形不變性的關鍵一步([arXiv:2012.11672](https://arxiv.org/abs/2012.11672));Duminil-Copin 以滲流與 Ising 系列工作獲 2022 Fields Medal([頌詞](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-hdc.pdf))。
- **Zimmer 猜想核心情形發表(2022–)**:Brown–Fisher–Hurtado 的 cocompact 格情形正式發表於 Annals of Math. 196 (2022)([期刊頁](https://projecteuclid.org/journals/annals-of-mathematics/volume-196/issue-3/Zimmers-conjecture--Subexponential-growth-measure-rigidity-and-strong-property/10.4007/annals.2022.196.3.1.short));非一致格情形持續推進([arXiv:2105.14541](https://arxiv.org/abs/2105.14541))。
- **隨機帶狀矩陣去局域化突破(2025,預印本)**:Yau–Yin 學派(Dubova–Yang–Yau–Yin 等)證明一維帶寬 W≫N^{1/2} 與二維 W≥N^c 的去局域化、QUE 與本徵值普遍性,逼近物理預測的臨界帶寬([arXiv:2503.07606](https://arxiv.org/abs/2503.07606)、[arXiv:2506.06441](https://arxiv.org/abs/2506.06441))。
- **⚠️ 希爾伯特第六問題宣稱解決(2025,預印本)**:Deng–Hani–Ma 宣稱從硬球牛頓力學嚴格導出玻爾茲曼方程進而導出流體方程([arXiv:2503.01800](https://arxiv.org/abs/2503.01800));數學界普遍視為重大突破,但尚未正式發表,且有針對其物理詮釋(稀薄氣體極限的適用範圍)的批評([arXiv:2504.06297](https://arxiv.org/abs/2504.06297))。
- **✅ Painlevé 猜想完整解決(2020 發表)**:Xue 證明平面四體問題存在非碰撞奇點(Acta Math. 224, 2020),補上 n=4 最後一塊拼圖;雖略早於本窗口,狀態常被過時清單誤列為開放,特此標注。[期刊頁](https://projecteuclid.org/journals/acta-mathematica/volume-224/issue-2/Non-collision-singularities-in-a-planar-4-body-problem/10.4310/ACTA.2020.v224.n2.a2.pdf)
