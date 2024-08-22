# 导入streamlit库，用于创建网页应用
import streamlit as st
# 导入ConversationBufferMemory类，用于对话记忆
from langchain.memory import ConversationBufferMemory
# 导入get_response函数，用于获取聊天机器人的响应
from utils import get_response

# 在侧边栏中获取用户的OpenAI API密钥
with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password")

# 设置网页标题
st.title("通义聊天机器人")
# 初始化对话记忆和消息列表
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(return_messages=True)
    st.session_state['messages'] = [{"role": "ai", "content": "你好，我是通义聊天机器人，有什么可以帮助你的吗？"}]

# 显示历史消息
for message in st.session_state['messages']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 获取用户输入的问题
prompt = st.chat_input("请输入你的问题:")
if prompt:
    # 检查是否输入了API密钥
    if not api_key:
        st.warning("请输入API Key")
        st.stop()
    # 将用户问题添加到消息列表中
    st.session_state['messages'].append({"role": "human", "content": prompt})
    st.chat_message("human").markdown(prompt)

    # 显示加载动画，模拟思考过程
    with st.spinner("思考中..."):
        content = get_response(prompt, st.session_state['memory'], api_key)
    # 将机器人的回答添加到消息列表中
    st.session_state['messages'].append({"role": "ai", "content": content})
    st.chat_message("ai").markdown(content)
