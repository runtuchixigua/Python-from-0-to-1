import streamlit as st
from util import get_response
from langchain.memory import ConversationBufferMemory

with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password")

st.title("通义聊天机器人")



st.chat_message("AI").markdown("你好，我是通义聊天机器人，你可以问我任何问题。")
st.chat_message("human").markdown("")