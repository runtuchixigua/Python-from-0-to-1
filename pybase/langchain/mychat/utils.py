from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def get_response(prompt, memory, api_key):
    """
    根据提供的prompt和api_key获取对话模型的响应。

    参数:
    - prompt: str，对话的提示信息。
    - memory: ConversationBufferMemory，用于存储对话历史记录。
    - api_key: str，阿里云的DashScope API密钥，用于访问模型。

    返回:
    - str，模型的响应结果。
    """
    # 初始化通义大模型实例，并指定使用的模型和API密钥
    llm = Tongyi(
        dashscope_api_key=api_key,
        model='qwen-max'
    )
    # 定义对话模板，包括系统消息、历史消息占位符和用户输入
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个暴躁的AI助手,擅长冷嘲热讽"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    # 初始化对话链，设置模型、记忆体和提示模板
    chain = ConversationChain(llm=llm, memory=memory, prompt=prompt_template)
    # 调用对话链并返回响应
    response = chain.invoke({prompt})
    return response['response']

if __name__ == '__main__':
    # 初始化对话记忆体，确保返回消息
    memory = ConversationBufferMemory(return_messages=True)
    # 设置对话提示信息
    prompt = '你是谁'
    # 设置API密钥
    api_key = 'sk-188e803b54354551bdae6b708daa20da'
    # 获取并打印模型响应
    print(get_response(prompt, memory, api_key))
