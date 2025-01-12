import json
import random
from collections import defaultdict
from typing import List

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langgraph.prebuilt import ToolInvocation, ToolExecutor

from chains import parser

search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search, max_results=5)
tool_executor = ToolExecutor([tavily_tool])


# def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
#     tool_invocation: AIMessage = state[-1]
#     parsed_tool_calls = parser.invoke(tool_invocation)
#     ids = []
#     tool_invocations = []
#     for parsed_call in parsed_tool_calls:
#         for query in parsed_call["args"]["search_queries"]:
#             tool_invocations.append(
#                 ToolInvocation(
#                     tool="tavily_search_results_json",
#                     tool_input=query,
#                 )
#             )
#             ids.append(parsed_call["id"])

#     outputs = tool_executor.batch(tool_invocations)

#     outputs_map = defaultdict(dict)
#     for id_, output, invocation in zip(ids, outputs, tool_invocations):
#         outputs_map[id_][invocation.tool_input] = output

#     tool_messages = []
#     for id_, query_outputs in outputs_map.items():
#         tool_messages.append(
#             ToolMessage(content=json.dumps(query_outputs), tool_call_id=id_)
#         )

#     return tool_messages
# tool_executor.py
from utils import save_structured_output

def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
    tool_invocation: AIMessage = state[-1]
    print("Tool invocation:", tool_invocation)
    parsed_tool_calls = parser.invoke(tool_invocation)
    print("Parsed tool calls:", parsed_tool_calls)
    
    for parsed_call in parsed_tool_calls:
        # 保存輸出
        output_data = {
            'answer': parsed_call['args'].get('answer', ''),
            'reflection': parsed_call['args'].get('reflection', {}),
            'references': parsed_call['args'].get('references', []),
            'search_queries': parsed_call['args'].get('search_queries', [])
        }
        save_structured_output(output_data)
    
    ids = []
    tool_invocations = []
    
    for parsed_call in parsed_tool_calls:
        # 檢查parsed_call的結構
        print("Parsed call structure:", parsed_call)
        
        # 根據實際結構調整訪問方式
        try:
            # 如果是單一查詢而不是查詢列表
            if isinstance(parsed_call.get("args", {}), str):
                query = parsed_call["args"]
                tool_invocations.append(
                    ToolInvocation(
                        tool="tavily_search_results_json",
                        tool_input=query,
                    )
                )
                ids.append(parsed_call["id"])
            # 如果是查詢列表
            elif "search_queries" in parsed_call.get("args", {}):
                for query in parsed_call["args"]["search_queries"]:
                    tool_invocations.append(
                        ToolInvocation(
                            tool="tavily_search_results_json",
                            tool_input=query,
                        )
                    )
                    ids.append(parsed_call["id"])
        except Exception as e:
            print(f"Error processing parsed call: {e}")
            continue
    
    outputs = tool_executor.batch(tool_invocations)
    outputs_map = defaultdict(dict)
    
    for id_, output, invocation in zip(ids, outputs, tool_invocations):
        outputs_map[id_][invocation.tool_input] = output
    
    tool_messages = []
    for id_, query_outputs in outputs_map.items():
        tool_messages.append(
            ToolMessage(content=json.dumps(query_outputs), tool_call_id=id_)
        )
    
    return tool_messages