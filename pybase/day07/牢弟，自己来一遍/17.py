'''
缺省参数（默认值参数）：就是在函数定义时为参数指定一个默认值
'''


def fuc(name, age, city='guang'):
    print(name, age, city)
    pass


fuc('tom', 18)
fuc('john', 23, city='guang111')
