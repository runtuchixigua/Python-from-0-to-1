'''
定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值
'''


def max(a, b):
    if a > b:
        return a
    else:
        return b


# print(max(11, 2))

'''
* 完成一个函数，给定三个值。判断你给的值是否可以组成一个三角形，如果能组成三角形，返回 True，否则返回 False。

提示：

* 三角形成立必须两边之和大于第三边

  * 第一步：定义函数，并接受三个参数

  * 第二步：任意相加其中的两条边判断是否大于第三边，要保证三条边中任意两边之和都大于第三边
'''


def triangle(a, b, c):
    list1 = [a, b, c]
    list1.sort()
    if list1[0] + list1[1] > list1[2]:
        return True
    else:
        return False


# print(triangle(1, 2, 2))


'''
计算100到200的数字之和，要求用for循环配合range实现；
'''


def calculate():
    result = 0
    for i in range(100, 201):
        result += i
    return result


# print(calculate())


'''
计算100-200之间的奇数之和，要求用for循环配合range实现；
'''


def calculateji():
    result = 0
    for i in range(101, 201, 2):
        result += i
    return result


# print(calculateji())

'''
使用 for 循环配合 range 打印出如下图形：
*
* *
* * *
* * * *
* * * * *
'''


def func1():
    for i in range(6):
        print(i * '* ')
    i += 1


# func1()


# i = [i for i in range(10)]
# print(i)
'''
已知列表num， 完成列表num的**去重**，并使用一行代码完成num列表奇数的筛选
num = [1,1,2,3,4,4,5]
'''
num = [1, 1, 2, 3, 4, 4, 5]


def func2(num):
    newnum = []
    for i in range(len(num)):
        if i not in newnum:
            if num[i] % 2 != 0:
                newnum.append(num[i])
    i += 1
    return newnum


# print(func2(num))


# i = [i for i in range(10) if i % 2 == 0]
# print(i)

'''
用列表推导式求出100（包含100）以内4的倍数：4 8 12 ...
'''

yibo = [i for i in range(101) if i % 4 == 0]
# print(yibo)

'''
使用 lambda 表达式，定义一个匿名函数，计算三个数字的和并返回，写完之后进行调用。
'''
ts = lambda x, y, z: x + y + z
# print(ts(1, 2, 3))


'''
定义一个函数func，设置两种不定长形参，按照如下方式进行调用：
func(1, 2, 3, a=4, b=5, d=6)
实现 func 函数的代码，计算传入参数的数字之和。
'''


def func(*a, **b):
    result = 0
    for i in a:
        result += i
    i += 1
    for i in b.values():
        result += i
    i += 1
    return result


# print(func(1, 2, 3, a=4, b=5, d=6))


list2 = [(i, j) for i in range(1, 3) for j in range(3)]
# print(list2)

'''
输出 9*9 乘法口诀表

**提示：**

**1. 使用for循环嵌套，分行与列考虑，共9行9列，i控制行，j控制列  **

**2. 使用range函数**
'''


def jiujiu(x, y):
    for i in range(1, x):
        for j in range(1, i + 1):
            print(f'{i}*{j}={i * j}', end='\t')

        print()



jiujiu(10, 10)


# c = 1
#
# print(id(c))
# def func3():
#     global c
#     print(id(c))
#     c += 1
#     print(c)
#     print(id(c))
#
#
# func3()
# print(c)
# print(id(c))