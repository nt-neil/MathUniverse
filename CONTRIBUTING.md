# 如何參與

這個專案歡迎任何形式的貢獻,不需要是數學家。

## 你可以做的事

- **補充最新進展**:某個難題有新論文、新突破?在該難題深度檔案的「進展時間線」或 `catalog/` 對應領域檔的「值得關注的動態」加一列,附上可查證的來源(arXiv、期刊、可信媒體)。
- **更新目錄狀態**:發現 `catalog/` 裡某題狀態過時(已解決/被否證/出現宣稱證明)?依 `catalog/_format.md` 的狀態標記修正,附來源。
- **新增目錄條目**:在 `catalog/` 對應領域檔加一列(格式見 `catalog/_format.md`)。
- **新增深度難題**:複製 `problems/_template/README.md`,放到對應領域的資料夾,並在 README 的總表加上連結。
- **修正錯誤**:數學陳述、翻譯、連結失效,都歡迎開 PR 或 issue。
- **AI 實驗**:用 AI 做的反例搜索、形式化驗證、文獻分析,結果(含失敗的)可放進對應難題資料夾的 `ai/` 子資料夾。
- **認領路線圖項目**:見 [ROADMAP.md](ROADMAP.md),開 issue 討論即可。

## 特別注意

- **`taxonomy/msc/` 不要手改**:整個目錄由 `tools/msc/generate.py` 從官方資料生成,手改會在下次重跑時被覆蓋;要修就修腳本再重跑。此目錄授權為 CC BY-NC-SA(見 `taxonomy/msc/LICENSE-MSC.md`),與 repo 其他內容不同。

## 基本規則

1. **來源優先**:任何「已證明/已推進」的聲明都必須附可查證出處。預印本(arXiv)要註明尚未經同儕審查。
2. **誠實定位**:本專案不宣稱解決了任何未解問題。AI 產出的內容需標註並經人工查證。
3. **語言**:內容以繁體中文為主,數學術語附英文原文;也歡迎純英文貢獻,我們會協助翻譯。
4. **格式**:難題檔案遵循 `problems/_template/README.md` 的結構。
5. **安全 / Security**:請勿提交 API 金鑰、token、私人檔案路徑(如 `/Users/<name>/...`)或個人聯絡資訊;CI 會用 Gitleaks 自動掃描每個 PR。Never commit API keys, tokens, private file paths, or personal contact info — CI scans every PR with Gitleaks.

## 流程

Fork → 修改 → Pull Request。小改動(錯字、連結)可以直接開 PR;新增難題或大改動建議先開 issue 討論。
