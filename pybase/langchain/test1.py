from langchain.chains import ConversationChain
from langchain.llms import OpenAI

# 初始化语言模型
llm = OpenAI(temperature=0)

# 创建对话链
conversation = ConversationChain(llm=llm)

# 进行对话
input1 = "您好"
response1 = conversation.predict(input=input1)
print(response1)

input2 = "今天天气怎么样？"
response2 = conversation.predict(input=input2)
print(response2)