#!/usr/bin/env python3
"""從官方 MSC2020 CSV 生成 taxonomy/msc/ 的完整分類樹。

資料來源:https://msc2020.org/MSC_2020.csv(tab 分隔,Latin-1 編碼)
用法:python3 tools/msc/generate.py(在 repo 根目錄或任意位置執行皆可)
腳本為冪等:重跑會完整重新生成 taxonomy/msc/ 下所有檔案。
只用 Python 3 標準庫。
"""

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_FILE = Path(__file__).resolve().parent / "data" / "MSC_2020.csv"
OUT_DIR = REPO_ROOT / "taxonomy" / "msc"

ATTRIBUTION = (
    "\n---\n\n"
    "資料來源:MSC2020(Mathematics Subject Classification 2020),"
    "© Mathematical Reviews(American Mathematical Society)與 zbMATH,"
    "依 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 授權散布"
    "(見 [msc2020.org](https://msc2020.org/)),不適用本 repo 的 CC BY 4.0。"
    "詳見 [LICENSE-MSC.md](./LICENSE-MSC.md)。\n"
)

# 一級分類繁中譯名(代碼 → 譯名;英文原名一律取自原始資料)
ZH_NAMES = {
    "00": "總論與綜合主題",
    "01": "數學史與傳記",
    "03": "數理邏輯與基礎",
    "05": "組合學",
    "06": "序、格與有序代數結構",
    "08": "一般代數系統",
    "11": "數論",
    "12": "體論與多項式",
    "13": "交換代數",
    "14": "代數幾何",
    "15": "線性與多重線性代數;矩陣理論",
    "16": "結合環與結合代數",
    "17": "非結合環與非結合代數",
    "18": "範疇論;同調代數",
    "19": "K-理論",
    "20": "群論及其推廣",
    "22": "拓樸群、李群",
    "26": "實變函數",
    "28": "測度與積分",
    "30": "複變函數",
    "31": "位勢論",
    "32": "多複變與解析空間",
    "33": "特殊函數",
    "34": "常微分方程",
    "35": "偏微分方程",
    "37": "動態系統與遍歷理論",
    "39": "差分方程與函數方程",
    "40": "數列、級數、可和性",
    "41": "逼近與展開",
    "42": "歐氏空間上的調和分析",
    "43": "抽象調和分析",
    "44": "積分變換、運算微積分",
    "45": "積分方程",
    "46": "泛函分析",
    "47": "算子理論",
    "49": "變分法與最佳控制;最佳化",
    "51": "幾何學",
    "52": "凸幾何與離散幾何",
    "53": "微分幾何",
    "54": "一般拓樸",
    "55": "代數拓樸",
    "57": "流形與胞腔複形",
    "58": "整體分析、流形上的分析",
    "60": "機率論與隨機過程",
    "62": "統計學",
    "65": "數值分析",
    "68": "電腦科學",
    "70": "質點與系統力學",
    "74": "可變形固體力學",
    "76": "流體力學",
    "78": "光學、電磁理論",
    "80": "古典熱力學、熱傳",
    "81": "量子理論",
    "82": "統計力學、物質結構",
    "83": "相對論與重力理論",
    "85": "天文學與天文物理",
    "86": "地球物理",
    "90": "作業研究、數學規劃",
    "91": "賽局理論、經濟、金融與其他社會行為科學",
    "92": "生物學與其他自然科學",
    "93": "系統理論;控制",
    "94": "資訊與通訊理論、電路",
    "97": "數學教育",
}

LICENSE_MSC = """# 本目錄(taxonomy/msc/)的授權

本目錄所有檔案的內容取自 **MSC2020(Mathematics Subject Classification 2020)**,
由 Mathematical Reviews(American Mathematical Society)與 zbMATH 共同編製與發布,
版權屬於該兩機構。

MSC2020 依 **Creative Commons Attribution-NonCommercial-ShareAlike(CC BY-NC-SA)**
授權條款發布:

- 官方發布頁(含授權聲明與原始資料下載):<https://msc2020.org/>
- 授權條款全文:<https://creativecommons.org/licenses/by-nc-sa/4.0/>

因此,**本目錄的內容不適用本 repo 其餘部分的 CC BY 4.0 授權**,
而是依上述 CC BY-NC-SA 條款散布(含非商業性與相同方式分享之限制)。
一級分類的繁體中文譯名為本 repo 加上的改作,同樣依 CC BY-NC-SA 條款散布。

本目錄檔案由 `tools/msc/generate.py` 從官方 CSV(`tools/msc/data/MSC_2020.csv`)自動生成。
"""


