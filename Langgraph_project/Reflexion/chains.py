from dotenv import load_dotenv
load_dotenv()
import datetime
from langchain_core.output_parsers.openai_tools import (
    PydanticToolsParser,
    JsonOutputToolsParser,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from cool_classes import AnswerQuestion, ReviseAnswer

llm = ChatOpenAI(model="gpt-4-turbo-preview")
parser = JsonOutputToolsParser(return_id=True)

actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert researcher
Current time: {time}
1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. Recommend search queries to research information and improve your answer.

Important: Please provide your final answer in Traditional Chinese, while keeping the analysis and reflection process in English."""
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Answer the user's question above using the required format. Ensure the final output is in Traditional Chinese."),
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

first_responder = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~250 word answer in Traditional Chinese."
) | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")

validator = PydanticToolsParser(tools=[AnswerQuestion])

revise_instructions = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
    - You MUST include numerical citations in your revised answer to ensure it can be verified.
    - Add a "參考資料" section to the bottom of your answer (which does not count towards the word limit). In form of:
    - [1] https://example.com
    - [2] https://example.com
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
    - The final answer must be in Traditional Chinese.
"""

revisor = actor_prompt_template.partial(
    first_instruction=revise_instructions
) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")