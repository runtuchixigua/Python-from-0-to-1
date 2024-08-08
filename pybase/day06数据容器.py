import numpy as np


def dm01字符串():
    # 99乘法表
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print(f'{i}*{j} = {i * j}', end=' ')
    #         j += 1
    #     print()
    #     i += 1

    # 多行字符串
    str1 = '''
    lsdalakdskfj
    lkasdjflkj
    alkdsjf
    '''

    # 特殊字符串定义
    str2 = 'I\'m boy'
    str3 = "I'm boy"
    print(str2)
    print(str3)

    # 字符串索引下标
    str4 = 'itniuma'
    print(str4[0])
    print(str4[1])
    print(str4[2])
    print(str4[3])
    print(str4[4])
    print(str4[5])
    print(str4[6])
    print('-' * 88)
    print(len(str4))
    print('-' * 88)
    for i in str4:
        print(i)

    # 切片
    str4 = 'itniuma'
    str5 = '12345678'
    # print(str4[1:5:2])
    # print(str4[1::-1])
    print(str5[::-1])
    print(str5[-2::-1])
    print(str5[1::-1])
    print(str5[7:1:-1])
    print('----------------------')
    # 下面交叉了这个打印不出来
    print(str5[1:8:-1])
    print(str5[8:1:1])

    # 子串查找和统计方法
    str6 = ' 1 hello itniuma hello python'
    print(str6.find('hello', 10))
    print(str6.count('hello'))

    # 字符串修改方法

    print(str.replace('apple', 'peach'))
    print(str.split(','))
    a = str.split(',')
    b = ','.join(a)
    print(b)

    str1 = 'apple,banana,orange'
    str2 = '123'
    print(str1.isdigit())
    print(str2.isdigit())

    password = input('请输入你的密码:')
    if len(password) == 6 and password.isdigit():
        print('yes yes yes')
    else:
        print('no no no no no no no no no no no no no no no no no no no no')

    a = '123'
    print(a.isalnum())
    print(a.isdigit())
    pass


def dm02列表():
    list1 = ['apple', 'banana', 'cherry', 'peach', 'orange']
    print(list1)
    print(list1[2])
    print(list1[-1])
    np1 = np.array(list1)
    print(np1)
    list2 = np1.reshape(5, 1)
    print(list2)
    print(type(list2))
    list3 = np.asmatrix(list1)
    list4 = np.array(list1)
    print(list3)
    print(list4)
    print(type(list3))
    print(type(list4))

    list5 = list3.T
    print(list5)
    print(type(list5))
    # A = np.asmatrix([1, 2], [3, 4])
    # print(A)
    list1.append('applepen')
    print(list1)

    del list1[0]
    print(list1)

    list1.remove('banana')
    print(list1)

    print('-------------------------------')
    i = 0
    while i < len(list1):
        print(list1[i])
        i += 1

    print('-------------------------------')
    for i in range(0, len(list1)):
        print(list1[i])

    pass


def dm03矩阵():
    data1 = [1, 2, 3, 4, 5]
    data2 = [6, 7, 8, 9, 10]
    data3 = [11, 12, 13, 14, 15]
    data4 = [16, 17, 18, 19, 20]
    data5 = [21, 22, 23, 24, 25]
    data6 = [26, 27, 28, 29, 30]
    data = np.array([[data1, data2, data3], [data4, data5, data6]])

    print(data)
    print(data[0, 0, 0])
    print(data[0, 0, :-2:-1])
    pass


def dm04列表索引修改():
    data1 = ['apple', 'banana', 'cherry', 'peach', 'orange']
    data1[0] = 'wtf'
    print(data1)
    if 'cherry' in data1:
        print('cherry exist')
    else:
        print('cherry not exist')

    print(data1[::-1])
    data1.reverse()
    print(data1)
    data1.sort(reverse=True)
    print(data1)


