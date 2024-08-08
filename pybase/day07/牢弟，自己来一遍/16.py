'''
实际参数的传递方案二
关键字参数：函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
'''


def fuc(name, age, city, country):
    return name + str(age) + city + country

print(fuc(name='tom',city='xiamen',age=18,country='china'))
