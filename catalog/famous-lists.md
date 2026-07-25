# 著名難題名單總覽(Famous Problem Lists)

> 收錄數學史上與現行最具影響力的「難題清單」:每份清單一節,含背景與逐題(或摘要)現況。本檔是跨領域索引,個別難題的深度檔案見 `problems/`。

**主要來源**:
- [Hilbert's problems — Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_problems)
- [Millennium Prize Problems — Clay Mathematics Institute](https://www.claymath.org/millennium-problems/)
- [Smale's problems — Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems)
- [Landau's problems — Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_problems)
- [Erdős Problems Database](https://www.erdosproblems.com/)(Thomas Bloom 維護)

**狀態標記**:`未解`/`部分解決`/`✅ 已解決(年份)`/`⚠️ 宣稱證明或甫公布之預印本`/`太模糊`(無法判定已解與否)/`有爭議`(是否算解決無共識)。

**查證註記**:希爾伯特與 Smale 清單各來源說法常互相矛盾(尤其希爾伯特第 9、11、20、21、22 題)。本檔以英文 Wikipedia 2026-07 版的狀態欄為基準,分歧處在表內註明。

---

## 1. 希爾伯特 23 問題(Hilbert's Problems, 1900)

David Hilbert 於 1900 年巴黎國際數學家大會演講提出的 23 個問題,形塑了整個 20 世紀數學的方向。部分問題陳述精確、已有定論;部分(如第 4、6、23 題)較像研究綱領,無法判定「已解與否」。另有一題「第 24 問題」(證明的簡單性判準)2000 年才從手稿中被發現,未列入原清單。

| # | 題名 | 狀態 | 備註/來源 |
|---|---|---|---|
| 1 | 連續統假設(Continuum Hypothesis) | 有爭議 | Gödel(1940)+ Cohen(1963)證明其獨立於 ZFC;「這算不算解答」無共識。[Wikipedia](https://en.wikipedia.org/wiki/Continuum_hypothesis) |
| 2 | 算術公理的相容性(Consistency of arithmetic) | 有爭議 | Gödel 不完備定理(1931)、Gentzen 相容性證明(1936);是否回答了希爾伯特原意無共識。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_second_problem) |
| 3 | 等體積多面體可否剖分互拼(Equidecomposability of polyhedra) | ✅ 已解決(1900,否定) | Dehn 不變量;23 題中最早解決。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_third_problem) |
| 4 | 以直線為測地線的幾何(Geometries with straight lines as geodesics) | 太模糊 | 公認陳述過於寬泛,無法判定已解與否。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_fourth_problem) |
| 5 | 連續群可否免去可微性假設(Lie groups without differentiability) | ✅ 已解決(1952,依常見詮釋) | Gleason、Montgomery–Zippin;Wikipedia 註明「視『連續群』詮釋而定」。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_fifth_problem) |
| 6 | 物理學的公理化(Axiomatization of physics) | 太模糊/部分 | (a) 機率論:Kolmogorov 公理化(1933)被接受;(b) 力學整體:視詮釋而定。⚠️ Deng–Hani–Ma(2025 預印本)宣稱由牛頓粒子系統嚴格導出流體方程,獲高度重視但「是否解決第 6 題」有異議。[arXiv:2503.01800](https://arxiv.org/abs/2503.01800)、[批評](https://arxiv.org/abs/2504.06297) |
| 7 | 某類數的超越性(Transcendence of α^β) | ✅ 已解決(1934) | Gelfond–Schneider 定理。[Wikipedia](https://en.wikipedia.org/wiki/Gelfond%E2%80%93Schneider_theorem) |
| 8 | 黎曼假設與質數問題(Riemann Hypothesis, Goldbach, twin primes) | 未解 | 三個子問題(RH、哥德巴赫、孿生質數)全數未解;見第 4 節 Landau 問題。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_eighth_problem) |
| 9 | 一般互反律(General reciprocity law) | 部分解決 | 阿貝爾擴張情形由 Artin 互反律(1927)解決;非阿貝爾情形(朗蘭茲綱領)未解。Wikipedia 列為「未解(有部分結果)」。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_ninth_problem) |
| 10 | 丟番圖方程可解性的判定法(Decidability of Diophantine equations) | ✅ 已解決(1970,否定) | Matiyasevich(MRDP 定理):不存在此演算法。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_tenth_problem) |
| 11 | 代數係數二次型(Quadratic forms over number fields) | ✅ 已解決(1924,分歧見備註) | Wikipedia 列為已解(Hasse 局部-全域原理);亦有來源視為僅部分解決。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_eleventh_problem) |
| 12 | Kronecker 青春之夢(Explicit class field theory) | 未解 | CM 理論解決虛二次域情形;Dasgupta–Kakde(2021)在全實域有重要進展。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twelfth_problem) |
| 13 | 七次方程與三變數函數(Solving 7th-degree equations) | 視變體而定 | 連續函數版本:Kolmogorov–Arnold(1957)否定解決;希爾伯特可能原指的代數/解析版本仍未解。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_thirteenth_problem) |
| 14 | 不變量環的有限生成性(Finiteness of invariant rings) | ✅ 已解決(1959,否定) | Nagata 反例。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_fourteenth_problem) |
| 15 | Schubert 計數演算的嚴格化(Rigorous foundation of Schubert calculus) | 部分解決 | 交點理論已嚴格化(van der Waerden、Weil 至現代);逐一驗證 Schubert 的數值仍在進行。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_fifteenth_problem) |
| 16 | 實代數曲線的拓撲與極限環(Topology of real curves; limit cycles) | 未解 | 兩部分皆開放;極限環個數連二次系統都未定。亦即 Smale 第 13 題。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem) |
| 17 | 正定有理函數之平方和表示(Sums of squares) | ✅ 已解決(1927) | Artin。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_seventeenth_problem) |
| 18 | 晶體群、鑲嵌與最密堆積(Space groups; sphere packing) | ✅ 已解決 | (a) 晶體群有限:Bieberbach(1910);(b) 非正規鑲嵌:Reinhardt(1928);(c) Kepler 猜想:Hales(1998,電腦輔助;2014 Flyspeck 形式化驗證)。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_eighteenth_problem) |
| 19 | 正則變分問題解的解析性(Analyticity of solutions) | ✅ 已解決(1957) | De Giorgi 與 Nash 獨立證明。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_nineteenth_problem) |
| 20 | 一般邊值問題(General boundary value problems) | 部分解決 | 20 世紀變分法與非線性 PDE 的核心主題,大量情形已解;Wikipedia 列為「未完全解決」。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twentieth_problem) |
| 21 | 指定單值群的 Fuchsian 方程(Riemann–Hilbert problem) | ✅ 已解決(1989,否定) | 長期被誤認已由 Plemelj(1908)解決;Bolibrukh 反例推翻。狀態史本身即是「來源互相矛盾」的著名案例。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twenty-first_problem) |
| 22 | 解析關係的自守函數單值化(Uniformization) | 部分解決 | 單變數核心情形由單值化定理(Koebe、Poincaré,1907)解決;Wikipedia 現列為「未解(有部分結果)」,與多數教科書「已解」的說法分歧。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twenty-second_problem) |
| 23 | 變分法的進一步發展(Further development of calculus of variations) | 太模糊 | 研究綱領而非單一問題。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twenty-third_problem) |

