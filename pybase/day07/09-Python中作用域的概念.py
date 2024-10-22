'''
什么是作用域？所谓的作用域就是变量的作用范围（就是变量在哪里可以使用，在哪里不可以使用）
没有函数之前，变量在任意位置都可以直接使用。有了函数以后，作用域被强制划分为两种形式：
① 全局作用域
def func():
    ② 局部作用域

随着作用域的出现，变量也被强制划分为两种形式：
① 在全局作用域中定义的变量 => 全局变量
② 在局部作用域中定义的变量 => 局部变量
'''
# 全局变量
num = 10
def func():
    # 局部变量
    num = 100