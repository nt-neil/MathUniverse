# 邏輯與集合論(Logic & Set Theory)未解難題目錄

> 收錄集合論、模型論、可計算性理論、證明論/逆數學中的著名開放問題,以及以「獨立性」告終的經典問題。

**「獨立(ZFC)」不等於「未解」**:本領域特有的情況是,一個問題可能被證明**獨立於 ZFC 公理系統**(既不能證明也不能否證,如連續統假設)。這在「相對於 ZFC」的意義下是完全解決的定理;但「在更強的自然公理下它是否有確定答案」可以仍是活躍的開放研究(如 Woodin 的 Ultimate-L 綱領)。本檔以 `獨立(ZFC)` 標記前者,並在需要處註明後續的開放面向;`未解` 保留給真正開放的問題。

**主要來源**:
- Wikipedia [List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)(模型論、集合論段)
- [FOM(Foundations of Mathematics)郵件列表](https://cs.nyu.edu/mailman/listinfo/fom)
- Montalbán, [Open Questions in Reverse Mathematics](https://math.berkeley.edu/~antonio/papers/questionsRM.pdf)
- Sargsyan, [Descriptive Inner Model Theory](https://arxiv.org/abs/1206.2712);Trang, [Recent Developments in Inner Model Theory](https://sites.math.unt.edu/~ntrang/IMTre.pdf)

## 難題清單

### 集合論

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| 連續統假設(Continuum Hypothesis, CH) | 是否不存在嚴格介於 ℕ 與 ℝ 基數之間的無窮基數? | 1878/Cantor | 獨立(ZFC)(Gödel 1940 + Cohen 1963);「是否有自然的正確答案」仍是開放研究:V=Ultimate-L 蘊涵 CH,而力迫公理路線(MM⁺⁺、(*))給出 2^ℵ⁰=ℵ₂ | [Wikipedia](https://en.wikipedia.org/wiki/Continuum_hypothesis) |
| Ultimate-L 猜想(Ultimate-L Conjecture) | 是否存在滿足「V=Ultimate-L」的容納超緊緻基數的典範內模型? | 2010s/Woodin | 未解(2024 年 exacting 基數結果顯示:若某些新大基數與 extendible 基數相容,則猜想不成立) | [Wikipedia](https://en.wikipedia.org/wiki/Ultimate_L) |
| HOD 猜想(HOD Conjecture) | ZFC 是否證明:在有 extendible 基數下,HOD 與 V 「接近」(HOD 二分法的正面一側恆成立)? | 2010/Woodin | 未解(同上:exacting 基數若與 extendible 相容則反駁之) | [arXiv:2411.11568](https://arxiv.org/abs/2411.11568) |
| Ω-猜想(Omega Conjecture) | Woodin 的 Ω-邏輯完備性猜想是否成立? | 1999/Woodin | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/%CE%A9-logic) |
| 超緊緻基數的內模型問題(Inner model problem for a supercompact) | 能否建構容納超緊緻基數的細結構典範內模型? | 1970s | 未解(內模型理論的核心目標) | [Trang 綜述](https://sites.math.unt.edu/~ntrang/IMTre.pdf) |
| Reinhardt 基數的一致性(Consistency of Reinhardt cardinals) | ZF(無選擇公理)+ 存在非平凡初等嵌入 j:V→V 是否一致?(Kunen 1971 已證與 ZFC 不一致) | 1967/Reinhardt | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/Reinhardt_cardinal) |
| 老鼠集合猜想(Mouse Set Conjecture) | 在決定性模型中,序數可定義的實數是否恰為出現在可迭代 mouse 中的實數? | 1990s/Steel、Woodin | 部分解決(在極小 AD_ℝ+「Θ 正則」模型中已證,Sargsyan) | [Sargsyan](https://arxiv.org/abs/1206.2712) |
| AD 與 AD⁺ 的等價(Does AD imply AD⁺?) | 決定性公理 AD 是否已蘊涵其結構性強化 AD⁺? | 1980s/Woodin | 未解 | [Aguilera 綜述](https://arxiv.org/abs/2302.02248) |
| Shelah 的 pcf 界限問題(Shelah's pcf bound) | 若 ℵ_ω 是強極限,Shelah 證明 2^ℵω < ℵ_{ω₄};能否改進到 ℵ_{ω₁}?pcf(a) 可否大於 \|a\|? | 1994/Shelah | 未解 | [Wikipedia](https://en.wikipedia.org/wiki/PCF_theory) |
| Suslin 假設(Suslin's problem) | 完備稠密無端點且滿足可數鏈條件的線序是否必同構於 ℝ? | 1920/Suslin | 獨立(ZFC)(Jech、Tennenbaum、Solovay 1960s–70s) | [Wikipedia](https://en.wikipedia.org/wiki/Suslin%27s_problem) |
| Whitehead 問題(Whitehead problem) | 每個 Whitehead 群(Ext¹(A,ℤ)=0 的阿貝爾群)是否皆自由? | 1952/Whitehead | 獨立(ZFC)(Shelah 1974;第一個被證明獨立的「主流代數」問題) | [Wikipedia](https://en.wikipedia.org/wiki/Whitehead_problem) |
| Borel 猜想(Borel conjecture) | 強測度零集是否必為可數集? | 1919/Borel | 獨立(ZFC)(CH 給反例;Laver 1976 證一致;Borel 猜想與對偶 Borel 猜想可同時一致,Goldstern–Kellner–Shelah–Wohofsky 2014) | [Wikipedia](https://en.wikipedia.org/wiki/Strong_measure_zero_set) |
| NF 的一致性(Consistency of New Foundations) | Quine 的 NF 集合論是否一致? | 1937/Quine | ✅ 已解決(2024)(Holmes–Wilshaw,證明經 Lean 形式化驗證) | [con-nf 專案](https://leanprover-community.github.io/con-nf/) |

### 模型論

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Vaught 猜想(Vaught's Conjecture) | 可數語言的完備理論,其可數模型數是否只能為至多可數或恰為連續統? | 1961/Vaught | 未解(ω-穩定理論、線序、布林代數等特例已證) | [Wikipedia](https://en.wikipedia.org/wiki/Vaught_conjecture) |
| Cherlin–Zilber 代數性猜想(Algebraicity conjecture) | 有限 Morley 秩的無限單群是否皆為代數閉體上的代數群? | 1979/Cherlin、Zilber | 未解(偶型情形已證) | [Wikipedia](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Model_theory_and_formal_languages) |
| 穩定體猜想(Stable fields conjecture) | 無限穩定體是否必為可分閉體? | 1970s–80s | 未解(超穩定情形已證 Macintyre;dp-有限等特例近年有進展) | [Wikipedia](https://en.wikipedia.org/wiki/Stable_theory) |
| Keisler 序的結構(Structure of Keisler's order) | Keisler 序對簡單理論的分類與整體結構為何? | 1967/Keisler | 部分解決(已知有無限多類、非線序、非「簡單」——見動態) | [Adv. Math. 2021](https://arxiv.org/abs/1906.10241) |

### 可計算性與可判定性

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Hilbert 第十問題:有理數版(H10 over ℚ) | 是否存在演算法判定多項式方程有無**有理數**解?(整數版已否定,Matiyasevich 1970) | 1900/Hilbert | 未解(數域整數環情形 2024 已否定——見動態) | [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_tenth_problem) |
| Skolem 問題(Skolem problem) | 是否可判定一個整數線性遞迴數列是否有零項? | 1930s/Skolem | 部分解決(階 ≤4 已可判定,2024–25;階 ≥5 未解) | [Wikipedia](https://en.wikipedia.org/wiki/Skolem_problem) |
| 單關係幺半群的字問題(Word problem for one-relation monoids) | 只有一條定義關係的幺半群,其字問題是否皆可判定?(單關係「群」已可判定,Magnus 1932) | 1914/Thue | 未解 | [綜述 arXiv:2105.02853](https://arxiv.org/abs/2105.02853) |
| Tarski 指數函數問題(Tarski's exponential function problem) | 實數體加上指數函數的一階理論是否可判定? | 1950s/Tarski | 未解(Macintyre–Wilkie 1996:若 Schanuel 猜想成立則可判定) | [Wikipedia](https://en.wikipedia.org/wiki/Tarski%27s_exponential_function_problem) |

### 證明論、逆數學與獨立性

| 難題 | 問題(一句話) | 提出 | 狀態 | 來源 |
|---|---|---|---|---|
| Hindman 定理的逆數學強度(Strength of Hindman's theorem) | Hindman 定理恰等價於 ACA₀、ACA₀⁺,還是嚴格介於其間? | 1987/Blass–Hirst–Simpson | 未解 | [Montalbán](https://math.berkeley.edu/~antonio/papers/questionsRM.pdf) |
| 自然的具體獨立命題(Friedman's concrete independence) | 是否存在公認「自然」的有限組合命題獨立於 ZFC?(Friedman 的布林關係理論給出候選,其「自然性」尚在辯論) | 1980s–/H. Friedman | 未解(研究綱領) | [Friedman BRT](https://u.osu.edu/friedman.8/foundational-adventures/boolean-relation-theory-book/) |

## 值得關注的動態(2021–2026)

- **2021|MM⁺⁺ 蘊涵 Woodin 公理 (*)**:Asperó 與 Schindler 證明 Martin's Maximum⁺⁺ 蘊涵 (*),統一了 1990 年代以來兩條互相競爭的強公理路線(皆給出 2^ℵ⁰=ℵ₂),發表於 *Annals of Mathematics* 193(3)。這被視為「連續統假設辯論」中力迫公理一側的重大整合。[Annals 2021](https://www.jstor.org/stable/10.4007/annamath.193.issue-3)|[UEA 報導](https://www.uea.ac.uk/about/news/article/uea-mathematician-wins-hausdorff-medal)
- **2024|Hilbert 第十問題:所有數域的整數環皆不可判定**:Koymans–Pagano(加法組合學+橢圓曲線 2-descent)與 Alpöge–Bhargava–Ho–Shnidman(Mordell 曲線)以完全不同方法獨立證明;2026 年更推廣到所有無限有限生成 ℤ-代數。**有理數版本仍未解**。[arXiv:2412.01768](https://arxiv.org/abs/2412.01768)|[arXiv:2412.04253](https://arxiv.org/pdf/2412.04253)|[arXiv:2602.04468](https://arxiv.org/abs/2602.04468)
- **2024|Exacting/ultraexacting 基數衝擊 HOD 猜想與 Ultimate-L 綱領**:Aguilera–Bagaria–Lücke 等引入新型大基數(相對 I0 嵌入一致),並證明:若 exacting 基數可與 extendible 基數共存,則 Woodin 的 HOD 猜想與 Ultimate-L 猜想不成立;exacting 基數本身即蘊涵 V≠HOD。這是近年對 Ultimate-L 綱領最具體的挑戰。[arXiv:2411.11568](https://arxiv.org/abs/2411.11568)
- **2024|Quine NF 集合論一致性證明完成形式化驗證**:Holmes 自 2010 年起宣稱的 Con(NF) 證明,由 Wilshaw 在 Lean 中完成全形式化(經由 Tangled Type Theory 模型),87 年老問題落幕。[con-nf](https://leanprover-community.github.io/con-nf/)|[Holmes 主頁](https://randall-holmes.github.io/)
- **2024|BB(5) = 47,176,870**:bbchallenge 協作計畫窮盡分析 1.8 億台 5 態圖靈機並以 Coq/Rocq 驗證,確定第五個忙碌海狸數——60 年來首次新增 BB 值;BB(6) 已知獨立性/不可行性壁壘更近。[bbchallenge](https://discuss.bbchallenge.org/t/july-2nd-2024-we-have-proved-bb-5-47-176-870/237)|[arXiv:2509.12337](https://arxiv.org/pdf/2509.12337)
- **2024–25|Skolem 問題:階 4 全面可判定**:Bacik 補齊代數線性遞迴階 ≤4 的可判定性(1980 年代以來僅知階 ≤3 與實代數階 4);另有正特徵環情形(STOC)與條件式(p-adic Schanuel)進展。階 5 仍未解。[arXiv:2409.01221](https://arxiv.org/abs/2409.01221)
- **2021|Keisler 序不「簡單」**:Malliaris–Shelah 在 ZFC 中證明 Keisler 序在簡單理論內部即有複雜結構(此前已證其有無限多類、非線序),徹底推翻該序簡單分層的早期圖景。[Adv. Math. 392 (2021)](https://arxiv.org/abs/1906.10241)
