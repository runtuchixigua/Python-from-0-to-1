from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate

llm = Tongyi(
    model='qwen-max',
    dashscope_api_key='sk-188e803b54354551bdae6b708daa20da'
)

prompt_template = ChatPromptTemplate.from_messages([
    ('system', '你是一个翻译小助手，你可以将{input_language}翻译成{output_language}'),
    ('user', '用户文本：{text}\n,翻译后的语言风格：{style}')
])
text = input('请输入要翻译的文本：')
prompt_value = prompt_template.invoke({
    'input_language': '英语',
    'output_language': '汉语',
    'text': text,
    'style': '文言文'
})
result = llm.invoke(prompt_value)
print(result)
