'''
基本语法：
import 模块名称 as 别名
from 模块名称 import 功能名称 as 别名
'''
# 获取操作系统信息
import sys as s
print(s.platform)

# 导入os模块中的mkdir()方法，为其定义一个别名
from os import mkdir as mdir
mdir('images')