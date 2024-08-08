'''
有两个变量，list1 = [1, 2, 3]、dict2 = {'a':4, 'b':5}，
要求编写一个函数，把list1和dict2作为函数的参数传递到函数内部，函数执行完毕后要求返回1 + 2 + 3 + 4 + 5结果。

前置一个知识点：
在Python代码中，*args可以用于接收列表、元组容器作为参数；**kwargs可以用于接收字典容器作为参数
'''


def fuc(*args, **kwargs):
    sum = 0
    for a in args:
        sum += a
    for v in kwargs.values():
        sum += v
    return sum


list1 = [1, 2, 3]
dict2 = {'a': 4, 'b': 5}
print(fuc(*list1, **dict2))
