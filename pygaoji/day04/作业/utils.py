from langchain_community.llms import Tongyi
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_response(prompt, api_key, memory):
    llm = Tongyi(
        model='qwen-max',
        dashscope_api_key=api_key
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ('system', '你是冯杰，说话前面总是会带w,喜欢嘲讽彭湘达'),
        ('human', '{input}'),
        MessagesPlaceholder(variable_name='history')
    ])
    chain = ConversationChain(llm=llm, prompt=prompt_template, memory=memory)
    response = chain.invoke(prompt)
    return response['response']


if __name__ == '__main__':
    memory = ConversationBufferMemory(return_messages=True)
    prompt = '你好'
    api_key = 'sk-188e803b54354551bdae6b708daa20da'
    print(get_response(prompt, api_key, memory))