**小計**(依上表分類):明確已解約 10 題(3、5、7、10、11、14、17、18、19、21),部分解決 4 題(9、15、20、22),未解 3 題(8、12、16),太模糊 3 題(4、6、23),有爭議/視詮釋 3 題(1、2、13)。不同來源因分類標準不同,數字常有出入。

---

## 2. 千禧年大獎難題(Millennium Prize Problems, 2000)

克萊數學研究所(Clay Mathematics Institute)於 2000 年懸賞、每題 100 萬美元的 7 個問題,是現行知名度最高的清單。至今僅龐加萊猜想被解決(Perelman 拒領獎金)。

| # | 題名 | 狀態 | 深度檔案 |
|---|---|---|---|
| 1 | 黎曼假設(Riemann Hypothesis) | 未解 | [../problems/millennium/riemann-hypothesis/README.md](../problems/millennium/riemann-hypothesis/README.md) |
| 2 | P 對 NP 問題(P versus NP) | 未解 | [../problems/millennium/p-vs-np/README.md](../problems/millennium/p-vs-np/README.md) |
| 3 | 貝赫–斯維訥通-戴爾猜想(Birch and Swinnerton-Dyer Conjecture) | 未解(rank ≤ 1 等特例已證) | [../problems/millennium/birch-swinnerton-dyer/README.md](../problems/millennium/birch-swinnerton-dyer/README.md) |
| 4 | 霍奇猜想(Hodge Conjecture) | 未解 | [../problems/millennium/hodge-conjecture/README.md](../problems/millennium/hodge-conjecture/README.md) |
| 5 | 納維–斯托克斯方程的存在性與光滑性(Navier–Stokes Existence and Smoothness) | 未解 | [../problems/millennium/navier-stokes/README.md](../problems/millennium/navier-stokes/README.md) |
| 6 | 楊–米爾斯存在性與質量間隙(Yang–Mills Existence and Mass Gap) | 未解 | [../problems/millennium/yang-mills/README.md](../problems/millennium/yang-mills/README.md) |
| 7 | 龐加萊猜想(Poincaré Conjecture) | ✅ 已解決(2003;2010 授獎) | [../problems/millennium/poincare-conjecture/README.md](../problems/millennium/poincare-conjecture/README.md) |

