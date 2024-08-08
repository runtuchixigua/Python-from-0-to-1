'''
实际参数的传递方案一
位置参数：调用函数时根据函数定义的参数位置来传递参数。
'''


def func(name, age, mobile):
    print(name)
    print(age)
    print(mobile)


# 位置传参 => 根据函数定义时参数的位置传递参数值 => name, age, mobile
func('Rose', 24, '10010')
