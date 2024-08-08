'''
自定义模块的测试需求：这个测试代码只会在当前页面执行，加载到其他页面以后就不会执行了
__name__：魔术变量（有特殊功能的变量，随着页面的不同，__name__可以返回不同的结果）
__name__
当前页面：返回值__main__字符串
其他页面：返回值my_module2模块名称
'''

def sum_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

# 测试模块中的函数
if __name__ == '__main__':
    print(sum_num(10, 20))
    print(sub_num(20, 10))