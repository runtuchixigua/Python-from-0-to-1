from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
print(memory.load_memory_variables({}))

memory.save_context({'input': '我叫老六'}, {'output': '记住了，老六'})
print(memory.load_memory_variables({}))

prompt = ChatPromptTemplate.from_messages([
    ('system', '你是一个乐于助人的AI助手'),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{user_input}')
])

llm = Tongyi(
    model='qwen-max',
    dashscope_api_key='sk-188e803b54354551bdae6b708daa20da'
)

chain = prompt | llm
history = memory.load_memory_variables({})['history']
result = chain.invoke({
    'user_input': '我是谁',
    'history': history
})
print(result)
