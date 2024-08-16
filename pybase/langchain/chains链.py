from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

llm = Tongyi(
    model='qwen-max',
    dashscope_api_key='sk-188e803b54354551bdae6b708daa20da'
)

prompt = ChatPromptTemplate.from_messages([
    ('system', '{out_instructions}'),
    ('user', '请生成5个{subject}色系的十六进制值')
])
output_parser = CommaSeparatedListOutputParser()
output_instructions = output_parser.get_format_instructions()

chain = prompt | llm | output_parser
result = chain.invoke({
    'subject': '莫兰迪',
    'out_instructions': output_instructions
})
print(result)
