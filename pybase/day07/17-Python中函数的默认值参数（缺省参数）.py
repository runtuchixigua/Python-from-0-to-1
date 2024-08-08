'''
缺省参数（默认值参数）：就是在函数定义时为参数指定一个默认值
'''
def student(name, age, gender='male'):
    print(name)
    print(age)
    print(gender)


# 调用student函数
student('张佳乐', 23)
student('姚真真', 22, 'female')

'''
注意：在函数参数定义时，普通参数要放置在左侧，缺省参数必须放置普通参数的右侧
'''