歷年不乏對黎曼假設、Navier–Stokes 等的宣稱證明(如 Atiyah 2018),均未獲學界接受,一律不改變上表狀態。

---

## 3. Smale 18 問題(Smale's Problems, 1998)

Stephen Smale 應 Arnold 之邀,為 21 世紀擬定的 18 個問題(發表於 1998 年 Mathematical Intelligencer),偏重動力系統、計算複雜度與數值分析,與希爾伯特、千禧年清單有三題重疊(RH、P vs NP、龐加萊)。

| # | 題名 | 狀態 | 備註/來源 |
|---|---|---|---|
| 1 | 黎曼假設(Riemann Hypothesis) | 未解 | 同千禧年第 1 題 |
| 2 | 龐加萊猜想(Poincaré Conjecture) | ✅ 已解決(2003) | Perelman;同千禧年第 7 題 |
| 3 | P 是否等於 NP(P versus NP) | 未解 | 同千禧年第 2 題 |
| 4 | 多項式整數零點/τ 猜想(Integer zeros of polynomials; Shub–Smale τ-conjecture) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 5 | 丟番圖曲線的高度界(Height bounds for Diophantine curves) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 6 | n 體問題相對平衡構形的有限性(Finiteness of central configurations) | 部分解決 | 4 體:Hampton–Moeckel(2006);5 體:Albouy–Kaloshin(2012,扣除例外參數集);一般 n 未解。[Wikipedia](https://en.wikipedia.org/wiki/Central_configuration) |
| 7 | 球面上點的分布/對數能量(Distribution of points on the 2-sphere) | 未解 | 有漸近部分結果;與 Smale 的第 7 題演算法版本並存。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 8 | 經濟學均衡的動態調整(Dynamics of price adjustment) | 部分解決 | Gjerstad(2013)、Lindgren(2022)等模型性結果;無公認完全解。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 9 | 線性規劃的強多項式演算法(Strongly polynomial LP algorithm) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 10 | Pugh 閉引理的高階版本(Closing lemma in C^r) | 部分解決 | Asaoka–Irie(2016)解決曲面 Hamiltonian 微分同胚情形;一般情形未解。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 11 | 一維動力系統是否泛型雙曲(Is one-dimensional dynamics generally hyperbolic?) | 部分解決 | 實多項式情形:Kozlovski–Shen–van Strien(2007)✅;複多項式情形未解。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 12 | 微分同胚的中心化子(Centralizers of diffeomorphisms) | 部分解決 | C¹ 情形:Bonatti–Crovisier–Wilkinson(2009)✅;C^r(r>1)未解。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 13 | 希爾伯特第 16 問題後半(Hilbert's 16th problem, limit cycles) | 未解 | 見第 1 節第 16 題 |
| 14 | Lorenz 吸引子是否為奇異吸引子(Lorenz attractor) | ✅ 已解決(2002) | Warwick Tucker 以嚴格區間算術的電腦輔助證明。[Wikipedia](https://en.wikipedia.org/wiki/Lorenz_system) |
| 15 | Navier–Stokes 方程(Navier–Stokes equations) | 未解 | 同千禧年第 5 題 |
| 16 | 雅可比猜想(Jacobian Conjecture) | ⚠️ 宣稱否定解決(2026,n ≥ 3) | 2026-07-20 Levent Alpöge 公布 AI 輔助尋得的 C³ 顯式多項式反例(Jacobian 行列式恆為 −2 但三點對撞),算術已被獨立驗算,維度 ≥ 3 情形否定;n = 2 仍開放。甫公布數日、尚未經正式審查,故標 ⚠️。[Secret Blogging Seminar](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)、[John D. Cook](https://www.johndcook.com/blog/2026/07/21/jacobian-conjecture/) |
| 17 | 平均多項式時間求解多項式方程組(Solving polynomial equations in polynomial time on average) | ✅ 已解決(2008/2016) | Beltrán–Pardo(2008,機率式演算法);Lairez(2016,確定式演算法)。[Lairez 2016](https://arxiv.org/abs/1507.05485) |
| 18 | 智能的極限(Limits of intelligence) | 未解/太廣 | 更接近研究綱領;無公認的精確陳述。[Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |

**小計**:完全解決 3 題(2、14、17),另第 16 題有 2026 年甫公布的否定解(⚠️,n=2 仍開放);部分解決 5 題(6、8、10、11、12);其餘未解。

---

## 4. Landau 四問題(Landau's Problems, 1912)

Edmund Landau 在 1912 年劍橋國際數學家大會上列出的 4 個質數問題,稱其「以現有科學無法攻克」。**114 年後(2026)四題全部仍未解**,但部分進展本身已是數論的里程碑。

| # | 題名 | 狀態 | 最佳進展/來源 |
|---|---|---|---|
| 1 | 哥德巴赫猜想(Goldbach's Conjecture) | 未解 | 弱哥德巴赫(奇數 = 三質數和):Helfgott(2013)✅(學界普遍接受,但完整證明仍以預印本/專書稿流通);強形式最佳:陳氏定理(1973,「1+2」)。[Wikipedia](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) |
| 2 | 孿生質數猜想(Twin Prime Conjecture) | 未解 | 張益唐(2013)首證有界質數間隙(7000 萬);Maynard–Tao 與 Polymath8 降至 246。[Wikipedia](https://en.wikipedia.org/wiki/Twin_prime) |
| 3 | 勒讓德猜想(Legendre's Conjecture,連續平方數間必有質數) | 未解 | 數值驗證至約 2⁶⁴;由質數間隙結果(Baker–Harman–Pintz)可得「幾乎所有」情形。[Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_conjecture) |
| 4 | n²+1 型質數無窮性(Near-square primes) | 未解 | Iwaniec(1978):無窮多 n²+1 至多為兩質數之積;Friedlander–Iwaniec(1997):a²+b⁴ 型質數無窮;Green–Sawhney(2024)在相關二次型有新進展。[Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_problems) |

---

## 5. 其他現行問題集(簡述)

### Simon 問題(Simon Problems, 1984/2000)

數學物理學家 Barry Simon 提出的 15 個問題(1984 年首列,2000 年改版),集中於 Schrödinger 算子與異常譜行為、庫侖能量等。最著名的「十杯馬丁尼問題」(Ten Martini Problem,概周期算子譜為 Cantor 集)由 Puig(2003,部分)與 Avila–Jitomirskaya(2009,完全)解決;Avila 2014 年 Fields 獎部分即因解決多個 Simon 問題。多數問題仍開放。來源:[Wikipedia](https://en.wikipedia.org/wiki/Simon_problems)。

### 丘成桐問題集(Yau's Problem Section, 1982)

丘成桐在《Seminar on Differential Geometry》(1982)發表的 120 個幾何分析問題,主導了其後數十年的幾何分析議程(其中含 Poincaré 猜想、正質量定理相關問題等);2014 年他又發表更新版回顧。多題已解(如 Frankel 猜想、部分 minimal surface 問題),多數仍開放。來源:[Yau, Problem Section 1982 / Perspectives on geometric analysis](https://arxiv.org/abs/math/0602363)。

### Arnold 問題集(Arnold's Problems, 2000)

V. I. Arnold 自 1950 年代起在莫斯科討論班累積的 861 個問題,2000 年結集成書(2004 年英文修訂版,Springer),涵蓋動力系統、奇點理論、辛幾何等,並附各題進展評註。許多題已解,整體無集中維護的現況統計。來源:[Wikipedia](https://en.wikipedia.org/wiki/Arnold%27s_Problems)。

### Erdős 問題全集(Erdős Problems Database, 2023–)

Paul Erdős 一生提出(常附獎金)的問題,由 Thomas Bloom 自 2023 年起在 [erdosproblems.com](https://www.erdosproblems.com/) 系統性彙整。**截至 2026 年中,資料庫共收 1217 題,其中 564 題(約 46%)已解決**(2026 年初為 41%,資料庫持續擴充與更新)。值得注意的動態:2025–2026 年出現多起 AI 輔助解題與 Lean 形式化計畫(如 Google DeepMind 對若干 Erdős 問題的自動化進展),使已解比例快速上升;亦有單題如 Erdős #690 在 2026 年被完整解決。來源:[Erdős Problems Database 概況](https://www.emergentmind.com/topics/erdos-problems-database)、[Xena Project:Erdős 問題形式化](https://xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/)。

---

## 6. 台灣/華人視角:華人數學家與著名難題

| 難題/貢獻 | 內容 | 狀態/來源 |
|---|---|---|
| 陳氏定理(Chen's Theorem) | 陳景潤(1966 宣布、1973 全文)證明充分大偶數 = 質數 + 至多兩質數之積(「1+2」),迄今仍是哥德巴赫猜想的最佳逼近 | ✅(1973)[Wikipedia](https://en.wikipedia.org/wiki/Chen%27s_theorem) |
| 有界質數間隙(Bounded gaps between primes) | 張益唐(Yitang Zhang,2013)首次證明存在無窮多對間隙 < 7000 萬的質數,突破孿生質數猜想僵局;後經 Maynard–Tao 與 Polymath8 降至 246 | ✅(2013)[Wikipedia](https://en.wikipedia.org/wiki/Yitang_Zhang) |
| 卡拉比猜想(Calabi Conjecture) | 丘成桐(Shing-Tung Yau,1976)證明,開啟 Calabi–Yau 流形與弦論幾何;1982 年 Fields 獎 | ✅(1976)[Wikipedia](https://en.wikipedia.org/wiki/Calabi_conjecture) |
| 三維掛谷猜想(Kakeya Conjecture in ℝ³) | 王虹(Hong Wang)與 Joshua Zahl(2025-02 預印本 [arXiv:2502.17655](https://arxiv.org/abs/2502.17655))證明 ℝ³ 中每個 Kakeya 集的 Hausdorff 與 Minkowski 維數皆為 3,被譽為「百年一遇」的突破;主論文截至 2026-07 仍為預印本(相關論文已刊於 Inventiones、JAMS),但已獲學界廣泛接受 | ✅(2025;主文仍預印本)[Terence Tao 解說](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/)、[Quanta](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/) |
| 2026 Fields 獎 | 王虹以掛谷猜想等調和分析工作獲 2026-07-23 費城 ICM 頒發的 Fields 獎——史上第三位女性、首位中國女性得主;同屆鄧宇(Yu Deng)亦獲獎(波湍流、Hilbert 第 6 問題方向),兩人為首度同屆出現兩位中國大陸本科出身的得主 | [Simons Foundation](https://www.simonsfoundation.org/2026/07/23/2026-fields-medals-awarded-to-four-of-worlds-top-mathematicians/)、[NPR](https://www.npr.org/2026/07/23/g-s1-135032/in-a-first-chinese-woman-wins-the-prestigious-fields-medal) |
| Hilbert 第 6 問題(流體方程推導) | 鄧宇(Yu Deng)、Zaher Hani、馬霄(Xiao Ma)(2025-03 預印本)宣稱由硬球粒子系統經 Boltzmann 理論嚴格導出 Euler/Navier–Stokes–Fourier 方程;數學界高度肯定,但「是否構成第 6 題的解答」有公開異議 | ⚠️(2025 預印本)[arXiv:2503.01800](https://arxiv.org/abs/2503.01800) |

---

## 值得關注的動態(2021–2026)

- **2026-07-20**:⚠️ Levent Alpöge 公布雅可比猜想(Smale 第 16 題)在維度 ≥ 3 的顯式反例(AI 輔助發現、算術已獨立驗算);n = 2 情形仍開放。若成立,這是本檔各清單 2020 年代最重大的狀態變動。[Secret Blogging Seminar](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- **2026-07-23**:王虹(掛谷猜想)、鄧宇獲 Fields 獎。[Simons Foundation](https://www.simonsfoundation.org/2026/07/23/2026-fields-medals-awarded-to-four-of-worlds-top-mathematicians/)
- **2025-02**:Wang–Zahl 證明三維掛谷猜想(預印本,已獲學界接受)。[arXiv:2502.17655](https://arxiv.org/abs/2502.17655)
- **2025-03**:⚠️ Deng–Hani–Ma 宣稱解決 Hilbert 第 6 問題的流體推導部分(預印本,詮釋有爭議)。[arXiv:2503.01800](https://arxiv.org/abs/2503.01800)
- **2023–2026**:Erdős Problems Database 上線並快速成長(1217 題、46% 已解),AI 輔助解題與 Lean 形式化成為新趨勢。[erdosproblems.com](https://www.erdosproblems.com/)
- **2021**:Dasgupta–Kakde 在 Hilbert 第 12 問題(全實域顯式類域論)取得重要進展。[Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_twelfth_problem)
