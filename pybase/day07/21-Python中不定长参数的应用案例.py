'''
有两个变量，list1 = [1, 2, 3]、dict2 = {'a':4, 'b':5}，要求编写一个函数，把list1和dict2作为函数的参数传递到函数内部，函数执行完毕后要求返回1 + 2 + 3 + 4 + 5结果。

前置一个知识点：
在Python代码中，*args可以用于接收列表、元组容器作为参数；**kwargs可以用于接收字典容器作为参数
'''
# 1. 定义一个函数
def func(*args, **kwargs):
    sum = 0
    for i in args:  # (1, 2, 3)
        sum += i
    for v in kwargs.values():
        sum += v
    print(sum)

# 2. 定义两个变量
list1 = [1, 2, 3]
dict2 = {'a':4, 'b':5}

# 3. 调用函数func以后，返回结果 => 1+2+3+4+5
func(*list1, **dict2)  # 把list1传递给args参数；dict2传递给kwargs
