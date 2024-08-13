info = [{'name': 'Tom', 'age': 18, 'mobile': '13578664321'}, {'name': 'Mary', 'age': 18, 'mobile': '19920187732'},
        {'name': 'Jennifier', 'age': 18, 'mobile': '18862357791'}]


def print_info():
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员信息')
    print('2: 删除学员信息')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 遍历输出所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def add_info():
    name = input('请输入姓名:')
    age = input('请输入年龄:')
    mobile = input('请输入电话:')

    # global info

    for i in info:
        if i['name'] == name:
            print('该用户已存在')
            return
    info_dict = {}
    info_dict['name'] = name
    info_dict['age'] = age
    info_dict['mobile'] = mobile
    info.append(info_dict)
    print(info)


def del_info():
    name = input('输入要删除学员的姓名:')
    # global info
    for i in info:
        if i['name'] == name:
            del info[info.index(i)]
            print('学员删除成功')
            print(info)
            return
    print('妹找到啊')
    return


def change_info():
    name = input('输入要修改学员的姓名:')
    # global info
    for i in info:
        if i['name'] == name:
            new_name = input('输入新名字:')
            new_age = input('输入新年龄:')
            new_mobile = input('输入新手机号:')
            info[info.index(i)]['name'] = new_name
            info[info.index(i)]['age'] = new_age
            info[info.index(i)]['mobile'] = new_mobile
            print('学员修改成功')
            print(info)
            return
    print('妹找到啊')
    return


def show_info(name):
    # global info
    for i in info:
        if i['name'] == name:
            print(f'名字:{i["name"]} 年龄:{i["age"]} 电话:{i["mobile"]}')
            return
    print('妹找到啊')
    return


def show_all():
    # global info
    for i in info:
        print(f'名字:{i["name"]} 年龄:{i["age"]} 电话:{i["mobile"]}')

    return


while True:
    print_info()

    user_num = int(input('请输入您要执行的功能序号：'))

    if user_num == 1:
        print('添加学员信息')
        add_info()
    elif user_num == 2:
        print('删除学员信息')
        del_info()
    elif user_num == 3:
        print('修改学员信息')
        change_info()
    elif user_num == 4:
        print('查询学员信息')
        name = input('输入要查询学员的姓名:')
        show_info(name)
    elif user_num == 5:
        print('查询全部学员信息')
        show_all()
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('信息输入错误')
