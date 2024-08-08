'''
手机通讯录管理系统
'''
user = []


def add(name, age):
    user.append(name)
    user.append(age)
    print(user[0], '添加成功')
    return user
    pass


def find(name):
    if name in user:
        return 'yes yes yes'
    else:
        return 'no no no'
    pass


print(add('Tom', 18))
print(find('Tom'))

user1 = ['hello', 'python']
if 'hell' in user1:
    print(user1)
else:
    print('no no no')
