import streamlit as st
from langchain_community.llms import Tongyi

# sk-188e803b54354551bdae6b708daa20da
with st.sidebar:
    st.write('请输入Tongyi API Key:')
    api_key = st.text_input('', type='password')

st.write('通义聊天机器人')
st.divider()

prompt = st.chat_input('请输入您的问题：')
llm = Tongyi(
    model='qwen-max',
    dashscope_api_key=api_key
)
result = llm.invoke(str(prompt))

with st.chat_message('user'):
    st.write(prompt)

message = st.chat_message('assistant')
message.write(str(result))
