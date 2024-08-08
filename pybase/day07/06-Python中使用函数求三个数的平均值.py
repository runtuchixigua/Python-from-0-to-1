'''
需求：使用函数求解三个数平均值
'''
def avg_num(num1, num2, num3):
    '''
    avg_num()函数，用于求参数的平均值
    :param num1: int，第一个参数
    :param num2: int，第二个参数
    :param num3: int，第三个参数
    :return: 返回三个数的平均值
    '''
    return (num1 + num2 + num3) / 3

# 调用avg_num函数
print(avg_num(10, 20, 30))