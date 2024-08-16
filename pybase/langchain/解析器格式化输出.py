from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

llm = Tongyi(
    model='qwen-max',
    dashscope_api_key='sk-188e803b54354551bdae6b708daa20da'
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "{output_instructions}"),
    ("human", "请帮我生成5个{subject}色系风格的十六进制颜色代码")
])

output_parser = CommaSeparatedListOutputParser()
output_instructions = output_parser.get_format_instructions()

prompt = prompt_template.invoke({
    "subject": "莫兰迪",
    "output_instructions": output_instructions
})
result = llm.invoke(prompt)
print(result)

result = output_parser.invoke(result)
print(result)
