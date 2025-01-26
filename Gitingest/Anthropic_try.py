from dotenv import load_dotenv
import os
import anthropic

# 載入 .env 文件
load_dotenv()

# 從環境變量獲取 API 密鑰
api_key = os.getenv("ANTHROPIC_API_KEY")

# 創建 Anthropic 客戶端
client = anthropic.Anthropic(
    api_key=api_key
)

# 發送消息
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)

print(message.content)