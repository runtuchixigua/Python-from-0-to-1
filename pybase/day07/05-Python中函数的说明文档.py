'''
函数的说明文档就是函数的说明书，我们在定义过程中，往往需要先定义函数，当函数定义完后，在编写说明文档！
案例：定义一个函数，用于求两个数的和
'''
# 1. 定义函数
def sum_num(num1, num2):
    # 2. 编写说明文档
    '''
    sum_num()函数主要用于求两个数的累加结果
    :param num1: int类型，代表第一个参数
    :param num2: int类型，代表第二个参数
    :return: 返回两个数的累加结果
    '''
    result = num1 + num2
    return result

# 3. 查看函数的说明文档
# 使用help()函数
help(sum_num)
# 使用PyCharm还可以使用Ctrl + Q快捷键
sum_num()
