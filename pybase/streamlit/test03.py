from langchain_community.llms import  Tongyi

llm = Tongyi(
    model = "qwen-max",
    dashscope_api_key = "sk-188e803b54354551bdae6b708daa20da"
)


while True:
    prompt = input("请输入问题：")
    result = llm.invoke(prompt)
    print(result)