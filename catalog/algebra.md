# 代數與代數幾何(Algebra & Algebraic Geometry)未解難題目錄

> 收錄群論、環論、表示論、交換代數與代數幾何(含算術幾何交界)的著名未解問題,及近年才解決的重大猜想。

**主要來源**:
- Wikipedia [List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)(Algebra、Algebraic geometry 段)
- [Open Problem Garden — Algebra](http://www.openproblemgarden.org/category/algebra)
- 逐題查證之 arXiv 預印本與期刊頁面(見各列連結)

## 難題清單

### 群論、環論與表示論

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| 反 Galois 問題(Inverse Galois Problem) | 每個有限群都是某個 ℚ 的 Galois 擴張的 Galois 群嗎? | 19 世紀末(Hilbert 1892 已研究) | 部分解決(可解群:Shafarevich;許多單群已實現;一般情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Inverse_Galois_problem) |
| Kaplansky 單位猜想(Unit Conjecture) | 無撓群的群環 K[G] 是否只有平凡單位元? | Higman 1940 / Kaplansky 1970 | ✅ 已否證(2021,Gardam 給出特徵 2 反例;Murray 推廣至所有正特徵;特徵 0 仍開放) | [arXiv:2102.11818](https://arxiv.org/abs/2102.11818) |
| Kaplansky 零因子猜想(Zero Divisor Conjecture) | 無撓群的群環 K[G] 是否沒有非平凡零因子? | Kaplansky 1970(源於 1940s) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures) |
| Kaplansky 冪等元猜想(Idempotent Conjecture) | 無撓群的群環是否只有 0 和 1 兩個冪等元? | Kaplansky 1970 | 部分解決(滿足 Baum–Connes / Farrell–Jones 的大類群已證) | [Wikipedia](https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures) |
| Köthe 猜想(Köthe Conjecture) | 若環無非零 nil 理想,是否也無非零單邊 nil 理想? | Köthe 1930 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/K%C3%B6the_conjecture) |
| Jacobson 猜想(Jacobson's Conjecture) | 雙邊 Noetherian 環中 Jacobson 根的冪之交是否為零? | Jacobson 1956 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Jacobson%27s_conjecture) |
| 有界 Burnside 問題(Bounded Burnside Problem) | 有限生成、指數有界的群必有限嗎?如 B(2,5)、B(2,8) 是否有限? | Burnside 1902 | 部分解決(大奇數指數為無限:Novikov–Adian 1968;受限版已解:Zelmanov 1991;B(2,5) 等小指數情形未知) | [Wikipedia](https://en.wikipedia.org/wiki/Burnside_problem) |
| Andrews–Curtis 猜想(Andrews–Curtis Conjecture) | 平凡群的平衡展示是否都能經 Nielsen 變換與共軛化為標準展示? | Andrews–Curtis 1965 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Andrews%E2%80%93Curtis_conjecture) |
| Whitehead 非球面性猜想(Whitehead Asphericity Conjecture) | 非球面二維複形的子複形是否仍非球面? | Whitehead 1941 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Whitehead_conjecture) |
| Tarski 自由群問題(Tarski's Problems) | 非交換自由群是否初等等價?其一階理論是否可判定? | Tarski 約 1945 | 部分解決(初等等價:Sela 與 Kharlampovich–Myasnikov 於 2006 前後證明;可判定性之證明仍有爭議,Sela 2014 指出 KM 論文有缺口) | [arXiv:1401.5711](https://arxiv.org/abs/1401.5711) |
| McKay 猜想(McKay Conjecture) | 有限群中次數與 ℓ 互質的不可約特徵標數,等於 Sylow ℓ-子群正規化子中的對應數? | McKay 1971–72 | ✅ 已解決(2025,Cabanes–Späth,Annals of Mathematics 203 (2026)) | [Annals](https://annals.math.princeton.edu/2026/203-3/p05) |
| Brauer 高度零猜想(Brauer's Height Zero Conjecture) | 區塊內所有不可約特徵標高度為零 ⇔ 其虧群為交換群? | Brauer 1955 | ✅ 已解決(2024,Malle–Navarro–Schaeffer Fry–Tiep,Annals 200 (2024)) | [Annals](https://projecteuclid.org/journals/annals-of-mathematics/volume-200/issue-2/Brauers-Height-Zero-Conjecture/10.4007/annals.2024.200.2.4.short) |
| Alperin 權猜想(Alperin Weight Conjecture) | 有限群模表示中單模數可由「權」的個數算出? | Alperin 1986 | 未解(已化約至單群之歸納條件) | [Wikipedia](https://en.wikipedia.org/wiki/Alperin%27s_weight_conjecture) |
| Connes 嵌入問題(Connes Embedding Problem) | 每個 II₁ 型 von Neumann 代數是否可嵌入超冪 R^ω? | Connes 1976 | ✅ 已否證(2020,Ji–Natarajan–Vidick–Wright–Yuen 經量子複雜度結果 MIP*=RE) | [arXiv:2001.04383](https://arxiv.org/abs/2001.04383) |
| Casas-Alvero 猜想(Casas-Alvero Conjecture) | 特徵 0 域上 d 次多項式若與每個導數都有公因式,必為 (X−α)^d? | Casas-Alvero 2001 | ⚠️ 宣稱證明(Ghosh 2025 預印本 arXiv:2501.09272,尚待審查;此前多個宣稱曾被推翻) | [arXiv:2501.09272](https://arxiv.org/abs/2501.09272) |
| Serre 猜想 II(Serre's Conjecture II) | 特徵維數 ≤2 的完全域上,單連通半單代數群的 H¹ 是否消沒? | Serre 1962 | 部分解決(古典型與若干例外型已證) | [Wikipedia](https://en.wikipedia.org/wiki/Serre%27s_conjecture_II_(algebra)) |
| Serre 正性猜想(Serre's Positivity Conjecture) | 正則局部環上相交重數 χ 在維數條件下是否恆正? | Serre 約 1958–65 | 部分解決(消沒:Roberts、Gillet–Soulé;非負性:Gabber;嚴格正性未解) | [Wikipedia](https://en.wikipedia.org/wiki/Serre%27s_multiplicity_conjectures) |

### 代數幾何與算術幾何

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Hodge 猜想(Hodge Conjecture) | 射影複流形上的 (p,p) 型有理上同調類都來自代數閉鏈? | Hodge 1950 | 未解(千禧年大獎問題) | [深度檔案](../problems/millennium/hodge-conjecture/README.md) |
| BSD 猜想(Birch–Swinnerton-Dyer Conjecture) | 橢圓曲線的秩等於其 L-函數在 s=1 的消沒階? | Birch, Swinnerton-Dyer 1965 | 部分解決(解析秩 ≤1:Gross–Zagier、Kolyvagin;千禧年大獎問題) | [深度檔案](../problems/millennium/birch-swinnerton-dyer/README.md) |
| Grothendieck 標準猜想(Standard Conjectures on Algebraic Cycles) | 代數閉鏈與上同調的關係(Lefschetz 型、Hodge 型等)是否成立? | Grothendieck 1968 | 部分解決(曲面與交換簇的部分情形;一般情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Standard_conjectures_on_algebraic_cycles) |
| Tate 猜想(Tate Conjecture) | 有限生成域上簇的 Galois 不變上同調類都來自代數閉鏈? | Tate 1963 | 部分解決(交換簇的除子:Faltings;K3 曲面除子已證;一般未解) | [Wikipedia](https://en.wikipedia.org/wiki/Tate_conjecture) |
| Fontaine–Mazur 猜想(Fontaine–Mazur Conjecture) | 哪些 p-進 Galois 表示來自代數幾何/自守形式? | Fontaine, Mazur 1995 | 部分解決(2 維不可約 odd regular 情形對所有奇質數 p 已完成:Kisin、Emerton、Pan 2022、p=3 於 2024) | [arXiv:2412.06812](https://arxiv.org/abs/2412.06812) |
| Langlands 綱領(Langlands Program)〔彙總條目〕 | 自守表示與 Galois 表示之間的對應網絡 | Langlands 1967 | 部分解決(函數體 GL_n:L. Lafforgue 2002;局部朗蘭茲 GL_n 已證;幾何朗蘭茲 2024 宣告證明、廣獲接受但仍為預印本;數體一般情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Langlands_program) |
| Grothendieck 截面猜想(Section Conjecture) | 數體上雙曲曲線的有理點與其平展基本群短正合列的截面一一對應? | Grothendieck 1983 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Section_conjecture) |
| Grothendieck–Katz p-曲率猜想(p-Curvature Conjecture) | 代數微分方程若對幾乎所有質數 mod p 平凡,是否有代數解基? | Grothendieck 約 1970(Katz 形式化) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Grothendieck%E2%80%93Katz_p-curvature_conjecture) |
| Jacobian 猜想(Jacobian Conjecture) | Jacobian 行列式為非零常數的多項式映射必為多項式可逆? | Keller 1939 | ⚠️ 宣稱否定解決(2026-07-20 Alpöge 公布 C³ 顯式反例,算術經獨立驗算但未經正式審查;n=2 仍開放) | [Secret Blogging Seminar](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)、[詳見 famous-lists](famous-lists.md) |
| Dixmier 猜想(Dixmier Conjecture) | Weyl 代數的自同態必為自同構? | Dixmier 1968 | 未解(穩定等價於 Jacobian 猜想:Tsuchimoto、Belov-Kanel–Kontsevich) | [Wikipedia](https://en.wikipedia.org/wiki/Dixmier_conjecture) |
| Zariski 消去問題(Zariski Cancellation Problem) | V×𝔸¹ ≅ 𝔸^{n+1} 是否蘊涵 V ≅ 𝔸ⁿ? | Zariski 1949 | 部分解決(正特徵 n≥3 已否證:Gupta 2014;特徵 0、n≥3 仍開放;n≤2 成立) | [arXiv:1309.1368](https://arxiv.org/abs/1309.1368) |
| Nagata 曲線猜想(Nagata's Conjecture on Curves) | 過平面上 r≥10 個一般位置點、重數給定的曲線最低次數下界 | Nagata 1959 | 部分解決(r 為完全平方時已證:Nagata;一般情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Nagata%27s_conjecture_on_curves) |
| 正特徵奇點消解(Resolution of Singularities in Characteristic p) | 正特徵域上任意維數簇是否存在奇點消解? | 源於 Zariski;特徵 0 由 Hironaka 1964 解決 | 部分解決(維數 ≤3:Abhyankar、Cossart–Piltant;高維未解) | [Wikipedia](https://en.wikipedia.org/wiki/Resolution_of_singularities) |
| 豐沛性猜想(Abundance Conjecture) | 極小模型上 nef 的典範除子是否半豐沛? | 極小模型綱領,1980s | 部分解決(維數 ≤3 已證;高維未解) | [Wikipedia](https://en.wikipedia.org/wiki/Abundance_conjecture) |
| Fujita 猜想(Fujita Conjecture) | K_X + mL 在 m≥dim X+1 時基點自由、m≥dim X+2 時極豐沛? | Fujita 1988 | 部分解決(基點自由性:維數 ≤5 已證,Reider、Ein–Lazarsfeld、Kawamata、Ye–Zhu) | [Wikipedia](https://en.wikipedia.org/wiki/Fujita_conjecture) |
| Green 猜想(Green's Conjecture) | 典範曲線的 syzygy 消沒由 Clifford 指數決定? | Green 1984 | 部分解決(一般(generic)曲線:Voisin 2002–05;任意曲線未解) | [Wikipedia](https://en.wikipedia.org/wiki/Green%27s_conjecture) |
| Hartshorne 猜想(Hartshorne's Conjecture) | ℙⁿ 中小餘維(如 2n/3 以下)的光滑子簇必為完全交? | Hartshorne 1974 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Hartshorne%27s_conjectures) |
| 權-單值猜想(Weight-Monodromy Conjecture) | 局部域上簇的 ℓ-進上同調之單值濾過與權濾過相符? | Deligne 1970 | 部分解決(維數 ≤2、set-theoretic 完全交情形:Scholze 2012) | [Wikipedia](https://en.wikipedia.org/wiki/Weight_monodromy_conjecture) |

## 值得關注的動態

近五年(2021–2026)本領域已解決或有重大進展的問題:

- **Kaplansky 單位猜想被否證(2021)**:Giles Gardam 在特徵 2 域上給出無撓群群環的非平凡單位元反例([arXiv:2102.11818](https://arxiv.org/abs/2102.11818),刊於 Annals of Mathematics 194 (2021));Alan Murray 隨即推廣至所有正特徵([arXiv:2106.02147](https://arxiv.org/abs/2106.02147))。特徵 0 情形與零因子、冪等元猜想仍開放。
- **幾何朗蘭茲猜想宣告證明(2024)**:Gaitsgory、Raskin 等九人以五篇、近千頁論文證明(範疇化、無分歧)幾何朗蘭茲猜想([arXiv:2405.03599](https://arxiv.org/abs/2405.03599) 起,第五篇 [arXiv:2409.09856](https://arxiv.org/abs/2409.09856);[Quanta 報導](https://www.quantamagazine.org/monumental-proof-settles-geometric-langlands-conjecture-20240719/))。截至 2026 年仍為預印本(持續修訂中),但已廣獲學界接受,Gaitsgory 因此獲 2025 年 Breakthrough Prize。
- **Brauer 高度零猜想證明完成(2024)**:Malle、Navarro、Schaeffer Fry、Tiep 補上奇質數方向,完成 Brauer 1955 年猜想全證,刊於 [Annals of Mathematics 200 (2024) 557–608](https://projecteuclid.org/journals/annals-of-mathematics/volume-200/issue-2/Brauers-Height-Zero-Conjecture/10.4007/annals.2024.200.2.4.short)。
- **McKay 猜想證明完成(2024–25)**:Cabanes 與 Späth 完成最後的例外型單群歸納條件驗證,證明 1971 年的 McKay 猜想([arXiv:2410.20392](https://arxiv.org/abs/2410.20392)),2025 年 4 月獲接受、刊於 [Annals of Mathematics 203 (2026)](https://annals.math.princeton.edu/2026/203-3/p05);[Quanta 報導](https://www.quantamagazine.org/after-20-years-math-couple-solves-major-group-theory-problem-20250219/)。
- **Fontaine–Mazur 猜想 2 維情形收尾(2022–24)**:Lue Pan 以完備上同調方法解決剩餘可約情形,使 2 維 regular 情形在 p≥5 完成;2024 年預印本再解決 p=3([arXiv:2412.06812](https://arxiv.org/abs/2412.06812)),2 維不可約 regular 情形對所有奇質數告成。
- **Connes 嵌入問題被否證(2020–21)**:量子計算複雜度結果 MIP*=RE 否證了 Connes 1976 年的嵌入問題([arXiv:2001.04383](https://arxiv.org/abs/2001.04383),獲 2021 ACM 論文獎項肯定)。
- **Casas-Alvero 猜想宣稱證明(2025)**:Soham Ghosh 以 Koszul 同調給出全特徵 0 情形的證明([arXiv:2501.09272](https://arxiv.org/abs/2501.09272)),⚠️ 仍為預印本、待同儕審查;此猜想過去已有多個宣稱證明被推翻,狀態暫不列為已解決。
