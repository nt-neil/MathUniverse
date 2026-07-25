# 數論(Number Theory)未解難題目錄

> 數論研究整數與質數的性質。本檔收錄該領域著名且有文獻可查的未解(或近年才解決的)問題,涵蓋質數分布、Diophantine 方程、加法數論與超越數論。

**主要來源**:
- [Wikipedia: List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)(數論各節)
- [Open Problem Garden](http://www.openproblemgarden.org/)
- [Wolfram MathWorld: Unsolved Problems](https://mathworld.wolfram.com/UnsolvedProblems.html)
- [Erdős Problems 資料庫](https://www.erdosproblems.com/)

## 難題清單

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| 黎曼猜想(Riemann Hypothesis) | ζ 函數所有非平凡零點的實部都是 1/2 | 1859,Riemann | 未解 | [深度檔案](../problems/millennium/riemann-hypothesis/README.md) |
| 哥德巴赫猜想(Goldbach's Conjecture) | 每個大於 2 的偶數都是兩個質數之和 | 1742,Goldbach | 部分解決(弱哥德巴赫已證,Helfgott 2013) | [深度檔案](../problems/number-theory/goldbach/README.md) |
| 孿生質數猜想(Twin Prime Conjecture) | 存在無窮多對相差 2 的質數 | 古典;1849 de Polignac 形式化 | 部分解決(無窮多對間隙 ≤ 246 已證,2013–2014) | [深度檔案](../problems/number-theory/twin-primes/README.md) |
| Collatz 猜想(Collatz Conjecture) | 反覆做「偶數除 2、奇數乘 3 加 1」最終都會到 1 | 1937,Collatz | 未解(Tao 2019 證「幾乎所有」軌道趨近有界) | [深度檔案](../problems/number-theory/collatz/README.md) |
| ABC 猜想(abc Conjecture) | 互質的 a+b=c 中,c 很少遠大於 rad(abc) | 1985,Oesterlé–Masser | ⚠️ 宣稱證明(望月新一 IUT 2012 起遭 Scholze–Stix 質疑;Joshi 2024–25 預印本亦宣稱補全,學界主流均未接受,問題實質上仍屬開放) | [Wikipedia](https://en.wikipedia.org/wiki/Abc_conjecture) |
| 奇完全數(Odd Perfect Number) | 是否存在奇數的完全數 | 古希臘(Euclid 時代已知偶完全數) | 未解(若存在必 > 10^1500,Ochem–Rao 2012) | [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number) |
| Mersenne 質數無窮性(Infinitude of Mersenne Primes) | 形如 2^p−1 的質數是否有無窮多個(合成的 Mersenne 數是否也無窮多) | 17 世紀,Mersenne | 未解(截至 2024 年 10 月已知 52 個) | [GIMPS](https://www.mersenne.org/primes/press/M136279841.html) |
| Fermat 質數(Fermat Primes) | 形如 2^(2^n)+1 的質數是否只有已知的 5 個 | 17 世紀,Fermat | 未解(F5 至 F32 皆已知為合成數) | [Wikipedia](https://en.wikipedia.org/wiki/Fermat_number) |
| Landau 四大問題(Landau's Problems) | 哥德巴赫、孿生質數、Legendre 猜想、是否有無窮多形如 n²+1 的質數 | 1912,Landau | 未解(四題全數開放;n²+1 僅知 Iwaniec 1978「至多兩個質因數」) | [Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_problems) |
| Legendre 猜想(Legendre's Conjecture) | 任意 n² 與 (n+1)² 之間必有質數 | 19 世紀初,Legendre | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_conjecture) |
| Brocard 問題(Brocard's Problem) | n!+1=m² 是否只有 n=4, 5, 7 三組解 | 1876,Brocard | 未解(大範圍驗算未見第四解) | [MathWorld](https://mathworld.wolfram.com/BrocardsProblem.html) |
| Beal 猜想(Beal Conjecture) | A^x+B^y=C^z(x,y,z>2)則 A、B、C 必有公質因數 | 1993,Beal | 未解(AMS 保管 100 萬美元懸賞) | [Wikipedia](https://en.wikipedia.org/wiki/Beal_conjecture) |
| Fermat–Catalan 猜想(Fermat–Catalan Conjecture) | a^m+b^n=c^k 在 1/m+1/n+1/k<1 下僅有有限多組解 | 1990 年代 | 未解(目前已知 10 組解) | [Wikipedia](https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture) |
| Erdős–Straus 猜想(Erdős–Straus Conjecture) | 對每個 n≥2,4/n 都能寫成三個單位分數之和 | 1948,Erdős–Straus | 未解(已驗算至極大範圍) | [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture) |
| Lehmer 猜想(Lehmer's Mahler Measure Problem) | 代數數的 Mahler 測度若大於 1,是否必 ≥ Lehmer 常數 1.17628… | 1933,Lehmer | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_conjecture) |
| Lehmer 全純商問題(Lehmer's Totient Problem) | 是否存在合成數 n 使 φ(n) 整除 n−1 | 1932,Lehmer | 未解(若存在必為極大的奇數) | [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_totient_problem) |
| Artin 原根猜想(Artin's Primitive Root Conjecture) | 非 ±1、非完全平方的整數 a 是無窮多質數的原根 | 1927,Artin | 未解(GRH 下已證,Hooley 1967;Heath-Brown 1986:至多兩個例外 a) | [Wikipedia](https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots) |
| Schanuel 猜想(Schanuel's Conjecture) | Q-線性獨立的 z₁…zₙ 使 z₁…zₙ, e^z₁…e^zₙ 的超越次數 ≥ n | 1960 年代,Schanuel | 未解(蘊涵 e+π 超越性等眾多開放問題) | [Wikipedia](https://en.wikipedia.org/wiki/Schanuel%27s_conjecture) |
| γ 的無理性(Irrationality of Euler–Mascheroni Constant) | Euler–Mascheroni 常數 γ ≈ 0.5772 是否為無理數 | 18 世紀,Euler | 未解 | [MathWorld](https://mathworld.wolfram.com/Euler-MascheroniConstant.html) |
| 奇數 ζ 值的無理性(Irrationality of ζ(5), ζ(7), …) | ζ(5) 等奇數點 zeta 值是否皆無理 | 20 世紀 | 部分解決(ζ(3) 無理,Apéry 1979;ζ(5)、ζ(7)、ζ(9)、ζ(11) 至少一個無理,Zudilin 2001) | [Wikipedia](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_theorem) |
| π 的正規性(Normality of π) | π 的十進位(或任意進位)展開是否每個數字串等頻出現 | 20 世紀 | 未解(尚無任何自然常數被證明正規) | [Wikipedia](https://en.wikipedia.org/wiki/Normal_number) |
| Cramér 猜想(Cramér's Conjecture) | 相鄰質數間隙 p_{n+1}−p_n = O((log p_n)²) | 1936,Cramér | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture) |
| Polignac 猜想(Polignac's Conjecture) | 每個偶數 2k 都是無窮多對相鄰質數之差 | 1849,de Polignac | 部分解決(存在某個 ≤ 246 的偶數成立,Zhang–Maynard–Polymath 2013–14) | [Wikipedia](https://en.wikipedia.org/wiki/Polignac%27s_conjecture) |
| Oppermann 猜想(Oppermann's Conjecture) | n²−n 與 n² 之間、n² 與 n²+n 之間各有質數 | 1882,Oppermann | 未解(強於 Legendre 猜想) | [Wikipedia](https://en.wikipedia.org/wiki/Oppermann%27s_conjecture) |
| Andrica 猜想(Andrica's Conjecture) | √p_{n+1} − √p_n < 1 對所有 n 成立 | 1986,Andrica | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Andrica%27s_conjecture) |
| Firoozbakht 猜想(Firoozbakht's Conjecture) | 數列 p_n^(1/n) 嚴格遞減 | 1982,Firoozbakht | 未解(與 Cramér 型猜想張力待釐清) | [Wikipedia](https://en.wikipedia.org/wiki/Firoozbakht%27s_conjecture) |
| Gilbreath 猜想(Gilbreath's Conjecture) | 質數列逐次取差的絕對值,每列首項皆為 1 | 1958,Gilbreath(Proth 1878 已述) | 未解(已驗算至 3×10^11 列以上) | [Wikipedia](https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture) |
| Grimm 猜想(Grimm's Conjecture) | 連續合成數可各自指派相異的質因數 | 1969,Grimm | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Grimm%27s_conjecture) |
| Carmichael 全純函數猜想(Carmichael's Totient Conjecture) | 不存在 n 使 φ(x)=φ(n) 只有唯一解 x=n | 1907,Carmichael | 未解(反例若存在必 > 10^(10^10),Ford 1998) | [Wikipedia](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function_conjecture) |
| Giuga 猜想(Giuga's Conjecture) | 1^(n−1)+2^(n−1)+…+(n−1)^(n−1) ≡ −1 (mod n) 若且唯若 n 為質數 | 1950,Giuga | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Giuga%27s_conjecture) |
| Sophie Germain 質數無窮性(Infinitude of Sophie Germain Primes) | 使 2p+1 也是質數的質數 p 是否有無窮多 | 19 世紀初,Germain | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes) |
| Wieferich 質數無窮性(Infinitude of Wieferich Primes) | 滿足 2^(p−1) ≡ 1 (mod p²) 的質數是否無窮多 | 1909,Wieferich | 未解(目前僅知 1093 與 3511) | [Wikipedia](https://en.wikipedia.org/wiki/Wieferich_prime) |
| Wall–Sun–Sun 質數存在性(Wall–Sun–Sun Primes) | 是否存在(以及是否無窮多)Wall–Sun–Sun 質數 | 1960–1992 | 未解(至今一個都沒找到) | [Wikipedia](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime) |
| 三立方和問題(Sums of Three Cubes) | 每個 n ≢ ±4 (mod 9) 是否都能寫成三個整數立方之和 | 1950 年代形式化 | 未解(33、42 於 2019 由 Booker–Sutherland 解出;100 以內僅餘表示未知者已清空,一般判定問題開放) | [Wikipedia](https://en.wikipedia.org/wiki/Sums_of_three_cubes) |
| 完美長方體(Perfect Cuboid) | 是否存在稜、面對角線、體對角線皆為整數的長方體 | 18 世紀(Euler 磚延伸) | 未解 | [MathWorld](https://mathworld.wolfram.com/PerfectCuboid.html) |
| 同餘數問題(Congruent Number Problem) | 判定哪些整數可作為有理邊直角三角形的面積 | 10 世紀阿拉伯手稿 | 未解(Tunnell 1983 在 BSD 猜想下給出完整判準) | [Wikipedia](https://en.wikipedia.org/wiki/Congruent_number) |
| BSD 猜想(Birch and Swinnerton-Dyer Conjecture) | 橢圓曲線的秩等於其 L 函數在 s=1 的消失階 | 1965,Birch–Swinnerton-Dyer | 部分解決(解析秩 0、1 情形已證,Gross–Zagier、Kolyvagin;千禧年大獎問題) | [Clay Mathematics Institute](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/) |
| Bunyakovsky 猜想(Bunyakovsky Conjecture) | 滿足自然條件的整係數不可約多項式取無窮多質數值 | 1857,Bunyakovsky | 未解(僅一次多項式情形已證,即 Dirichlet 定理;Schinzel 假設 H 為其推廣) | [Wikipedia](https://en.wikipedia.org/wiki/Bunyakovsky_conjecture) |
| Duffin–Schaeffer 猜想(Duffin–Schaeffer Conjecture) | 刻劃「幾乎所有實數」可被有理數以給定精度逼近的條件 | 1941,Duffin–Schaeffer | ✅ 已解決(2019,Koukoulopoulos–Maynard,刊於 Annals of Mathematics 2020) | [Wikipedia](https://en.wikipedia.org/wiki/Koukoulopoulos%E2%80%93Maynard_theorem) |
| Erdős 問題全集(Erdős Problems,彙總條目) | Erdős 提出的一千餘個問題(大量屬數論),集中收錄於專門資料庫,約半數仍開放 | 20 世紀,Erdős | 未解(資料庫 1200+ 題中約 46% 已解決,持續更新) | [erdosproblems.com](https://www.erdosproblems.com/) |

## 值得關注的動態

近 5 年(2021–2026)本領域已解決或有重大進展的問題:

- **Erdős–Graham 單位分數問題 ✅(2021)**:Thomas Bloom 證明任何正上密度的整數集合都含有一組倒數和恰為 1 的有限子集,解決 Erdős–Graham 問題。來源:[arXiv:2112.03726](https://arxiv.org/abs/2112.03726)。
- **Zhang 論 Landau–Siegel 零點 ⚠️(2022)**:張益唐發表預印本宣稱 L(1,χ) ≫ (log D)^(−2022)(弱於完整的「無 Siegel 零點」猜想但仍是重大宣稱);其後被指出論證有疑點,至今未通過同行評審,不能視為已確立。來源:[arXiv:2211.02515](https://arxiv.org/abs/2211.02515)、[Nature 報導](https://www.nature.com/articles/d41586-022-03689-2)。
- **Guth–Maynard 零點密度突破(2024)**:Larry Guth 與 James Maynard 改進 Dirichlet 多項式大值估計,首次實質改進 Ingham 1940 年的 ζ 零點密度上界(N(σ,T) ≤ T^(30(1−σ)/13+o(1))),並改進短區間質數定理——數十年來對黎曼猜想方向最重要的進展之一。來源:[arXiv:2405.20552](https://arxiv.org/abs/2405.20552)、[Scientific American](https://www.scientificamerican.com/article/the-riemann-hypothesis-the-biggest-problem-in-mathematics-is-a-step-closer/)。
- **Gaussian 質數猜想 ✅(2024)**:Ben Green 與 Mehtaab Sawhney 證明存在無窮多形如 p²+4q²(p、q 皆質數)的質數,解決 Friedlander–Iwaniec 的猜想,並推廣到 p²+nq² 系列。來源:[arXiv:2410.04189](https://arxiv.org/abs/2410.04189)、[Quanta Magazine](https://www.quantamagazine.org/mathematicians-uncover-a-new-way-to-count-prime-numbers-20241211/)。
- **第 52 個 Mersenne 質數(2024)**:GIMPS 於 2024 年 10 月確認 2^136279841 − 1 為質數(41,024,320 位數,Luke Durant 以雲端 GPU 叢集發現),為目前已知最大質數;Mersenne 質數無窮性本身仍未解。來源:[GIMPS 新聞稿](https://www.mersenne.org/primes/press/M136279841.html)。
- **ABC 猜想爭議持續(2024–2025)**:Kirti Joshi 發表「Arithmetic Teichmüller Spaces」系列預印本宣稱建立 abc 猜想的完整證明並回應 Scholze–Stix 的批評;望月新一拒絕其進路,學界主流亦未接受任何一方的證明,問題狀態仍為 ⚠️ 宣稱證明。來源:[arXiv:2403.10430](https://arxiv.org/abs/2403.10430)。
- **Erdős 問題資料庫與 AI 解題(2023–2025)**:erdosproblems.com 於 2023 年上線集中追蹤千餘題;2025 年起多個 AI 系統(如 Aristotle、GPT-5 系列)自主解出並以 Lean 形式化了若干開放題(如 #124、#1026),另有大量「AI 重新發現既有文獻解法」的案例,狀態逐題核實中。來源:[Terence Tao 部落格](https://terrytao.wordpress.com/2025/12/08/the-story-of-erdos-problem-126/)、[AI contributions to Erdős problems](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)。
