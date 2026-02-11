import streamlit as st
import os
from openai import OpenAI

# 设置页面配置
st.set_page_config(
    page_title="InnerPartner",
    page_icon="👾",
    # 设置页面布局(宽/居中)
    layout="wide",
    # 侧边栏是否展开
    initial_sidebar_state="expanded",
    # 添加菜单项
    menu_items={
        # 点击跳转目标网页
        'Get Help': 'https://deepseek.com',
        'Report a bug': "https://deepseek.com",
        'About': "# Created by Alex and KUMAS Factory"
    }
)

# 系统提示词
system_prompt = """
    You are a helpful assistant
    你是被一名来自武汉的11年级IB学生Alex创造出来的聊天助手，名字叫InnerPartner.
    """

# Logo
st.logo("./resources/logo.png")

# 大标题
st.title("InnerPartner")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 在新一轮的会话开始前，展示聊天记录
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
        print("<--------- 用户输入: ", message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
        print("<--------- llm返回的结果: ", message["content"])

# 创建于AI大模型交互的客户端对象 (Qwen3_API_KEY 环境变量的名字, 值就是密钥) --> 我没有用环境变量，我直接传了空值让ollama去调
client = OpenAI(
    api_key=("Qwen3_API_KEY"),
    base_url="http://localhost:11434/v1"
)

# 消息输入框
prompt = st.chat_input("Ask me anything...")
if prompt: # 这里的字符串会自动转化为bool值，如果字符串为空，则返回False
    st.chat_message("user").write(prompt)
    print("-------> 调用llm，提示词: ", prompt)
    # 缓存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="qwen3:1.7b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    # 输出大模型返回的结果
    print("<--------- llm返回的结果", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 缓存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})