'''
在Python代码中，函数的参数不仅可以使用*args，还可以使用**kwargs，除此以外，两者还可以合并在一起使用！
好处：既可以接收位置参数，又可以接收不定长参数
基本语法：
def func(*args, **kwargs):
    pass

func(位置参数, 关键字参数)

注意：如果*args和**kwargs结合在一起使用，则*args必须放在左边，**kwargs必须放置在最右边！！！
'''


def fuc(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    pass


fuc()
fuc(111,name = 'tom',age = 18)