# 分析與偏微分方程(Analysis & PDE)未解難題目錄

> 收錄調和分析、複分析、算子理論、譜理論與流體/色散偏微分方程中的著名未解(或近年才解決的)問題。

**主要來源**:
- [Wikipedia — List of unsolved problems in mathematics(Analysis 段)](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Analysis)
- [Open Problem Garden — Analysis](http://www.openproblemgarden.org/category/analysis)
- Tao,《Some recent progress on the restriction conjecture》調和分析綜述([arXiv:math/0303136](https://arxiv.org/abs/math/0303136))

## 難題清單

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| 掛谷集合猜想(Kakeya set conjecture) | ℝⁿ 中含每個方向單位線段的集合,Hausdorff 維數必為 n? | 1917 掛谷/1919 Besicovitch | 部分解決(n≤3 已證,3 維為 Wang–Zahl 2025;n≥4 未解) | [深度檔案](../problems/analysis/kakeya/README.md) |
| 限制猜想(Restriction conjecture) | 球面上的 Fourier 限制算子在猜想的全範圍 Lᵖ 有界? | 1967 Stein | 部分解決(n=2 已證;n≥3 未解) | [arXiv 綜述](https://arxiv.org/abs/math/0303136) |
| Bochner–Riesz 猜想(Bochner–Riesz conjecture) | Bochner–Riesz 平均在臨界指數以上皆 Lᵖ 收斂? | 1930s Bochner/Riesz | 部分解決(n=2 已證 1972;n≥3 未解) | [Wikipedia](https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean) |
| 局部平滑猜想(Local smoothing conjecture) | 波方程解對時間平均後可獲得額外的 Lᵖ 正則性? | 1991 Sogge | 部分解決(2+1 維已證,Guth–Wang–Zhang 2020;高維未解) | [arXiv:1909.10693](https://arxiv.org/abs/1909.10693) |
| Carleson 問題(Schrödinger 逐點收斂)(Carleson's problem) | 初值在多少 Sobolev 正則性下,自由 Schrödinger 演化幾乎處處收斂回初值? | 1980 Carleson | 部分解決(門檻 s=n/(2(n+1)) 除端點外已定;Du–Guth–Li 2017、Du–Zhang 2019) | [arXiv:1805.02775](https://arxiv.org/abs/1805.02775) |
| 不變子空間問題(Invariant subspace problem) | 可分 Hilbert 空間上每個有界算子都有非平凡閉不變子空間? | 1930s von Neumann/Beurling | 未解(Enflo 2023 預印本 ⚠️ 宣稱證明 Hilbert 空間情形,至今未經同儕審查接受) | [Wikipedia](https://en.wikipedia.org/wiki/Invariant_subspace_problem) |
| Sendov 猜想(Sendov's conjecture) | 根都在閉單位圓盤內的多項式,每個根距某臨界點不超過 1? | 1959 Sendov | 部分解決(次數 ≤8 已證;充分大次數已證,Tao 2020) | [arXiv:2012.04125](https://arxiv.org/abs/2012.04125) |
| Crouzeix 猜想(Crouzeix's conjecture) | 矩陣函數演算以數值域為譜集合時,最佳常數為 2? | 2004 Crouzeix | 未解(已知常數 1+√2,Crouzeix–Palencia 2017) | [Wikipedia](https://en.wikipedia.org/wiki/Crouzeix%27s_conjecture) |
| Kadison–Singer 問題(Kadison–Singer problem) | ℓ∞ 對角代數上的純態是否唯一延拓到 B(ℓ²)? | 1959 Kadison/Singer | ✅ 已解決(2013,Marcus–Spielman–Srivastava) | [arXiv:1306.3969](https://arxiv.org/abs/1306.3969) |
| Fuglede 猜想(Fuglede's conjecture) | 集合是譜集合 ⇔ 可平移鋪滿空間? | 1974 Fuglede | 部分解決(n≥3 一般情形已否證,Tao 2004 起;凸體情形全維已證,Lev–Matolcsi 2022;n=1,2 未解) | [Wikipedia](https://en.wikipedia.org/wiki/Fuglede%27s_conjecture) |
| Pompeiu 問題/Schiffer 猜想(Pompeiu problem) | 對所有全等副本積分為零就迫使函數為零的平面域,只有圓盤例外? | 1929 Pompeiu | 未解(2025 有宣稱證明之預印本 ⚠️,未經審查) | [Wikipedia](https://en.wikipedia.org/wiki/Pompeiu_problem) |
| Chowla 猜想(Chowla's conjecture) | Liouville 函數的多點自相關平均為零? | 1965 Chowla | 部分解決(對數平均 2 點 Tao 2016、奇數點 Tao–Teräväinen 2018) | [arXiv:1710.01195](https://arxiv.org/abs/1710.01195) |
| Sarnak 猜想(Sarnak's conjecture) | Möbius 函數與任何零熵動力系統序列無關(正交)? | 2010 Sarnak | 未解(多類零熵系統特例已證) | [AIM 專頁](https://aimath.org/pastworkshops/sarnakconjecture.html) |
| 三維 Euler 方程正則性(Euler equations regularity) | 三維不可壓 Euler 方程的光滑初值會在有限時間爆破嗎? | 18 世紀 Euler(現代提法 20 世紀) | 部分解決(光滑邊界域的光滑資料爆破已證,Chen–Hou 2022/2025;全空間 ℝ³ 未解) | [arXiv:2210.07191](https://arxiv.org/abs/2210.07191) |
| Navier–Stokes 存在性與光滑性(Navier–Stokes existence and smoothness) | 三維 Navier–Stokes 方程的光滑解是否整體存在? | 2000 Clay 千禧年問題 | 未解 | [深度檔案](../problems/millennium/navier-stokes/README.md) |
| Onsager 剩餘問題(post-Onsager problems) | 原 Onsager 猜想(Hölder 指數 1/3 為能量守恆門檻)已證;強 L³ 版本與湍流耗散異常(零階定律)仍開放 | 1949 Onsager | 未解(原猜想 ✅ 2018 Isett 已證) | [Wikipedia](https://en.wikipedia.org/wiki/Onsager%27s_conjecture) |
| 孤立子分解猜想(Soliton resolution conjecture) | 色散方程的整體解漸近分解為孤立子疊加加輻射項? | 1970s–80s(民間猜想) | 部分解決(徑向能量臨界波方程全維已證,Duyckaerts–Kenig–Merle 等 2019–2023;一般情形未解) | [arXiv:2203.09614](https://arxiv.org/abs/2203.09614) |
| Vlasov–Maxwell 方程正則性(Vlasov–Maxwell regularity) | 三維相對論 Vlasov–Maxwell 系統的光滑解是否整體存在? | 1980s Glassey–Strauss | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Analysis) |
| Brennan 猜想(Brennan conjecture) | 單連通域到圓盤的共形映射導數之積分冪估計對 4/3<p<4 成立? | 1978 Brennan | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Analysis) |
| Vitushkin 猜想(Vitushkin's conjecture) | 解析容量為零 ⇔ Favard 長度為零(對 σ-有限長度集合)? | 1967 Vitushkin | 部分解決(有限長度集合已證,David 1998;相關 Painlevé 問題 ✅ 2003 Tolsa 已解;σ-有限情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Analytic_capacity) |
| Bloch 與 Landau 常數(Bloch and Landau constants) | Bloch 常數等單葉性常數的精確值為何? | 1929 Bloch/Landau | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_constants) |
| Smale 平均值問題(Smale's mean value problem) | 次數 ≥2 的多項式必有臨界點 c 使 \|p(c)−p(z)\| ≤ K\|p′(z)(c−z)\|,K=1? | 1981 Smale | 未解(已知 K≤4) | [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_mean_value_problem) |
| Goodman 猜想(Goodman's conjecture) | p-葉(multivalent)函數的係數界估計? | 1948 Goodman | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Analysis) |
| 熱點猜想(Hot spots conjecture) | 凸域上第二 Neumann 特徵函數的極值必在邊界上? | 1974 Rauch | 部分解決(三角形已證,Judge–Mondal 2020;某些多連通域已否證;一般凸域未解) | [Open Problem Garden](http://www.openproblemgarden.org/op/the_hot_spots_conjecture) |
| Pólya 特徵值猜想(Pólya's eigenvalue conjecture) | 任意平面域的 Dirichlet/Neumann 特徵值計數不超過/不低於 Weyl 主項? | 1954 Pólya | 部分解決(鋪磚域已證 1966;圓盤已證,Filonov–Levitin–Polterovich–Sher 2023) | [arXiv:2203.07696](https://arxiv.org/abs/2203.07696) |
| Falconer 距離集猜想(Falconer's distance set conjecture) | 維數超過 n/2 的集合,其距離集有正測度? | 1985 Falconer | 未解(平面已達 5/4 門檻,Guth–Iosevich–Ou–Wang 2020) | [arXiv:1808.09346](https://arxiv.org/abs/1808.09346) |
| Erdős 相似性問題(Erdős similarity problem) | 是否每個無窮實數集合都存在正測度集合不含其任何相似(仿射)副本? | 1974 Erdős | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s_similarity_problem) |

## 值得關注的動態

近 5 年(2021–2026)已解決或有重大進展的問題:

- **三維掛谷集合猜想獲證(2025)**:Hong Wang 與 Joshua Zahl 證明 ℝ³ 中每個掛谷集合的 Hausdorff 與 Minkowski 維數皆為 3,被譽為「百年一遇」的突破([arXiv:2502.17655](https://arxiv.org/abs/2502.17655);[Quanta 報導](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/);[Tao 的技術導覽](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/))。
- **2026 Fields 獎兩位得主出自分析/PDE(2026-07)**:Hong Wang 因掛谷猜想等調和分析工作獲獎(史上第三位女性得主);Yu Deng 因隨機資料色散方程與 Hilbert 第六問題方向的工作獲獎([Quanta:Hong Wang](https://www.quantamagazine.org/hong-wang-wins-2026-fields-medal-the-third-woman-ever-20260723/);[Quanta:Yu Deng](https://www.quantamagazine.org/yu-deng-wins-the-fields-medal-2026-for-his-work-on-the-random-data-problem-20260723/))。
- **Hilbert 第六問題(流體極限)重大進展(2025)**:Deng–Hani–Ma 從牛頓粒子動力學長時間推導出 Boltzmann 方程,進而導出流體方程(預印本,[arXiv:2503.01800](https://arxiv.org/abs/2503.01800))。
- **三維 Euler 方程邊界域爆破獲證(2022–2025)**:Chen–Hou 以電腦輔助證明光滑初值、光滑邊界域的 3D 軸對稱 Euler(及 2D Boussinesq)有限時間爆破;成果 2025 年刊於 PNAS([arXiv:2210.07191](https://arxiv.org/abs/2210.07191);[PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2500940122))。
- **不變子空間問題:Enflo 宣稱未獲確認(2023–)**:Per Enflo 2023 年 5 月上傳預印本宣稱解決 Hilbert 空間情形([arXiv:2305.15442](https://arxiv.org/abs/2305.15442)),至今未在同儕審查期刊發表、未被學界接受,問題仍視為開放;另有其他宣稱證明已被駁斥([arXiv:2411.19409](https://arxiv.org/abs/2411.19409))。
- **Pólya 猜想在圓盤成立(2023)**:Filonov–Levitin–Polterovich–Sher 證明圓盤(首個非鋪磚域)滿足 Pólya 特徵值猜想,刊於 Inventiones Mathematicae([arXiv:2203.07696](https://arxiv.org/abs/2203.07696))。
- **凸體 Fuglede 猜想全維獲證(2022)**:Lev–Matolcsi 證明凸體是譜集合若且唯若可平移鋪滿空間,刊於 Acta Mathematica([arXiv:1904.12262](https://arxiv.org/abs/1904.12262))。
- **孤立子分解:徑向能量臨界波方程全維數獲證(2023)**:Collot–Duyckaerts–Kenig–Merle 等完成所有維數的徑向情形,刊於 Annals of PDE([arXiv:2203.09614](https://arxiv.org/abs/2203.09614))。
- **Liouville 符號模式超多項式增長(2023)**:Matomäki–Radziwiłł–Tao–Teräväinen–Ziegler 刊於 Annals of Mathematics,朝 Sarnak「正熵」猜想推進([Annals 197-2](https://projecteuclid.org/journals/annals-of-mathematics/volume-197/issue-2))。
