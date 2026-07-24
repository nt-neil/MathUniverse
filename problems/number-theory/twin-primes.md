# 孿生質數猜想(Twin Prime Conjecture)

> 相差 2 的質數對(如 11 與 13、101 與 103)是否有無窮多對?

| | |
|---|---|
| **領域** | 數論 Number Theory / 解析數論、篩法 Sieve Theory |
| **提出** | 傳統上歸於 1849 年 A. de Polignac(其猜想的 $k=2$ 特例);問題本身更古老 |
| **狀態** | 未解決(「有界質數間隙」已於 2013–2014 年證明) |
| **懸賞** | 無官方懸賞 |

## 問題陳述

**直觀版**:質數越往後越稀疏(平均間隔約 $\ln p$),但似乎總會不時出現「緊貼在一起」、只差 2 的質數對。猜想說這種質數對永遠不會用完。

**正式版**:
$$\#\{p \text{ 質數} : p + 2 \text{ 也是質數}\} = \infty$$
等價地,令 $p_n$ 為第 $n$ 個質數,則 $\liminf_{n\to\infty}(p_{n+1} - p_n) = 2$。

**定量版(Hardy–Littlewood 第一猜想)**:$x$ 以下的孿生質數對數 $\pi_2(x) \sim 2C_2 \int_2^x \frac{dt}{(\ln t)^2}$,其中 $C_2 \approx 0.6601618$ 為孿生質數常數。數值資料與此預測吻合極佳。

**推廣(de Polignac)**:對每個偶數 $2k$,有無窮多對相差 $2k$ 的相鄰質數。

## 背景與重要性

這是「質數的加法結構」最純粹的測試題之一,與哥德巴赫猜想同屬 Hardy–Littlewood 質數 $k$-元組猜想(prime $k$-tuples conjecture)的特例。2013 年張益唐(Yitang Zhang)的突破首次證明質數間隙有界,是本世紀數論最著名的進展之一,隨後 Maynard 與 Polymath 計畫在一年內把界從 7000 萬壓到 246——這段歷史也成為大規模網路協作數學(Polymath)的代表案例。發展出的 GPY/Maynard–Tao 多維篩法已成為研究質數分布的標準工具。

## 目前狀態

截至 2026 年 7 月:未解決。已知:

