# 組合與圖論 Combinatorics & Graph Theory 未解難題目錄

> 收錄組合數學(含極值組合、加法組合、組合機率)與圖論的著名未解問題,以及 2019 年以來新解決的重要問題。本領域近年進展極快,狀態均逐題查證至 2026 年中。

**主要來源**:
- [Wikipedia: List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)(Combinatorics / Graph theory 段)
- [Open Problem Garden](http://www.openproblemgarden.org/)(圖論問題大宗)
- [erdosproblems.com](https://www.erdosproblems.com/)(Erdős 問題資料庫,Thomas Bloom 維護)
- [Gil Kalai: Combinatorics and more](https://gilkalai.wordpress.com/)(近年突破的即時報導)

## 難題清單

### 組合(含加法組合)

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Ramsey 數 R(5,5)(Ramsey number R(5,5)) | 最小的 n 使任意紅藍著色 K_n 必含單色 K_5;目前只知 43 ≤ R(5,5) ≤ 46 | 1930 年代起 | 未解(上界 2024 年降至 46,Angeltveit–McKay) | [arXiv:2409.15709](https://arxiv.org/abs/2409.15709) |
| 對角 Ramsey 數漸近(Diagonal Ramsey asymptotics) | R(k,k) 的增長率為何?下界約 √2^k、上界 (4−ε)^k,中間差距仍是指數級 | 1935 Erdős–Szekeres | 未解(上下界 2023、2025 各有指數級改進,見動態) | [arXiv:2303.09521](https://arxiv.org/abs/2303.09521) |
| 聯集封閉集合猜想(Frankl's union-closed sets conjecture) | 任何有限聯集封閉集合族,必有某元素出現在至少一半的集合中 | 1979 Frankl | 部分解決(常數 ≈0.3823 已證,1/2 未達;見動態) | [Wikipedia](https://en.wikipedia.org/wiki/Union-closed_sets_conjecture) |
| 向日葵猜想(Sunflower conjecture) | k 元集合族只要大小超過 C^k(某常數 C)就必含 3 瓣向日葵 | 1960 Erdős–Rado | 未解(2019 Alweiss–Lovett–Wu–Zhang 把界改進到 (O(k log k))^k) | [Wikipedia](https://en.wikipedia.org/wiki/Sunflower_%28mathematics%29) |
| Erdős 等差數列猜想(Erdős conjecture on arithmetic progressions) | 倒數和發散的正整數集合必含任意長等差數列 | 1936/1970s Erdős–Turán | 部分解決(k=3 由 Bloom–Sisask 2020 證得;一般 k 未解) | [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s_conjecture_on_arithmetic_progressions) |
| Cap set 增長常數(Cap set growth constant) | F_3^n 中無三點共線集合的最大增長率 c(2.2202 ≤ c ≤ 2.756)確切值為何 | 1984 起 | 未解(上界 Ellenberg–Gijswijt 2016;下界 2023 由 FunSearch 改進) | [Wikipedia](https://en.wikipedia.org/wiki/Cap_set) |
| 無三點共線問題(No-three-in-line problem) | n×n 格點中最多能放幾個點使任三點不共線?能否對所有大 n 放到 2n 點 | 1917 Dudeney | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/No-three-in-line_problem) |
| 孤獨跑者猜想(Lonely runner conjecture) | 環形跑道上 k 個等速相異的跑者,每人都有某時刻與其他人距離 ≥ 1/k | 1967 Wills | 部分解決(k ≤ 7 已證) | [Wikipedia](https://en.wikipedia.org/wiki/Lonely_runner_conjecture) |
| Sidorenko 猜想(Sidorenko's conjecture) | 任何二部圖 H 在稠密圖中的同態密度不低於隨機圖的期望值 | 1993 Sidorenko | 部分解決(多類二部圖已證,一般情形未解) | [Wikipedia](https://en.wikipedia.org/wiki/Sidorenko%27s_conjecture) |
| 1/3–2/3 猜想(1/3–2/3 conjecture) | 任何非全序偏序集必有一對元素,其先後順序在線性擴張中的比例介於 1/3 與 2/3 之間 | 1968 Kislitsyn | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture) |
| Dedekind 數(Dedekind numbers) | 計算 n 變數單調布林函數個數 D(n);目前只算到 D(9) | 1897 Dedekind | 部分解決(D(9) 於 2023 由兩組獨立算出;一般公式未解) | [Wikipedia](https://en.wikipedia.org/wiki/Dedekind_number) |
| 敏感度猜想(Sensitivity conjecture) | 布林函數的敏感度與其他複雜度度量(度數、塊敏感度)多項式等價 | 1992 Nisan–Szegedy | ✅ 已解決(2019,Huang 兩頁證明,Annals of Math.) | [arXiv:1907.00847](https://arxiv.org/abs/1907.00847) |
| Marton 猜想/多項式 Freiman–Ruzsa(Polynomial Freiman–Ruzsa / Marton's conjecture) | 加倍常數小的集合可被多項式多個陪集覆蓋(有界撓群情形) | 1999 頃 Marton | ✅ 已解決(2023,Gowers–Green–Manners–Tao) | [arXiv:2311.05762](https://arxiv.org/abs/2311.05762) |
| Kahn–Kalai 猜想(Kahn–Kalai / expectation threshold conjecture) | 隨機結構的真實門檻與期望門檻至多差一個對數因子 | 2006 Kahn–Kalai | ✅ 已解決(2022,Park–Pham) | [arXiv:2203.17207](https://arxiv.org/abs/2203.17207) |
| Erdős 問題全集(Erdős problems,彙總條目) | Erdős 生前提出的上千個懸賞與非懸賞問題;資料庫現收 1,200+ 題,約 46% 已解 | Erdős(1930s–1996) | 未解(彙總;個別問題持續被解決) | [erdosproblems.com](https://www.erdosproblems.com/) |

### 圖論

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Hadwiger 猜想(Hadwiger conjecture) | 無 K_t minor 的圖可用 t−1 色著色 | 1943 Hadwiger | 未解(t ≤ 6 已證;最佳一般界 O(t log log t) 色,Delcourt–Postle 2021;odd 變體 2025 被否定,見動態) | [Wikipedia](https://en.wikipedia.org/wiki/Hadwiger_conjecture_%28graph_theory%29) |
| 重構猜想(Reconstruction conjecture) | 每個 ≥3 頂點的圖可由其所有單頂點刪除子圖(deck)唯一重構 | 1941 Kelly–Ulam | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Reconstruction_conjecture) |
| 圈雙重覆蓋猜想(Cycle double cover conjecture) | 每個無橋圖都有一組圈,使每條邊恰被覆蓋兩次 | 1973/1979 Szekeres、Seymour | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Cycle_double_cover) |
| Barnette 猜想(Barnette's conjecture) | 每個 3-連通 3-正則二部平面圖都有 Hamilton 圈 | 1969 Barnette | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Barnette%27s_conjecture) |
| Erdős–Gyárfás 猜想(Erdős–Gyárfás conjecture) | 最小度數 ≥ 3 的圖必含長度為 2 的冪的圈 | 1994 Erdős–Gyárfás | 未解(最小度數夠大時成立,Liu–Montgomery;P₁₃-free 等特例已證) | [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture) |
| Erdős–Hajnal 猜想(Erdős–Hajnal conjecture) | 禁止任一固定誘導子圖 H 的圖,必含多項式大小的團或獨立集 | 1977/1989 Erdős–Hajnal | 部分解決(所有 ≤5 頂點的 H 已證,含 P₅,Nguyen–Scott–Seymour 2023;一般未解) | [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Hajnal_conjecture) |
| 1-因子分解猜想(1-factorization conjecture) | 偶數 n 頂點、最小度數 ≥ 2⌈n/4⌉−1 的正則圖可作 1-因子分解 | 1985 Chetwynd–Hilton(溯及 Dirac) | 部分解決(充分大 n 已證,Csaba–Kühn–Lo–Osthus–Treglown 2016) | [Wikipedia](https://en.wikipedia.org/wiki/1-factorization) |
| 優美標號猜想(Graceful tree conjecture, Ringel–Kotzig) | 每棵樹都有優美標號 | 1967 Ringel、Kotzig、Rosa | 未解(相關的 Ringel 猜想已於 2020 對大 n 證得,Montgomery–Pokrovskiy–Sudakov) | [Wikipedia](https://en.wikipedia.org/wiki/Graceful_labeling) |
| Seymour 第二鄰域猜想(Second neighborhood conjecture) | 每個無 2-圈有向圖必有一頂點,其二步鄰域不小於一步鄰域 | 1990 頃 Seymour | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Second_neighborhood_problem) |
| Tutte 5-流猜想(Tutte's 5-flow conjecture) | 每個無橋圖都有處處非零的 5-流 | 1954 Tutte | 未解(6-流已證,Seymour 1981) | [Wikipedia](https://en.wikipedia.org/wiki/Nowhere-zero_flow) |
| 全著色猜想(Total coloring conjecture) | 任何圖的全著色數至多 Δ+2 | 1964–65 Vizing、Behzad | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Total_coloring) |
| Erdős–Faber–Lovász 猜想(Erdős–Faber–Lovász conjecture) | n 個兩兩至多交於一點的 K_n 之聯集可用 n 色著色 | 1972 Erdős–Faber–Lovász | 部分解決(充分大 n 已證,Kang–Kelly–Kühn–Methuku–Osthus 2021,刊於 Annals 2023) | [arXiv:2101.04698](https://arxiv.org/abs/2101.04698) |
| Ryser–Brualdi–Stein 猜想(Ryser–Brualdi–Stein conjecture) | 每個 n 階拉丁方陣含大小 n−1 的部分橫截線(n 奇數時含完整橫截線) | 1967 起 Ryser、Brualdi、Stein | 部分解決(充分大 n 的 n−1 情形已證,Montgomery 2023) | [arXiv:2310.19779](https://arxiv.org/abs/2310.19779) |
| Oberwolfach 問題(Oberwolfach problem) | K_n(n 奇數)能否分解成任意指定的 2-正則圖的拷貝 | 1967 Ringel | 部分解決(充分大 n 已證,Glock–Joos–Kim–Kühn–Osthus 2021) | [arXiv:1806.04644](https://arxiv.org/abs/1806.04644) |
| 等角線問題(Equiangular lines with a fixed angle) | 固定夾角下,高維空間中等角線的最大條數 | 1966 起 | ✅ 已解決(2021,Jiang–Tidor–Yao–Zhang–Zhao,Annals of Math.) | [arXiv:1907.12466](https://arxiv.org/abs/1907.12466) |
| Hedetniemi 猜想(Hedetniemi's conjecture) | 兩圖張量積的色數等於兩者色數的較小值 | 1966 Hedetniemi | ✅ 已解決(2019,Shitov 反例否定,Annals of Math.) | [arXiv:1905.02167](https://arxiv.org/abs/1905.02167) |
| 雙層床猜想(Bunkbed conjecture) | 滲流模型中,雙層床圖內同層兩點連通機率不低於跨層兩點 | 1985 Kasteleyn | ✅ 已解決(2024,Gladkov–Pak–Zimin 反例否定) | [arXiv:2410.02545](https://arxiv.org/abs/2410.02545) |

## 值得關注的動態

近 5 年(2021–2026)本領域進展密集,以下逐條附來源:

- **2023|三項等差數列的 Kelley–Meka 突破**:Kelley–Meka 證明無 3-AP 集合大小至多 N·exp(−Ω((log N)^{1/12})),首度逼近 Behrend 型界,被視為加法組合十年來最大突破;Bloom–Sisask 隨後把指數改進到 1/9,並確認了無 3-AP 密度的準多項式上界。來源:[arXiv:2302.07211](https://arxiv.org/abs/2302.07211)、[arXiv:2309.02353](https://arxiv.org/abs/2309.02353)、[Gil Kalai 報導](https://gilkalai.wordpress.com/2023/02/14/absolutely-sensational-morning-news-zander-kelley-and-raghua-meka-proved-behrend-type-bounds-for-3aps/)。
- **2023–2025|Ramsey 數上下界雙雙指數級改進**:Campos–Griffiths–Morris–Sahasrabudhe 證明 R(k) ≤ (4−ε)^k,是 1935 年 Erdős–Szekeres 上界後首次指數級改進(刊於 [Annals of Math. 203, 2026](https://projecteuclid.org/journals/annals-of-mathematics/volume-203/issue-3/An-exponential-improvement-for-diagonal-Ramsey/10.4007/annals.2026.203.3.4.short),[arXiv:2303.09521](https://arxiv.org/abs/2303.09521));2025 年 Ma–Shen–Xie 又給出 1947 年 Erdős 下界後首次指數級改進(刊於 Inventiones,[arXiv:2507.12926](https://arxiv.org/abs/2507.12926))。小 Ramsey 數方面,Angeltveit–McKay 2024 證明 R(5,5) ≤ 46([arXiv:2409.15709](https://arxiv.org/abs/2409.15709));非對角情形 r(4,t) 的漸近由 Mattheus–Verstraëte 2023 確定([arXiv:2306.04007](https://arxiv.org/abs/2306.04007))。
- **2022–2023|聯集封閉集合猜想的常數突破**:Gilmer 用資訊論方法首次給出常數下界 0.01([arXiv:2211.09055](https://arxiv.org/abs/2211.09055));數週內多組人馬(Alweiss–Huang–Sellke、Chase–Lovett、Sawin、Pebody)推進到 (3−√5)/2 ≈ 0.38197,Sawin 與 Yu 再微幅超越至 ≈0.38234;完整的 1/2 仍未解。來源:[Gil Kalai 報導](https://gilkalai.wordpress.com/2022/11/17/amazing-justin-gilmer-gave-a-constant-lower-bound-for-the-union-closed-sets-conjecture/)、[arXiv:2212.00658](https://arxiv.org/abs/2212.00658)。
- **2023|Marton 猜想(多項式 Freiman–Ruzsa)獲證**:Gowers–Green–Manners–Tao 以熵方法解決加法組合的「聖杯」級猜想,後續並被完整形式化為 Lean 證明。來源:[arXiv:2311.05762](https://arxiv.org/abs/2311.05762)、[Tao 部落格](https://terrytao.wordpress.com/2023/11/13/on-a-conjecture-of-marton/)。
- **2022|Kahn–Kalai 期望門檻猜想獲證**:Park–Pham 以出人意料的短證明解決隨機圖與滲流門檻的核心猜想。來源:[arXiv:2203.17207](https://arxiv.org/abs/2203.17207)、[IAS 報導](https://www.ias.edu/news/park-and-pham-prove-kahn-kalai-conjecture)。
- **2023|Erdős–Hajnal 猜想的 P₅ 情形獲證**:Nguyen–Scott–Seymour 解決最小的懸而未決情形,補齊所有 5 頂點圖(C₅ 情形由 Chudnovsky–Scott–Seymour–Spirkl 於 2021 完成);刊於 Proc. LMS 2026。來源:[arXiv:2312.15333](https://arxiv.org/abs/2312.15333)。
- **2024|雙層床猜想被否定**:Gladkov–Pak–Zimin 以 7,222 頂點平面圖反例推翻 1985 年 Kasteleyn 的滲流猜想(建立在 Hollom 的超圖反例上)。來源:[arXiv:2410.02545](https://arxiv.org/abs/2410.02545)、[Quanta 報導](https://www.quantamagazine.org/maths-bunkbed-conjecture-has-been-debunked-20241101/)。
- **2025|Odd Hadwiger 猜想被否定(預印本)**:Kühn–Sauermann–Steiner–Wigderson 構造無 K_t odd minor 但色數達 (3/2−o(1))t 的圖,推翻 Gerards–Seymour 1993 的 odd 變體;原 Hadwiger 猜想不受影響。預印本,尚待審查。來源:[arXiv:2512.20392](https://arxiv.org/abs/2512.20392)。
- **2021–2023|大 n 情形的系列突破(吸收法/迭代吸收)**:Erdős–Faber–Lovász 猜想(Kang–Kelly–Kühn–Methuku–Osthus,[Annals 2023](https://arxiv.org/abs/2101.04698))、Oberwolfach 問題(Glock–Joos–Kim–Kühn–Osthus,[arXiv:1806.04644](https://arxiv.org/abs/1806.04644))、Ryser–Brualdi–Stein 猜想(Montgomery 2023,[arXiv:2310.19779](https://arxiv.org/abs/2310.19779))均對充分大 n 獲證。
- **2021|等角線問題解決**:Jiang–Tidor–Yao–Zhang–Zhao 完全確定固定夾角下高維等角線最大數,刊於 Annals。來源:[arXiv:1907.12466](https://arxiv.org/abs/1907.12466)。
- **2023|AI 輔助的新下界**:DeepMind 的 FunSearch(LLM+演化搜尋)找到 8 維 512 點的 cap set(舊紀錄 496)並改進 cap set 容量下界至 2.2202,刊於 Nature。來源:[Nature 論文](https://www.nature.com/articles/s41586-023-06924-6)。
- **2023|D(9) 算出**:第 9 個 Dedekind 數由兩組團隊(Jäkel;Van Hirtum 等,FPGA 超算)獨立算出,為 42 位數。來源:[Wikipedia: Dedekind number](https://en.wikipedia.org/wiki/Dedekind_number)。
- **2023–|erdosproblems.com 成為活資料庫**:Bloom 建立的 Erdős 問題資料庫已收 1,200+ 題、約 46% 標記已解,並與 Lean 形式化及 AI 求解實驗(2025 年底起多題由 AI 給出被接受的證明)互動,成為追蹤本領域動態的一手來源。來源:[erdosproblems.com](https://www.erdosproblems.com/)。
