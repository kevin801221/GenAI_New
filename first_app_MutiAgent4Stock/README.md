```markdown
# 多代理人財務分析系統 (Multi-Agent Financial Analysis System)

graph TD
    A[Agent: 市場研究分析師] --> T1[Task 1: 搜索公司新聞]
    A --> T2[Task 2: 分析市場趨勢]
    A --> T3[Task 3: 競爭對手分析]
    
    B[Agent: 財務分析師] --> T4[Task 4: 財報分析]
    B --> T5[Task 5: 風險評估]
    B --> T6[Task 6: 投資建議]
    
## 🌟 項目簡介

這是一個基於 CrewAI 框架開發的多代理人財務分析系統，利用 AI 代理協同工作，為用戶提供專業的股票投資分析服務。系統整合了市場研究和財務分析功能，通過多個 AI 代理的協作，提供全面的投資建議。

## 🚀 特點

- 多代理協同：結合市場研究分析師和特許財務分析師的專業視角
- 智能搜索：整合 Google Serper API 進行實時市場信息搜索
- 本地 LLM：使用 Ollama 運行 Llama 3.2 模型，保證隱私和效率
- 專業分析：提供結構化的市場研究報告和投資建議
- 中文支持：完全支持中文輸入和輸出

## 🛠️ 技術架構

- **框架**：CrewAI
- **語言模型**：Llama 3.2 (通過 Ollama 部署)
- **搜索 API**：Google Serper
- **開發語言**：Python 3.8+

## 📋 系統組件

```
project/
├── main.py               # 主程序入口
├── agents.py            # AI 代理定義
├── tasks.py            # 任務定義
└── tools/
    └── search.py       # 搜索工具實現
```

## 💻 安裝指南

1. **安裝 Ollama**
```bash
# MacOS/Linux
curl https://ollama.ai/install.sh | sh

# 拉取 Llama 3.2 模型
ollama pull llama3.2
```

2. **安裝依賴包**
```bash
pip install crewai langchain requests python-dotenv
```

3. **環境變量設置**
創建 `.env` 文件並添加：
```env
SERPER_API_KEY=your_serper_api_key
```

## 🚀 使用方法

1. **啟動 Ollama 服務**
```bash
ollama serve
```

2. **運行分析系統**
```bash
python main.py
```

3. **輸入公司名稱**
按照提示輸入想要分析的公司名稱，系統將自動開始分析。

## 🤖 代理介紹

### 市場研究分析師
- 職責：搜索和分析公司市場信息
- 特點：專注於市場趨勢和公司動態
- 工具：整合 Google Serper API 進行信息搜索

### 特許財務分析師
- 職責：深入分析財務數據並提供投資建議
- 特點：專注於財務分析和投資價值評估
- 輸出：具體的投資建議和目標價位

## 📊 輸出示例

系統將生成包含以下內容的分析報告：

1. 公司概況
2. 最新重要新聞動態
3. 財務分析
4. 市場地位評估
5. 投資建議

## 🔧 自定義配置

可以通過修改 `main.py` 中的 LLM 配置來調整模型參數：

```python
llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434",
    config={
        "temperature": 0.7,
        "top_p": 0.9,
        "context_length": 4096,
    }
)
```

## 📝 開發說明

### 添加新代理
1. 在 `agents.py` 中定義新的代理類
2. 設置代理的角色、目標和背景故事
3. 配置所需工具和權限

### 添加新任務
1. 在 `tasks.py` 中定義新的任務
2. 設置任務描述和期望輸出
3. 分配適當的代理執行任務

## 🔍 常見問題

1. **如何提升分析質量？**
   - 調整 LLM 的 temperature 參數
   - 增加上下文長度
   - 優化代理的提示詞

2. **模型回應較慢？**
   - 確保電腦配置足夠
   - 考慮使用更小的模型版本
   - 優化任務流程

3. **搜索結果不準確？**
   - 檢查 Serper API 配置
   - 優化搜索關鍵詞
   - 調整搜索範圍

## 📈 未來計劃

- [ ] 添加更多專業分析工具
- [ ] 支持更多數據源接入
- [ ] 優化代理協作機制
- [ ] 添加 Web 界面
- [ ] 支持批量分析功能

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request 來幫助改進項目！

1. Fork 本項目
2. 創建特性分支
3. 提交改動
4. 推送到分支
5. 創建 Pull Request

## 📄 許可證

MIT License

## 📞 聯繫方式

- 作者：[Your Name]
- Email：[Your Email]
- GitHub：[Your GitHub Profile]

## 🙏 致謝

- CrewAI 框架
- Ollama 項目
- Llama 模型
- Google Serper API

```

這個 README.md 涵蓋了：
1. 項目介紹和特點
2. 技術架構
3. 安裝和使用說明
4. 系統組件說明
5. 代理介紹
6. 自定義配置指南
7. 開發說明
8. 常見問題
9. 未來計劃
10. 貢獻指南