'''
手机通讯录管理系统
'''
users = []

def add():
    # 声明全局变量
    global users
    user = {}
    user['name'] = 'Tom'
    user['age'] = 23
    users.append(user)
    print('恭喜您，信息录入成功！')

def find():
    name = input('请输入您要查找人员姓名：')
    global users
    for i in users:
        if i['name'] == name:
            print(i)
            break
    else:
        print('很抱歉，您要搜索的人员暂不存在！')

add()
find()