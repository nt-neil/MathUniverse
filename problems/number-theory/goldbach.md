# 哥德巴赫猜想(Goldbach's Conjecture)

> 每個大於 2 的偶數,都能寫成兩個質數之和嗎?

| | |
|---|---|
| **領域** | 數論 Number Theory / 加法數論 Additive Number Theory |
| **提出** | 1742 年,Christian Goldbach 與 Euler 通信中提出 |
| **狀態** | 未解決(「弱哥德巴赫猜想」已於 2013 年被證明) |
| **懸賞** | 無現行官方懸賞(2000 年 Faber 出版社曾懸賞 100 萬美元,已過期) |

## 問題陳述

**直觀版**:隨便挑一個偶數,例如 $28 = 5 + 23 = 11 + 17$,似乎總能拆成兩個質數相加。猜想說這對**所有**大於 2 的偶數都成立。偶數越大,拆法通常越多(「哥德巴赫彗星」現象),但「總是至少一種拆法」至今無人能證。

**正式版(強哥德巴赫猜想 / binary Goldbach)**:
$$\forall\, n \in 2\mathbb{Z},\ n \ge 4:\ \exists\, p, q \text{ 質數},\ n = p + q$$

**弱哥德巴赫猜想(ternary Goldbach,已證)**:每個 $\ge 7$ 的奇數都是三個質數之和。強猜想蘊含弱猜想(奇數 $n = 3 + (n-3)$,$n-3$ 為偶數)。

## 背景與重要性

1742 年 Goldbach 在給 Euler 的信中提出雛形,Euler 回信給出現今的標準形式。它是加法數論的原型問題:質數是「乘法性」的對象,問它們的「加法性」行為,正是這類問題困難的根源。攻克它所發展的工具——Hardy–Littlewood 圓法(circle method)、篩法(sieve methods)——已成為解析數論的支柱,影響遍及 Waring 問題、質數等差數列(Green–Tao)等領域。

## 目前狀態

截至 2026 年 7 月:強猜想未解決。已知:

- **弱猜想已完全證明**(Helfgott 2013,見時間線;證明被學界廣泛接受,完整專著仍在出版流程中)。
- **Chen 定理**:每個充分大的偶數都是 $p + P_2$(一個質數加上一個至多兩個質因子的數)。這是篩法能達到的極限之一,卡在著名的「宇稱問題」(parity problem)——篩法本質上無法區分質因子個數的奇偶。
- **例外集**:不能表示為兩質數和的偶數(若存在)密度為零,且例外集大小有明確上界。
- **數值驗證**:至 $4 \times 10^{18}$ 全部成立(2014,經同行評審);2025 年社群網格運算再往前推(見時間線,非同行評審)。

卡在哪裡:圓法對「三個質數」(major arcs 主導)有效,對「兩個質數」則 minor arcs 誤差項壓不住;篩法則被宇稱問題擋住。兩條主力路線各有本質性障礙。

## 進展時間線

| 年份 | 進展 | 貢獻者 |
|---|---|---|
| 1742 | 猜想提出 | C. Goldbach, L. Euler |
| 1920 | 篩法首次逼近:每個大偶數為兩個質因子個數 $\le 9$ 的數之和(「9+9」) | V. Brun |
| 1937 | 每個充分大的奇數是三個質數之和 | I. M. Vinogradov |
| 1966–1973 | Chen 定理:充分大偶數 $= p + P_2$(「1+2」) | 陳景潤 Chen Jingrun |
| 1975 | 例外集密度為零的定量版本 | H. Montgomery, R. Vaughan |
| 2013 | **弱哥德巴赫猜想完整證明**([arXiv:1312.7748](https://arxiv.org/abs/1312.7748),廣被接受;完整專著仍在出版流程) | H. Helfgott |
| 2014 | 數值驗證強猜想至 $4 \times 10^{18}$(Math. Comp. 83,[DOI](https://doi.org/10.1090/S0025-5718-2013-02787-1)) | T. Oliveira e Silva, S. Herzog, S. Pardi |
| 2025 | 社群網格運算專案 Gridbach 宣稱將驗證推進至 $4\times 10^{18} + 7\times 10^{13}$([專案作者說明](https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d);社群專案,非同行評審) | H. J. Nakata / Gridbach |

註:2024–2026 間 arXiv 與各處不時出現「已證明哥德巴赫猜想」的預印本或論文,截至查證時**沒有任何一篇被主流數學社群接受**。

## 主要研究方法

- **圓法(Hardy–Littlewood–Vinogradov)**:把表示數寫成指數和的積分,主弧給主項、次弧給誤差。對三質數問題成功(Vinogradov→Helfgott),對二質數問題誤差項本質性地失控。
- **篩法(Brun→Selberg→Chen)**:逐步逼近「1+1」,最好成果是 Chen 的「1+2」。宇稱問題是已被證明存在的路障,除非注入新的「型別資訊」(如 Friedlander–Iwaniec 式的雙線性方法)。
- **例外集路線**:不求全解,先證「幾乎所有偶數都行」並縮小例外集;與零點密度估計相關,Guth–Maynard 2024 的技術進步可望間接改進此類結果。
- **計算驗證**:提供信心與資料(每個偶數的表示法個數 $g(n)$,即哥德巴赫彗星),但有限驗證永遠不構成證明。

## AI 可以怎麼幫忙

- **形式化**:強、弱猜想的**陳述**在 Lean 4 / Mathlib 中都可以幾行寫出(只需 `Nat.Prime` 與加法);陳述本身沒有形式化障礙。Helfgott 弱猜想**證明**的形式化則是未完成的大工程(涉及大量顯式解析估計與區間算術),目前沒有完成的公開專案。
- **機器學習/LLM**:無已被認可的直接突破;合理用途是輔助文獻篩選(該領域「宣稱證明」的噪音極大,自動分類真偽線索有實際價值)。
- **本 repo 可做的事**:
  - 寫一個哥德巴赫拆分計數器,重現「哥德巴赫彗星」並與 Hardy–Littlewood 預測公式($g(n)$ 的漸近)做比對;
  - 在 Lean 中形式化強/弱猜想的陳述,以及「強蘊含弱」的簡單推理,作為形式化練習;
  - 建立 2024–2026「宣稱證明」清單與其被指出的錯誤,作為誠實的文獻追蹤;
  - 追蹤 Helfgott 專著的出版狀態與弱猜想證明形式化的任何啟動跡象。

## 關鍵文獻與資源

- Helfgott, *The ternary Goldbach conjecture is true*(2013):https://arxiv.org/abs/1312.7748
- Oliveira e Silva, Herzog & Pardi, *Empirical verification of the even Goldbach conjecture...*, Math. Comp. 83 (2014):https://doi.org/10.1090/S0025-5718-2013-02787-1
- Vaughan, *The Hardy–Littlewood Method*(圓法標準教材,Cambridge University Press)
- 陳景潤原始論文的背景綜述可見 Halberstam & Richert, *Sieve Methods*
- Tomás Oliveira e Silva 的驗證計畫頁面(含 $g(n)$ 資料):https://sweet.ua.pt/tos/goldbach.html
