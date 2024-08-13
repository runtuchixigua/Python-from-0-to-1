'''
定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。 [上传文件题]
'''
import random

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def captchar(str1):
    numstr = ''
    for i in range(4):
        r = random.randint(0, len(str1))
        numstr += str1[r]
    print(numstr)


captchar(str1)
