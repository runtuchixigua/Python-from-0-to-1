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
def funcB():
    print('--- funcB func start ---')
    print('--- funcB func ---')
    print('--- funcB func end ---')

def funcA():
    print('--- funcA func start ---')
    # 调用了funcB()函数
    funcB()
    print('--- funcA func end ---')


# 只需要funcA()函数即可
funcA()

'''
Debug调试工具一共有两个按钮：① Step Over ② Step Into
Step Over：调试非函数结构，代码一行一行执行，遇到函数，不进入到函数内部，直接返回函数的执行结果
Step Into：调试函数结构代码，代码一行一行执行，遇到函数，会直接进入到函数内部，一行一行执行，从而返回结果
'''