'''
使用while循环计算1~100的累加和（包含1和100）
'''
i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)


# while i <= 5:
#     print('* ' * i)
#     i += 1


# while True:
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#     if username == 'python' or password == '123456':
#         print('欢迎光临')
#         break
#     else:
#         print('你真是笨蛋，这都不知道吗')
#         continue


# 设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字，如果遇见7和7的倍数则打印“哈~”跳过本次循环。
# while i <= 100:
#     if i % 7 != 0:
#         print(i)
#     else:
#         print('哈~')
#     i += 1


'''
要求用户输入一个字符串，遍历当前字符串（遍历就是把字符串中的每一个字符都打印出来），如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。
'''

# str1 = input('输入您的字符串儿:')
# for i in str1:
#     if i == 'q':
#         break
#     elif i == ' ':
#         continue
#     else:
#         print(i, end='')
# i = 1
# j = 1
#
# while i <= 5:
#     while j <= i:
#         print('* ', end='')
#         j = j + 1
#     print('\n')
#     j = 1
#     i = i + 1

'''
使用for循环计算数值1到用户输入数值的累加和
'''
# num = int(input('请输入您的数字儿:'))
# result = 0
# for i in range(num + 1):
#     result += i
# print(result)

# a = '中国'
# b = a * 3
# print(b)

# n = 1
# sum = 1
# while sum < 10:
#     n = n + 1
#     sum = sum + n
# print(sum)


