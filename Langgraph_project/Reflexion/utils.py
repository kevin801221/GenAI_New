import json
import logging
from datetime import datetime
from typing import Any, Dict

def save_structured_output(data: Dict[str, Any], base_filename: str = None):
    # 使用時間戳作為文件名的一部分
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = base_filename or f"agent_output_{timestamp}"
    
    # 保存JSON格式
    json_filename = f"{base_filename}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 保存TXT格式（更易讀的格式）
    txt_filename = f"{base_filename}.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write(f"AI Agent Output - {timestamp}\n")
        f.write("="*50 + "\n\n")
        
        # 寫入主要內容
        if 'answer' in data:
            f.write("Answer:\n")
            f.write("-"*20 + "\n")
            f.write(data['answer'] + "\n\n")
        
        if 'reflection' in data:
            f.write("Reflection:\n")
            f.write("-"*20 + "\n")
            for key, value in data['reflection'].items():
                f.write(f"{key.capitalize()}:\n{value}\n\n")
        
        if 'references' in data:
            f.write("References:\n")
            f.write("-"*20 + "\n")
            for ref in data['references']:
                f.write(f"- {ref}\n")

# 設置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('agent_execution.log'),
        logging.StreamHandler()
    ]
)

# 在你的主要代碼中使用
def execute_tools(parsed_call):
    try:
        # 你原有的邏輯
        output_data = {
            'answer': parsed_call['args'].get('answer', ''),
            'reflection': parsed_call['args'].get('reflection', {}),
            'references': parsed_call['args'].get('references', []),
            'search_queries': parsed_call['args'].get('search_queries', [])
        }
        
        # 保存輸出
        save_structured_output(output_data)
        logging.info(f"Successfully processed and saved output for call ID: {parsed_call.get('id')}")
        
        return output_data
    except Exception as e:
        logging.error(f"Error in execute_tools: {str(e)}")
        raise