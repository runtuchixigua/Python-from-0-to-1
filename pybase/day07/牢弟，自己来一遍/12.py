'''
global的作用：在函数内部（局部作用域）中声明全局变量，一个变量一旦声明以后，则后续使用就相当于操作全局变量
注意：① 只能定义在函数内部 ② 只能用于声明，不能用于赋值操作
'''


def func1():
    global x
    return x


x = 100
print(x)
print(func1())


num = 1
def func2():
    global num
    num += 1
    return num


print(func2())
print(num)