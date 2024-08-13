'''
接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，则提示用户登录成功，其他情况则提示用户名或密码输入错误，只有3次输入机会。
'''
i = 2
while i >= 0:
    username = input('请输入你的账号：')
    password = input('请输入你的密码：')
    if username == 'admin' and password == 'admin888':
        print('用户登录成功')
        break
    else:
        print(f'用户名或密码输入错误，您还有{i}次输入机会')
    i -= 1