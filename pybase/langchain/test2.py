from langchain_community.llms import Tongyi


llm = Tongyi(
    model='qwen-max',
    dashscope_api_key="sk-188e803b54354551bdae6b708daa20da"
)
'''
import pandas as pd

# 读取默认的第一个 sheet
df_default = pd.read_excel("data_test.xlsx")

# 读取名为 "Sheet1" 的 sheet
df_sheet1 = pd.read_excel("data_test.xlsx", sheet_name="Sheet1")

# 读取索引为 0 的 sheet
df_index0 = pd.read_excel("data_test.xlsx", sheet_name=0)

# 读取多个 sheet 并存储为字典
dfs_multiple = pd.read_excel("data_test.xlsx", sheet_name=["Sheet1", "Sheet2"])

# 显示数据
print(df_default)
print(df_sheet1)
print(df_index0)
print(dfs_multiple)

'''


# result = llm.invoke('''
# 你需要对用户的反馈进行原因分类。
# 分类包括:价格过高、售后支持不足、产品使用体验不佳、其他。
# 回答格式为:分类结果:xx。
# 用户的问题是:性价比不高，我觉得不值这个价钱。
# ''')


