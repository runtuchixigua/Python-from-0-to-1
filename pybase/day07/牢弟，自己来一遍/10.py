dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
del dict1['a']
print(dict1)
dict1.clear()
print(dict1)

'''
结论1：全局作用域可以访问全局变量
结论2：局部作用域也可以访问全局变量
综上所述：全局变量的作用范围比较广，既可以在全局作用域中访问，也可以在局部作用域中访问！
'''

a = 1
def fuc():
    print(a)
    return a


print(a)
print(fuc())
