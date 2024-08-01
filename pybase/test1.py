# a1 = 11
# b1 = 17
#
# a1 = a1 + b1
# b1 = a1 - b1
# a1 = a1 - b1
#
# print(a1)
# print(b1)

# hello = 12
# a = eval('hello')
# print(PI)

a = 10000
print("hello world", a)

# 定义小数price、weight、money，输出`苹果单价9.00元／⽄，购买了5.00⽄，需要支付45.00元`。[备注：记得添加必要的注释。]
#价格
price = 9
#重量
weight = 5
#费用
money = price * weight

print(f'苹果单价{price: .2f}元／⽄，购买了{weight: .2f}⽄，需要支付{money: .2f}元')



'''
用户登录系统：用户输入用户名和密码，在控制台格式化输出用户输入的用户名和密码。[备注：记得规范化变量命名。效果如下：

>   请输入用户名：Jerry
>   请输入密码：jerry666
>   您好，您输入的用户名是Jerry, 密码是jerry666，欢迎登录系统。
'''
name = input('请输入用户名：')
keyword = input('请输入密码：')
print(f'您好，您输入的用户名是{name}, 密码是{keyword}，欢迎登录系统。')


'''
已知用户姓名、年龄、体重数据，要求从键盘上录入用户信息，并在控制台格式化输出用户信息，例如`用户姓名:TOM,年龄:18岁,当前体重是50.55kg。
[备注：记得规范化变量命名，以及添加必要的注释。]
'''
name = input('请输入姓名:')
age = input('请输入年龄:')
weight = input('请输入体重:')
print(f'用户姓名:{name},年龄:{age},当前体重是{float(weight)}kg')


# 定义⼀个小数scale=10.0，输出`数据比例是10.00%`。


