import os
import requests
import json
from langchain.tools import tool

class SearchTools:
    @tool
    def searchInfo(query: str):
        """在網上搜索關於指定內容的相關信息
        
        Args:
            query (str): 搜索查詢字符串
            
        Returns:
            str: 格式化的搜索結果
        """
        return SearchTools.search(query)
    
    def search(query: str):
        """使用Google Serper API執行新聞搜索
        
        Args:
            query (str): 搜索查詢字符串
            
        Returns:
            str: 格式化的新聞結果，包含標題、日期、來源和摘要
        """
        # 設置API端點
        url = "https://google.serper.dev/news"
        
        # 準備請求數據
        payload = json.dumps({
            "q": query,
            "hl": "zh-tw"  # 設置語言為繁體中文
        })
        
        # 設置請求頭
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        
        # 發送請求
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['news']
        
        # 處理結果
        stirng = []
        for result in results:
            try:
                stirng.append('\n'.join([
                    f"標題: {result['title']}",
                    f"時間: {result['date']}",
                    f"來源: {result['source']}",
                    f"摘要: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError:
                next
        
        content = '\n'.join(stirng)
        return f"\nSearch result: {content}\n"