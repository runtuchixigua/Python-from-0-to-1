'''
基本语法：
def func(*args):  # args是变量名，返回的数据类型为元组类型
    pass

func(位置参数)
'''
def func(*args):
    print(args)
    print(type(args))

# 使用位置传参来传递参数值
func()
func('Tom')
func('Tom', 23)
func('Tom', 23, '10086')