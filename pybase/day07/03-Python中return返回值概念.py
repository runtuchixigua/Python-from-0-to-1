'''
思考：在其他的编程语言中，一个函数只能返回一个结果；Python中函数也是这样么？
'''

def func():
    return 10, 20, 30


print(func())
print(type(func()))

'''
结论2：在Python代码中，函数可以返回多个结果，其是以元组的方式返回的！
'''