- **有界間隙(unconditional)**:存在 $H \le 246$ 使得有無窮多對相鄰質數相差 $\le H$(Polymath8b,2014)。**246 仍是學界接受的最佳無條件上界**(見 [Polymath wiki 紀錄頁](https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes));網路上時有宣稱改進(如壓到 234)的預印本,均未經同行評審、未被接受。
- **條件結果**:在廣義 Elliott–Halberstam 猜想(GEH)下,界可壓到 6;即使 GEH 全部成立,現有方法也到不了 2(宇稱問題的障礙)。
- **Chen 定理(1973)**:有無窮多質數 $p$ 使 $p+2$ 至多有兩個質因子。
- **函數體類比已證**:在 $\mathbb{F}_q[T]$($q$ 夠大)中,孿生質數猜想的類比成立(Sawin–Shusterman,2019)。
- **最大已知孿生質數對**:$2996863034895 \times 2^{1290000} \pm 1$(388,342 位數,PrimeGrid,2016;[官方公告 PDF](https://www.primegrid.com/download/twin-1290000.pdf),截至查證時仍是紀錄,見 [t5k 排行榜](https://t5k.org/top20/page.php?id=1))。

卡在哪裡:從 246 到 2 不是「再優化一點」的問題。多維篩法有已知的理論極限(即使假設最強的分布猜想也只能到 6),而「恰好差 2」需要突破宇稱問題——目前沒有任何方法看得到路。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1849 | de Polignac 提出推廣猜想 | A. de Polignac |
| 1919 | Brun 定理:孿生質數倒數和收斂(Brun 常數 $\approx 1.9022$)——孿生質數即使無窮也很稀疏 | V. Brun |
| 1973 | 無窮多 $p$ 使 $p+2 = P_2$ | 陳景潤 Chen Jingrun |
| 2005 | GPY:相鄰質數間隙可遠小於平均($\liminf \frac{p_{n+1}-p_n}{\ln p_n} = 0$) | D. Goldston, J. Pintz, C. Yıldırım |
| 2013 | **首次證明有界間隙**:$H \le 70{,}000{,}000$(Annals of Mathematics) | 張益唐 Yitang Zhang |
| 2013 | 多維篩法,獨立給出 $H \le 600$;且證明任意長度的質數「叢集」有界([arXiv:1311.4600](https://arxiv.org/abs/1311.4600)) | J. Maynard |
| 2014 | Polymath8b:$H \le 246$(無條件);GEH 下 $H \le 6$([arXiv:1407.4897](https://arxiv.org/abs/1407.4897)) | D. H. J. Polymath(Tao 主持) |
| 2016 | 最大已知孿生質數對(388,342 位數) | PrimeGrid / T. Greer |
| 2019 | 函數體版本的孿生質數猜想($\mathbb{F}_q[T]$,$q$ 大)獲證 | W. Sawin, M. Shusterman |
| 2024 | Guth–Maynard 的 Dirichlet 多項式大值估計改進短區間質數分布([arXiv:2405.20552](https://arxiv.org/abs/2405.20552));是質數間隙領域的重要工具進展,但**未**改動 246 這個界 | L. Guth, J. Maynard |
| 2025–2026 | 無被接受的界限改進;領域持續活躍(如 AIM 持續舉辦 [bounded gaps between primes 工作坊](https://aimath.org/workshops/upcoming/primegaps2/)) | — |

## 主要研究方法

- **多維篩法(GPY → Maynard–Tao)**:對 admissible tuple 設計權重,證明區間內「至少兩個質數」。現行紀錄 246 的來源;已知即使在最優化下也碰不到 2。
- **質數分布水平(level of distribution)**:Zhang 的突破在於對光滑模數突破 Bombieri–Vinogradov 的 1/2 水平;進一步提高水平(Elliott–Halberstam 方向)是壓低界的主要槓桿。
- **宇稱問題研究**:篩法無法區分質因子個數奇偶,是「到 2」的本質障礙;尋找繞過宇稱的雙線性結構(如 Friedlander–Iwaniec 型定理)是長期方向。
- **函數體與類比模型**:Sawin–Shusterman 在多項式環中的成功說明類比世界裡障礙可以被幾何工具(如 monodromy)繞過,啟發但尚不能移植回整數。

## AI 可以怎麼幫忙

- **形式化**:猜想**陳述**在 Lean 4 / Mathlib 中一行可寫(`∀ n, ∃ p > n, p.Prime ∧ (p+2).Prime`);Mathlib 已有充足的質數與篩法前置(如 Selberg 篩的部分工作),但 Zhang/Maynard 證明的完整形式化尚無公開完成的專案。把「無窮多質數」「Brun 定理」等前置在 Lean 中重建是務實切入點。
- **機器學習/LLM**:無已被認可的直接貢獻;Polymath8 的歷史顯示這領域的進展形式(大規模協作優化 + 關鍵理論突破)其實適合工具輔助——當年的界限優化就依賴大量計算搜索(admissible tuples 的搜索)。
- **本 repo 可做的事**:
  - 重現 Polymath8 的 admissible $k$-tuple 搜索(給定 $k$ 找最窄的可容許組),這是有明確答案可對的計算問題;
  - 計算 $\pi_2(x)$ 並與 Hardy–Littlewood 常數預測作圖比對;
  - 追蹤 246 界的文獻動態,維護「宣稱改進 vs. 實際被接受」的誠實清單;
  - 在 Lean 中形式化猜想陳述與 Brun 定理的陳述,標記證明缺口。

## 關鍵文獻與資源

- Zhang, *Bounded gaps between primes*, Annals of Mathematics 179 (2014)
- Maynard, *Small gaps between primes*(2013):https://arxiv.org/abs/1311.4600
- Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes*(2014):https://arxiv.org/abs/1407.4897
- Polymath wiki(界限演進的完整紀錄):https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes
- Polymath 計畫回顧:*The "bounded gaps between primes" Polymath project — a retrospective*:https://arxiv.org/abs/1409.8361
- t5k 孿生質數紀錄排行榜:https://t5k.org/top20/page.php?id=1
