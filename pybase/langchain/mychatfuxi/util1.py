from langchain_community.llms import Tongyi
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain


def get_response(prompt, api_key, memory):
    llm = Tongyi(
        dashscope_api_key=api_key,
        model='qwen-max'
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ('system', '你是一个AI助手，请根据上下文回答问题。'),
        ('human', '{input}'),
        MessagesPlaceholder(variable_name='history')
    ])
    chain = ConversationChain(
        llm=llm,
        prompt=prompt_template,
        memory=memory
    )
    response = chain.invoke(prompt)
    return response['response']


if __name__ == '__main__':
    api_key = 'sk-188e803b54354551bdae6b708daa20da'
    memory = ConversationBufferMemory(return_messages=True)
    print(get_response('你好', api_key, memory))
