'''
在Python代码中，函数的参数可以分为两种形式：① 形式参数 ② 实际参数
形式参数：在函数定义时所指定的参数，简称形参
实际参数：在函数调用时所传递的参数，简称实参
'''

def func(name, age, mobile):  # 形参
    print(name)
    print(age)
    print(mobile)


func('Tom', 23, '10086')  # 实参