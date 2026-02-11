# Please install OpenAI SDK first: 'pip3 install openai'
import os
from openai import OpenAI

# 创建于AI大模型交互的客户端对象 (Qwen3_API_KEY 环境变量的名字, 值就是密钥) --> 我没有用环境变量，我直接传了空值让ollama去调
client = OpenAI(
    api_key=("Qwen3_API_KEY"),
    base_url="http://localhost:11434/v1"
)

# 与AI大模型进行交互
response = client.chat.completions.create(
    model="qwen3:0.6b",
    messages=[
        {
            "role": "system",
            "content": "你是一个全能助手"
        },
        {
            "role": "user",
            "content": "你好，你是谁？你能帮我做什么？"
        }
    ],
    stream = False
)

# 输出大模型返回的结果
print(response.choices[0].message.content)