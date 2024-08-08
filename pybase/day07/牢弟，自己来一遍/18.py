'''
基本语法：
def func(*args):  # args是变量名，返回的数据类型为元组类型
    pass

func(位置参数)
'''


def fuc(*args):
    print(args)
    print(type(args))
    pass


fuc()
fuc('name', 18)
fuc('a', 1, [2, 3, 4])
