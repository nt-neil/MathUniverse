# 計算與複雜度(Computation & Complexity)未解難題目錄

> 計算複雜度理論與演算法的核心未解問題:複雜度類分離、電路下界、細粒度複雜度、量子計算與 meta-complexity,兼收若干著名演算法猜想。

**主要來源**:
- Wikipedia [List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)
- [Complexity Zoo](https://complexityzoo.net/)、Simons Institute [Meta-Complexity 開放問題清單](https://wiki.simons.berkeley.edu/lib/exe/fetch.php?media=mc23%3A91meta-complexity_open-problems.pdf)
- Scott Aaronson 部落格([Shtetl-Optimized](https://scottaaronson.blog/))

## 難題清單

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| P vs NP(P versus NP) | 可快速驗證解的問題是否都能快速求解? | 1971 Cook / 1973 Levin | 未解 | [深度檔案](../problems/millennium/p-vs-np/README.md) |
| NP vs coNP(NP versus coNP) | 有短證明的問題,其否定是否也有短證明?(否則 P≠NP) | 1970 年代 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Co-NP) |
| P vs PSPACE(P versus PSPACE) | 多項式空間可解的問題是否都能多項式時間解?兩者間整條層級(NP、PH)無一分離 | 1970 年代 | 未解(2025 Williams 時間-空間模擬 TIME[t]⊆SPACE[√(t log t)] 為 50 年來首次實質進展) | [Williams 2025](https://people.csail.mit.edu/rrw/time-vs-space.pdf) |
| PH vs PSPACE(PH versus PSPACE) | 多項式層級是否嚴格包含於 PSPACE? | 1976 Stockmeyer | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_hierarchy) |
| P vs BPP:去隨機化(Derandomization) | 隨機演算法是否都可去隨機化,即 P = BPP? | 1977 Gill 定義 BPP;1997 Impagliazzo–Wigderson 條件性結果 | 未解(普遍相信 P=BPP;已知由夠強電路下界可推出) | [Wikipedia](https://en.wikipedia.org/wiki/BPP_(complexity)) |
| NC vs P(NC versus P) | 所有多項式時間可解問題都能高效平行化嗎? | 1979 Cook 等 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/NC_(complexity)) |
| L vs P、L vs NL | 對數空間是否嚴格弱於多項式時間?確定性與非確定性對數空間是否相等? | 1970 年代 | 未解(2024 Cook–Mertz 樹評估演算法動搖了以 Tree Evaluation 分離 L 與 P 的路線) | [Wikipedia](https://en.wikipedia.org/wiki/L_(complexity)) |
| BQP 與 NP、PH 的關係(BQP versus NP/PH) | 量子多項式時間與 NP、多項式層級誰包含誰?(已知均無包含關係的證據:2018 Raz–Tal 給出 oracle 分離 BQP⊄PH) | 1993 Bernstein–Vazirani | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/BQP) |
| 電路下界:NP ⊄ P/poly | NP 問題是否需要超多項式大小的布林電路?(可推出 P≠NP) | 1980 Karp–Lipton | 未解(已知最佳一般電路下界仍僅約 3.1n 線性) | [Wikipedia](https://en.wikipedia.org/wiki/P/poly) |
| VP vs VNP:Valiant 猜想(Valiant's Conjecture) | 代數版 P vs NP:permanent 是否需要超多項式大小的算術電路? | 1979 Valiant | 未解(2021 Limaye–Srinivasan–Tavenas 證得常數深度代數電路超多項式下界) | [ECCC 2021](https://eccc.weizmann.ac.il/report/2021/081/) |
| 唯一賽局猜想(Unique Games Conjecture) | Unique Games 的近似是否 NP-hard?(決定大量近似演算法的最優性) | 2002 Khot | 未解(2018 Khot–Minzer–Safra 證明 2-to-2 定理,即「半個 UGC」) | [Wikipedia](https://en.wikipedia.org/wiki/Unique_games_conjecture) |
| 指數時間假設 ETH(Exponential Time Hypothesis) | 3-SAT 是否需要 2^Ω(n) 時間?(強於 P≠NP) | 1999–2001 Impagliazzo–Paturi(–Zane) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Exponential_time_hypothesis) |
| 強指數時間假設 SETH(Strong ETH) | k-SAT 的複雜度是否隨 k 趨近 2^n?(細粒度複雜度的核心假設) | 2001 Impagliazzo–Paturi | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Exponential_time_hypothesis#Strong_exponential_time_hypothesis) |
| 圖同構複雜度(Graph Isomorphism) | 圖同構是否在 P?(不太可能 NP-complete) | 1972 Karp 列為開放 | 未解(2016–17 Babai 準多項式時間演算法,經修正後被接受) | [Wikipedia](https://en.wikipedia.org/wiki/Graph_isomorphism_problem) |
| 整數分解與離散對數(Integer Factorization / Discrete Log) | 古典電腦能否多項式時間分解整數、算離散對數?(量子已可:1994 Shor) | 古典問題;複雜度形式 1970 年代 | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Integer_factorization) |
| 格問題複雜度(Lattice Problems, SVP/LWE) | 最短向量等格問題的真實難度為何?量子電腦能否攻破?(後量子密碼的基石) | 1981 van Emde Boas;1996 Ajtai | 未解(2024 Y. Chen 宣稱之多項式時間量子 LWE 演算法發現錯誤後已撤回) | [Wikipedia](https://en.wikipedia.org/wiki/Lattice_problem) |
| 單向函數存在性(One-Way Functions) | 是否存在易算難逆的函數?(現代密碼學的最低假設;2020 Liu–Pass 證其等價於時間限定 Kolmogorov 複雜度的平均難度) | 1976 年代(Diffie–Hellman 後) | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/One-way_function) |
| 最小電路大小問題 MCSP(Minimum Circuit Size Problem) | 「給定真值表,求最小電路」是否 NP-complete?(meta-complexity 核心開放題) | 1950 年代蘇聯 Perebor 傳統;2000 Kabanets–Cai | 未解(2022 Hirahara 證部分函數版 MCSP* 為 NP-hard) | [Hirahara, FOCS 2022](https://eccc.weizmann.ac.il/report/2022/119/) |
| 矩陣乘法指數(Matrix Multiplication Exponent, ω=2?) | 兩個 n×n 矩陣能否以 n^{2+o(1)} 時間相乘? | 1969 Strassen | 未解(現況 ω < 2.371339,2024;已知雷射法無法達到 2) | [Wikipedia](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication) |
| 對數秩猜想(Log-Rank Conjecture) | 布林矩陣的確定性通訊複雜度是否被 rank 的 polylog 所界定? | 1988 Lovász–Saks | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Log-rank_conjecture) |
| Hartmanis–Stearns 猜想 | 實時(線性時間)Turing 機算出的無理數必為超越數? | 1965 Hartmanis–Stearns | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Hartmanis%E2%80%93Stearns_conjecture) |
| 動態最優性猜想(Dynamic Optimality Conjecture) | Splay tree 是否為動態最優的二元搜尋樹(競爭比 O(1))? | 1985 Sleator–Tarjan | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Splay_tree#Dynamic_optimality_conjecture) |
| k-server 猜想(k-Server Conjecture) | 任意度量空間上 k-server 問題是否存在競爭比恰為 k 的確定性演算法? | 1990 Manasse–McGeoch–Sleator | 部分解決(確定性版仍開放;隨機化版 O(log k) 猜想 2023 被否證) | [Wikipedia](https://en.wikipedia.org/wiki/K-server_problem) |
| 細粒度複雜度:3SUM 與 APSP(Fine-Grained: 3SUM / APSP) | 3SUM 能否真正次二次時間?全點對最短路徑能否真正次三次時間? | 1995 Gajentaan–Overmars;APSP 猜想 2010 年代 | 未解(3SUM 已有 n²/polylog 的改進,但次二次仍未知) | [Wikipedia](https://en.wikipedia.org/wiki/3SUM) |
| 線性規劃強多項式演算法(Strongly Polynomial LP) | 線性規劃是否有與位元長度無關的強多項式時間演算法?(Smale 第 9 問) | 1998 Smale | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_problems) |
| 奇偶賽局求解(Parity Games in P) | 奇偶賽局(在 NP∩coNP 中)能否多項式時間求解? | 1991 Emerson–Jutla / Mostowski | 未解(2017 Calude 等給出準多項式時間演算法) | [Wikipedia](https://en.wikipedia.org/wiki/Parity_game) |
| 量子 PCP 猜想(Quantum PCP Conjecture) | 估計局部 Hamiltonian 基態能量到常數精度是否 QMA-hard?(PCP 定理的量子類比) | 約 2006(Aharonov 等形式化) | 未解(2022 NLTS 定理證得必要條件) | [Aharonov–Arad–Vidick 綜述](https://arxiv.org/abs/1309.7495) |

## 值得關注的動態

近 5 年(2021–2026)已解決或有重大進展的問題:

- **時間-空間模擬突破(2025)**:R. Williams 證明 TIME[t] ⊆ SPACE[√(t log t)],大幅改進 1975 年 Hopcroft–Paul–Valiant 的 t/log t 界,獲 STOC 2025 最佳論文;並由此得到明確的「O(n) 空間可解但需 n²/polylog 時間」問題,是 P vs PSPACE 五十年來的一小步。[論文](https://people.csail.mit.edu/rrw/time-vs-space.pdf)、[Aaronson 評介](https://scottaaronson.blog/?p=8680)
- **樹評估問題近乎進 L(2024)**:J. Cook 與 I. Mertz 證明 Tree Evaluation 可在 O(log n·log log n) 空間解決(STOC 2024),推翻其為分離 L 與 P 候選難例的預期,且為上述 Williams 2025 結果的關鍵工具。[論文](https://dl.acm.org/doi/10.1145/3618260.3649664)
- **矩陣乘法指數連續改進(2024)**:Vassilevska Williams–Xu–Xu–Zhou(SODA 2024)將 ω 降到 2.371552,隨後 Alman–Duan–Vassilevska Williams–Xu–Xu–Zhou 進一步降到 ω < 2.371339,為現今最佳界。[arXiv:2307.07970](https://arxiv.org/abs/2307.07970)、[arXiv:2404.16349](https://arxiv.org/abs/2404.16349)
- **✅ 隨機化 k-server 猜想被否證(2023)**:Bubeck–Coester–Rabani 構造出隨機化競爭比 Ω(log²k) 的度量空間,推翻「所有度量空間皆 Θ(log k)」的猜想(STOC 2023);確定性 k-server 猜想仍開放。[arXiv:2211.05753](https://arxiv.org/abs/2211.05753)
- **部分函數 MCSP 為 NP-hard(2022)**:Hirahara 證明 MCSP*、MKTP* 等部分函數版 meta-complexity 問題在隨機化歸約下 NP-hard(FOCS 2022),突破長期的歸約障礙;全函數 MCSP 是否 NP-complete 仍開放。[ECCC 2022/119](https://eccc.weizmann.ac.il/report/2022/119/)
- **常數深度代數電路超多項式下界(2021)**:Limaye–Srinivasan–Tavenas 首次對特徵 0 域上所有常數深度的一般代數電路證得超多項式下界(FOCS 2021 最佳論文),是 VP vs VNP 方向數十年來最大進展。[ECCC 2021/081](https://eccc.weizmann.ac.il/report/2021/081/)
- **NLTS 定理(2022)**:Anshu–Breuckmann–Nirkhe 證明 No Low-energy Trivial States 猜想,掃除量子 PCP 猜想的一個必要障礙(STOC 2023)。[arXiv:2206.13228](https://arxiv.org/abs/2206.13228)
- **⚠️ 量子破格演算法宣稱撤回(2024)**:Y. Chen 於 2024 年 4 月宣稱多項式時間量子演算法解 LWE 格問題,一週後被 Wu 與 Vidick 發現第 9 步錯誤,作者已撤回宣稱;後量子密碼假設目前安然無恙。[ePrint 2024/555](https://eprint.iacr.org/2024/555)、[Aaronson 評介](https://scottaaronson.blog/?p=7946)
- **量子分解電路改進(2023)**:Regev 提出多維版 Shor 演算法,將分解 n 位元整數的量子電路門數自 Õ(n²) 降至 Õ(n^{1.5})(古典複雜度仍未知)。[arXiv:2308.06572](https://arxiv.org/abs/2308.06572)
