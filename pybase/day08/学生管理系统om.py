stu_list = []


def menu():
    print('---------学生管理系统-----------')
    print('【1】添加学生')
    print('【2】删除学生')
    print('【3】修改学生')
    print('【4】查询学生')
    print('【5】查看全部学生')
    print('【6】退出系统')
    print('-----------------------------')


def add_stu():
    name = input('请输入你滴名字：')
    age = int(input('请输入你多老了：'))
    mobile = input('请输入你滴疯：')
    stu_list.append({'name': name, 'age': age, 'mobile': mobile})
    with open('student.txt', 'w', encoding='utf-8') as f:
        f.write(str(stu_list))
        f.close()
    print(stu_list)
    pass


def del_stu():
    name = input('请输入你想删滴那个人名字：')
    for i in stu_list:
        if i['name'] == name:
            del stu_list[stu_list.index(i)]
            with open('student.txt', 'w', encoding='utf-8') as f:
                f.write(str(stu_list))
                f.close()
        else:
            print('妹找到啊')
    print(stu_list)
    pass


def change_stu():
    name = input('请输入你想改滴那个人名字：')
    for i in stu_list:
        if i['name'] == name:
            i['age'] = input('请输入盖地年龄：')
            i['mobile'] = input('请输入盖地手机:')
        else:
            print('妹找到啊')
        with open('student.txt', 'w', encoding='utf-8') as f:
            f.write(str(stu_list))
            f.close()
    print(stu_list)

    pass


def show_info():
    name = input('请输入你想查滴那个人名字：')
    for i in stu_list:
        if i['name'] == name:
            print(i['name'], i['age'], i['mobile'])
        else:
            print('妹找到啊')
    pass


def show_all():
    for i in stu_list:
        print(i['name'], i['age'], i['mobile'])

    pass


if __name__ == '__main__':
    while True:
        menu()
        user_num = input("输入你想要的：")
        if user_num == '1':
            add_stu()
        if user_num == '2':
            del_stu()
        if user_num == '3':
            change_stu()
        if user_num == '4':
            show_info()
        if user_num == '5':
            show_all()
        if user_num == '6':
            break
