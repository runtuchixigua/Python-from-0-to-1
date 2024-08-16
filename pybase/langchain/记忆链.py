from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = Tongyi(
    model='qwen-max',
    dashscope_api_key='sk-188e803b54354551bdae6b708daa20da'
)

memory = ConversationBufferMemory(return_messages=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", '你是一个乐于助人的助手'),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{input}')
])
chain = ConversationChain(llm=llm, prompt=prompt, memory=memory)
print(chain.invoke({
    'input': "我是老六"
}))
print(chain.invoke({
    'input': '我叫什么'
}))
