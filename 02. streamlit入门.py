import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="KUMAS Factory",
    page_icon="🧊",
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


# 创建标题
st.title("KUMAS Factory")
st.header("Welcome to My Data Playground")
st.subheader("Built by AlexGuo with Streamlit")


# logo
st.logo("./resources/logo.png") # 网页左上角显示logo


# 创建一个登录页面
st.write("If you want get more info, log in plz")
# 普通输入框
username = st.text_input("Username：")

# 密码框
password = st.text_input("Password：", type="password")

# 单选按钮
choice = st.radio("Choice:", ("Login", "Register"))

if st.button("Continue"):
    if choice == "Login":
        if username == "admin" and password == "666888":
            st.success("Successful")
            st.balloons()
            # 段落文字
            st.write(
                "Hi there! I’m AlexGuo, and this is my interactive data application—crafted to turn raw numbers into clear, actionable insights.")
            st.write(
                "In a world overflowing with data, the real challenge isn’t collecting it—it’s understanding it. That’s why I built this tool: to make data exploration intuitive, visual, and accessible to everyone, whether you're a seasoned analyst or just curious about what your data can tell you.")
            st.header("What You Can Do Here:")
            st.write("Upload your own datasets (CSV, Excel, and more)")
            st.write("Get instant summaries—see data types, missing values, and key statistics at a glance")
            st.write("Visualize trends interactively with dynamic charts you can filter, zoom, and explore")
            st.write("Ask questions of your data through simple, user-friendly controls")
            st.write(
                "This project reflects my belief that powerful analytics shouldn’t require complex setups or coding expertise. Behind the scenes, it’s powered by Python, pandas, and Streamlit—but all you need is curiosity.")

            st.header("About Me")
            st.subheader("My Sad XXG")

            # 图片
            st.image("./resources/xxg.png")

            st.subheader("My Favorite Song")
            st.write("------------爱在西元前------------")

            # 音频
            st.audio("./resources/Jay.mp3")

            st.subheader("My Favorite Animation")
            st.write("Lego Ninjago")

            # 视频
            st.video("./resources/Lego.mp4")
        else:
            st.error("Incorrect username or password")

    elif choice == "Register":
        if username == "admin" and password == "666888":
            st.error("User already exists")
        else:
            st.success("Successful")
            st.balloons()
    else:
        st.warning("Please select a choice")


st.write("I’m AlexGuo—a data enthusiast passionate about bridging the gap between information and insight. When I’m not building tools like this, I’m learning, experimenting, or thinking about how data can solve real-world problems.")
st.write("Feel free to explore, play around, and share your feedback. This app is a living project—and your input helps shape its future.")
st.write("Built with ❤️ using open-source tools. Free, fast, and always evolving.")