def dm05列表嵌套():
    data1 = ['apple', 'banana', 'cherry', 'peach', 'orange']
    data2 = [6, 7, 8, 9, 10]
    data3 = [data1, data2]
    print(data3)
    data4 = np.array(data3)
    print(data4)
    print(data3[1][2])

    data4 = [['apple', 'banana', 'cherry', 'peach', 'orange'], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    print(data4[0][4])


def dm06元祖定义访问():
    tuple1 = (10,)
    print(tuple1)
    tuple2 = (10, 20, 30, 40)
    print(tuple2[2])
    # 元祖不可修改
    # del tuple2[1]
    # print(tuple2)
    print(len(tuple2))


def dm07字典定义和应用():
    dict1 = {'name': 'runtu', 'age': 20, 'gender': 'man'}
    print(dict1)
    print(type(dict1))
    print(dict1['name'])
    print(dict1['age'])
    dict1['address'] = '福建省厦门市'
    print(dict1)
    del dict1['gender']
    print(dict1)
    dict1['age'] = 22
    print(dict1)


def dm01_作业():
    '''
    如果需要使用变量保存以下字符串，我们该如何书写代码
    鲁迅说:"我没有说过这句话"
    '''
    str1 = '我没有说过这句话'

    '''
    做一个简单的用户信息管理系统：
    提示用户依次输入姓名，年龄和爱好
    并且在输入完成之后，一次性将用户输入的数据展示出来
    '''
    # dict1 = {'name': '', 'age': '', 'hobby': ''}
    # dict1['name'] = input('请输入姓名:')
    # dict1['age'] = input('请输入年龄:')
    # dict1['hobby'] = input('请输入爱好:')
    # print(dict1)
    # print(type(dict1))

    '''
    现有字符串如下，请使用切片提取出ceg
    words = "abcdefghi"
    '''
    # words = "abcdefghi"
    # print(words[2:-2:2])

    '''
    有如下两行代码：
    tuple1 = (2)
    tuple2 = (2,)
    请问tuple1与tuple2有什么不同
    '''
    # tuple1 = (2)
    # tuple2 = (2,)
    # print(type(tuple1))
    # print(type(tuple2))

    '''
    现有：tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")
    我想获得“alisi”这个内容，你能否想到三种方法来做？
    '''
    tuple1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
    print(tuple1[2])
    print(tuple1[tuple1.index('alisi')])
    print(tuple1[-3])
    print(len(tuple1))

    pass


def dm02_高级作业():
    '''
    james需要在一个字符串'hello python'中查找python这个关键字，如何实现？
    '''
    # str1 = 'hello python'
    # print(str1.find('python'))

    '''
    将下列两个列表合并，将合并后的列表去重，之后降序并输出

    list1 = [11, 45, 34, 51, 90]
    list2 = [4, 16, 23, 0]
    '''
    list1 = [11, 45, 34, 51, 90]
    list2 = [4, 16, 23, 0 ]
    list3 = list1 + list2
    print(list3)
    # a = len(list3)
    # for i in range(0, a):
    #     for j in range(0, a):
    #         if list3[i] < list3[j]:
    #             list3[i], list3[j] = list3[j], list3[i]
    #         j += 1
    #     i += 1
    # new_list = []
    # for i in range(0, len(list3)):
    #     if list3[i] not in new_list:
    #         new_list.append(list3[i])
    # print(new_list)
    #-----------------------------------

    list3 = set(list3)
    print(list3)
    list3 = list(list3)
    list3.sort(reverse=True)
    print(list3)


    '''
    现有列表：
    namelist =["tom","kaisa","alisi",["xiaoming","songshu"]]
    现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
    并且向小列表中添加一个元素“python”
    '''
    # namelist = ["tom", "kaisa", "alisi", ["xiaoming", "songshu"]]
    #
    # print(type(namelist[3]))
    # namelist[3].append("python")
    # tuple1 = (namelist[0], namelist[1], namelist[2])
    # print(type(tuple1))
    # namelist.remove(namelist[0])
    # namelist.remove(namelist[0])
    # namelist.remove(namelist[0])
    # namelist.append(tuple1)
    # print(namelist)

pass

if __name__ == '__main__':
    # dm03矩阵()
    # dm04列表索引修改()
    # dm05列表嵌套()
    # dm06元祖定义访问()
    # dm07字典定义和应用()
    # dm01_作业()
    dm02_高级作业()
    print('-------End------')
