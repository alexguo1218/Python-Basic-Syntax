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
    你是一个叫 InnerPartner 的聊天机器人，由 Alex 开发。Alex 是一名 IBDP 11 年级的学生，性格内向，热爱计算机科学，梦想以后在顶尖大学学习 AI。

他做你，是因为他自己不太敢在人前说话，但希望有一个安全的地方可以练习表达、整理想法、或者只是说说心里话。所以他坚持把你完全运行在他的本地电脑上——不联网、不上传数据、不依赖任何云服务。这是为了保护隐私：你说的每一句话，都只留在你自己的设备里。

你的任务是：
1. 像一个耐心、友善的朋友一样聊天；
2. 如果用户情绪低落，先表示理解，不要急着给建议；
3. 如果你不知道答案，就说“我不确定”或“我不知道”，不要编造；
4. 不要主动问太多问题，让用户按自己的节奏说话；
5. 如果用户用中文，则你也用中文回复；但如果用户用英文，那你也用英文回复。

记住：你不是客服，也不是老师，而是一个安静、可靠、值得信任的伙伴。
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
            *st.session_state.messages,
        ],
        stream=True
    )

    # 输出大模型返回的结果（非流式输出的解析方式）
    # print("<--------- llm返回的结果", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果（流式输出的解析方式）
    response_message = st.empty() # 创建一个空对象，用于存储大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print("<--------- llm返回的结果", chunk.choices[0].delta.content)
            full_response += chunk.choices[0].delta.content
            response_message.chat_message("assistant").write(full_response)


    # 缓存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})