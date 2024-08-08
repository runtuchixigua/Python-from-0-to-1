'''
实际参数的传递方案二
关键字参数：函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
'''
def func(name, age, mobile):
    print(name)
    print(age)
    print(mobile)

# 关键字传参 => 通过“键=值”形式加以指定 => 参数名=参数值
func(name='Rose', age=24, mobile='10010')