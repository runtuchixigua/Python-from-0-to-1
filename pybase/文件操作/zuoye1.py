# f = open('test.txt', 'w')
# f.write('gogogo')
# f.close()
# f = open('test.txt', 'r')
# print(f.read())
# f.close()

'''
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个文件 2.txt 中保存。
'''
from random import random

# str = input('输入一个字符串:')
#
# with open('2.txt', 'w',encoding='utf8') as f:
#     f.write(str)
#     f.close()


'''
使用 PyCharm 直接创建一个文件 A.txt，写入内容："python是我用过的最好用，最优雅的计算机语言，没有之一！！！"

然后编写一个程序，读取 A 文件的内容，然后以逗号为分割符分割成三部分，将这三部分内容分别写入B.txt、C.txt、D.txt文件中。
'''

with open('A.txt', 'w', encoding='utf8') as f:
    f.write('python是我用过的最好用，最优雅的计算机语言，没有之一！！！')


def qieqieqie():
    with open('A.txt', 'r', encoding='utf8') as f:
        str = f.read()
        str = str.split('，')
    file_list = ['B.txt', 'C.txt', 'D.txt']
    for i in range(len(file_list)):
        with open(file_list[i], 'w', encoding='utf8') as f:
            f.write(str[i])


# qieqieqie()


'''
假设有一个文件 num.txt，里面存储了如下的一些数字，内容如下：

```
10
18
30
11
12
15
```

编写一个 python 程序，读取文件中的内容，存储成 python 中的列表形式：
'''
mylist = []
with open('num.txt', 'r', encoding='utf8') as f:
    for l in f:
        mylist.append(int(l))
    # print(mylist)

'''
假设有一个 python 字典如下：
```python
user_dict = {'name': 'smart', 'age': 18, 'tel': '13888888888'}
```
编写一个 python 程序，将字典的数据写入一个 user.txt 文件中，写入格式如下：
'''
# user_dict = {'name': 'smart', 'age': 18, 'tel': '13888888888'}
# with open('user.txt', 'w', encoding='utf8') as f:
#     for k, v in user_dict.items():
#         f.write(f'{k}:{v}' + '\n')

'''
下面有一个字符串：

str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

编写一个程序，从上面的字符串中随机取出4个字符，生成一个模拟验证码字符串，比如：'a01V'

'''
from random import *

str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ma = ''


def captcha():
    global ma
    for i in range(4):
        ma += str1[randint(0, len(str1) - 1)]
    print(ma)


# captcha()

# with open('word.txt', 'r', encoding='utf8') as f:
#     # print(f.read())
#     print(f.readline())
#     print(f.readlines())
#     f.close()


# score = 0
# with open('grades.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         content = line.split(',')
#         print(type(content))
#         print(content)
#         score += int(content[1])
#         print(score)
#     f.close()
#
#     print(score/5)

# sum = 0
# num = 0
# f  = open('grades.txt', 'r', encoding='utf8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     num += 1
#     sum += int(line.strip().split(',')[1])
#
# print(sum/num)
# f.close()

# cou1 = 0
# with open('word.txt', 'r', encoding='utf8') as f:
#     # content = f.read()
#     # content = content.split(' ')
#     # cou1 = content.count('itheima')
#     # print(content)
#     # print(cou1)
#     for l in f:
#         cou1  += l.count('itheima')
#     print(cou1)

# with open('aa.txt', 'r+', encoding='utf8') as f:
#     f.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     # print(f.read())
#     f.close()

# import time
# with open('flush_demo.txt', 'w', encoding='utf8') as f:
#     f.write('first line\n')
#     time.sleep(5)
#     f.write('second line\n')
#     f.flush()
#     time.sleep(5)
#     f.write('third line\n')

# def attendance(t, name, yn):
#     with open('attendance.txt', 'w', encoding='utf8') as f:
#         f.write(f'{t} {name} {yn}')
#     print(f'{t} {name} {yn} 记录完成')
#
# attendance(1,'tom','daole')
# name = input('name:')
# age = input('age:')
# tel = input('tel:')
# with open('user.txt', 'a', encoding='utf8') as f:
#     f.write(f'name:{name}\n')
#     f.write(f'age:{age}\n')
#     f.write(f'tel:{tel}\n')
#     f.write('-----------------------------------')


# fr = open('bill.txt', 'r', encoding='utf8')
# fw = open('bill.txt.bak', 'w', encoding='utf8')
# for line in fr:
#     line = line.strip().split(',')
#     if line[3] == '收入':
#         fw.write(str(line) + '\n')
# fr.close()
# fw.close()


# fr = open('dog.png', 'rb')
# fw = open('dog_1.png', 'wb')
# while True:
#     content = fr.read(1024)
#     if not content:
#         break
#     fw.write(content)
# fr.close()
# fw.close()


# import os,time
# os.rename('temp.txt','python.txt')
# time.sleep(10)
# os.remove('python.txt')

# import os
# print(os.getcwd())
# os.chdir('static')
# if not os.path.exists('images'):
#     os.mkdir('images')
# if not os.path.exists('videos'):
#     os.mkdir('videos')
# for file in os.listdir():
#     print(file)
# os.rmdir('videos')

# import shutil
#
# shutil.rmtree('static')

# num = input('num:')
# a=0
# try:
#     num = int(num)
#     a = 100 / num
#     print(a)
# except Exception as e:
#     print(e)
#     exit()
# print(a)

try:
    f = open('AI.txt', 'r', encoding='utf8')
except:
    f = open('AI.txt', 'a', encoding='utf8')
else:
    f.read()
finally:
    f.close()