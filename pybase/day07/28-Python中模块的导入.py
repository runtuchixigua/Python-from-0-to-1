'''
在Python代码中，模块分为两种形式：系统模块 和 自定义模块
导入方式通常可以使用：① import ② from

案例：导入math数学模块，求数字9的平方根
'''
# 导入方式一 => import
# import math
# 调用模块中的方法（函数） => 模块名称.方法名()
# print(math.sqrt(9))


# 导入方式二 => from
# from math import *
from math import sqrt
# 调用模块中的方法（函数） => 方法名()
print(sqrt(9))