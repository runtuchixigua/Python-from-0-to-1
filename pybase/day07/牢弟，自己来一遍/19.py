'''
基本语法：
def func(**kwargs):  # kwargs是变量名，返回的数据类型为字典类型
    pass

func(关键字参数）  # 参数=参数值
'''

def fuc(**kwargs):
    print(kwargs)
    print(type(kwargs))
    pass

fuc()
fuc(name= 'tom')
fuc(name= 'tom', age= 18)

