# MSC2020 分類樹生成工具

從官方 MSC2020 資料生成 `taxonomy/msc/` 下的完整分類樹 Markdown 檔。

## 資料來源

- `data/MSC_2020.csv`:官方發布的機器可讀版,下載自 <https://msc2020.org/MSC_2020.csv>
  (tab 分隔、Latin-1 編碼,欄位:`code`、`text`(短名)、`description`(含交叉引用的完整描述))
- `data/MSC_2020.tex`:官方 TeX 版備份,下載自 <https://msc2020.org/MSC_2020.tex>(腳本未使用,僅留存)
- 授權:MSC2020 © Mathematical Reviews(AMS)與 zbMATH,CC BY-NC-SA,
  詳見 `taxonomy/msc/LICENSE-MSC.md`

## 用法

```sh
python3 tools/msc/generate.py
```

只需 Python 3 標準庫。腳本為冪等:每次執行會先清除 `taxonomy/msc/` 下的舊 `.md` 檔,
再完整重新生成:

- `taxonomy/msc/README.md`:總索引(63 個一級分類,含繁中譯名)
- `taxonomy/msc/<兩位代碼>.md`:每個一級分類一檔,含二級分類與三級條目表
- `taxonomy/msc/LICENSE-MSC.md`:MSC 資料的授權聲明

執行結束會印出各級條目數;三級 + `##-##` 通用條目合計應為 6006。
