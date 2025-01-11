# main.py
from crewai import Crew, Process, LLM
from agents import AnalysisAgents
from tasks import AnalysisTasks

# main.py
llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434",
    # 增加配置參數
    config={
        "temperature": 0.7,        # 控制創造力與準確性的平衡
        "top_p": 0.9,             # 控制輸出的多樣性
        "context_length": 8192,    # 提供足夠的上下文長度
        "response_format": {"type": "text"},  # 確保回應格式一致
        "seed": 42,               # 設定隨機種子以獲得一致的輸出
    }
)

class FinancialCrew:
    """財務分析團隊類，協調不同代理完成分析任務"""
    
    def __init__(self, company: str):
        """
        初始化財務分析團隊
        
        Args:
            company (str): 要分析的公司名稱
        """
        self.company = company
    
    def run(self):
        """
        執行分析流程
        
        Returns:
            str: 分析結果
        """
        # 初始化代理和任務
        agents = AnalysisAgents(llm)
        tasks = AnalysisTasks()
        
        # 創建分析師代理
        mr_analyst = agents.market_research_analyst()
        cfa = agents.cfa()
        
        # 創建任務
        research = tasks.research(mr_analyst, self.company)
        analysis = tasks.analysis(cfa, research)
        
        # 創建並執行Crew
        crew = Crew(
            agents=[mr_analyst, cfa],
            tasks=[research, analysis],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("\n\n## 歡迎來到投資顧問團隊")
    print("-------------------------")
    company = input("請輸入您想分析的公司名稱\n")
    financial_crew = FinancialCrew(company)
    result = financial_crew.run()
    print("\n\n####################")
    print("## 如下是分析結果")
    print("####################\n")
    print(result)