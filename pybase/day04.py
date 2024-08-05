# i = 1
# while i <= 100:
#     print('kuduan')
#     i += 1
#
# import random
#
# ran = print(random.randint(0, 100))
# print(type(ran))
# # for i in ran:
# #     print(i)


# # 请通过用户输入姓名和当前年龄，若年龄超过64岁，提示：已到退休年龄，可以退休了；否则，提示：骚年好好加油，多多创造自身价值吧！
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age > 64:
#     print("已到退休年龄，可以退休了")
# else:
#     print('骚年好好加油，多多创造自身价值吧！')

#
# 在运输货物时，通常是：每吨货物每公里运费P(元)与运输距离S(运输公里数)有关，路途越远，每公里运价越低。运输货物计算公式如下：
#
# | 每吨货物每公里运费P(元) | 运输距离S(运输公里数) |
# | :---------------------: | --------------------- |
# |           10            | s<100                 |
# |            8            | 100<=s<150            |
# |            7            | 150<=s<200            |
# |            6            | 200<=s<300            |
# |           5.5           | 300<=s<500            |
# |            5            | s>=500                |
#
# # 还需注意的是，当所付的总运费超过5000元时，商家再给予九五折优惠。请从键盘输入货物吨数、运输公里数，并使用代码求解应付的实际运费额。
# s = int(input("Enter your distance: "))
# p = 10.0
# if s > 100:
#     p = 10
# elif 100 <= s < 150:
#     p = 8
# elif 150 <= s < 200:
#     p = 7
# elif 200 <= s < 300:
#     p = 6
# elif 300 <= s < 500:
#     p = 5.5
# else:
#     p = 5
#
# price = s * p
# if price > 5000:
#     price = price * 0.95
#     print(f'应付的实际运费额已打95折为:{price}')
# else:
#     print(f'应付的实际运费额为:{price}')



# 制作用户登录系统：已知A用户注册的用户名为`heimauser`，密码是`123456`。要求如下：
#
# ​		a.登录时需要验证用户名、密码、验证码(固定验证码为`ASDF`)；
#
# ​		b.提示：系统先验证验证码是否正确，正确后再验证用户名和密码，试着使用if条件语句完成。


name = input("Enter your name: ")
password = input("Enter your password: ")
captcha = input("Enter your captcha: ")
if captcha == 'ASDF':
    if password == '123456':
        if name == 'heimauser':
            print("Hello " + name)