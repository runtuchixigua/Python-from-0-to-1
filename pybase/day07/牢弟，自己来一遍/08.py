'''
所谓的函数嵌套：就是在一个函数中又调用了另外一个函数！
基本语法：
def func1():
    ...
    func2()  # 调用了func2函数
    ...

Pycharm中存在一个专业代码调试工具 => Debug工具
通过Debug工具我们可以了解代码的执行流程，调试步骤一共分两步：① 下断点 ② 启动调试
下断点：通常放置在关键字的前面，如if、while、for以及函数的调用位置！
'''


def fuc1():
    return '1111'


def func2(a):
    if a == True:
        a = fuc1()
        return a
    else:
        return a


print(func2(1))
