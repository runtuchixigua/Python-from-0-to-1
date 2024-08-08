'''
思考：当我们定义一个函数时，如果函数没有返回值，则打印这个函数，默认返回啥？
'''

def func():
    print('hello python!')
    # 隐藏条件
    # return None

print(func())  # 打印func()函数的返回值

'''
结论3：在Python代码中，如果一个函数没有返回值，则打印函数的返回结果时，默认返回None
'''