def clean(s: str) -> str:
    """把原始資料的 TeX 慣例轉成適合 Markdown 的形式。"""
    s = s.replace("\\{", "{").replace("\\}", "}")
    s = s.replace("\\(", "$").replace("\\)", "$")
    s = s.replace("|", "\\|")
    return s.strip()


def load_rows():
    rows = []
    with open(DATA_FILE, encoding="latin-1", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # header: code, text, description
        for row in reader:
            if row and row[0]:
                rows.append((row[0].strip(), clean(row[1]), clean(row[2])))
    return rows


def main():
    rows = load_rows()
    top = {}      # "11" -> name
    second = {}   # "11" -> [(code, desc), ...]  (##Xxx)
    third = {}    # "11A" -> [(code, desc), ...] (##X##)
    dash = {}     # "11" -> [(code, desc), ...]  (##-##)

    for code, text, desc in rows:
        if re.fullmatch(r"\d\d-XX", code):
            top[code[:2]] = text  # 一級分類用短名(不含交叉引用註記)
        elif re.fullmatch(r"\d\d[A-Z]xx", code):
            second.setdefault(code[:2], []).append((code, desc))
        elif re.fullmatch(r"\d\d[A-Z]\d\d", code):
            third.setdefault(code[:3], []).append((code, desc))
        elif re.fullmatch(r"\d\d-\d\d", code):
            dash.setdefault(code[:2], []).append((code, desc))
        else:
            raise SystemExit(f"無法辨識的代碼格式:{code}")

    missing = set(top) - set(ZH_NAMES)
    if missing:
        raise SystemExit(f"缺少中文譯名:{sorted(missing)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # 冪等:清掉舊生成檔
    for p in OUT_DIR.glob("*.md"):
        p.unlink()

    (OUT_DIR / "LICENSE-MSC.md").write_text(LICENSE_MSC, encoding="utf-8")

    n_leaf_total = 0
    # 各一級分類檔
    for sec in sorted(top):
        name = top[sec]
        lines = [f"# MSC {sec} — {name}", ""]
        lines.append(f"繁中譯名:{ZH_NAMES[sec]}(官方代碼 `{sec}-XX`)")
        lines.append("")
        lines.append("[← 回 MSC 總索引](./README.md)")
        lines.append("")
        if sec in dash:
            lines.append(f"## {sec}-XX 通用條目")
            lines.append("")
            lines.append("| 代碼 | 英文描述 |")
            lines.append("|---|---|")
            for code, desc in dash[sec]:
                lines.append(f"| `{code}` | {desc} |")
                n_leaf_total += 1
            lines.append("")
        for code2, desc2 in second.get(sec, []):
            lines.append(f"## {code2} — {desc2}")
            lines.append("")
            kids = third.get(code2[:3], [])
            if kids:
                lines.append("| 代碼 | 英文描述 |")
                lines.append("|---|---|")
                for code3, desc3 in kids:
                    lines.append(f"| `{code3}` | {desc3} |")
                    n_leaf_total += 1
                lines.append("")
        lines.append(ATTRIBUTION)
        (OUT_DIR / f"{sec}.md").write_text("\n".join(lines), encoding="utf-8")

    # 總索引 README.md
    n2 = sum(len(v) for v in second.values())
    n3 = sum(len(v) for v in third.values())
    nd = sum(len(v) for v in dash.values())
    lines = ["# MSC2020 完整分類樹", ""]
    lines.append(
        "Mathematics Subject Classification 2020(MSC2020)由 Mathematical Reviews(AMS)"
        "與 zbMATH 共同維護,是國際通用的數學文獻分類系統。"
    )
    lines.append("")
    lines.append(
        f"本目錄收錄完整分類:**{len(top)} 個一級分類**、**{n2} 個二級分類**、"
        f"**{n3} 個三級條目**(另有 {nd} 個 `##-##` 形式的通用條目,"
        "如教科書、綜述、歷史、計算方法等,列於各一級分類檔開頭)。"
    )
    lines.append("")
    lines.append("三級條目描述保留英文原文;一級分類附繁體中文譯名。")
    lines.append("")
    lines.append("| 代碼 | 英文名稱 | 繁中譯名 |")
    lines.append("|---|---|---|")
    for sec in sorted(top):
        lines.append(f"| [`{sec}-XX`](./{sec}.md) | {top[sec]} | {ZH_NAMES[sec]} |")
    lines.append(ATTRIBUTION)
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"一級:{len(top)} 二級:{n2} 三級:{n3} 通用(##-##):{nd}")
    print(f"葉條目寫入總數:{n_leaf_total}(應等於 三級+通用 = {n3 + nd})")
    print(f"生成檔案:{len(list(OUT_DIR.glob('*.md')))} 個於 {OUT_DIR}")


if __name__ == "__main__":
    main()
