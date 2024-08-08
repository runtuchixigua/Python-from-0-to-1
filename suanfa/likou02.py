# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# 输入：l1 =
# 输出：[8,9,9,9,0,0,0,1]
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


def addTwoNumbers1(l1, l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    l1 = ''.join([str(i) for i in l1])
    l2 = ''.join([str(i) for i in l2])
    l1 = int(l1) + int(l2)
    l1 = str(l1)
    l1 = [int(i) for i in l1]
    l1.reverse()
    return l1


# print(addTwoNumbers1(l1, l2))



def addTwoNumbers2(l1, l2):
    l1 = l1.reverse()
    l2 = l2.reverse()
    l1 = ''.join([str(i) for i in l1])
    l2 = ''.join([str(i) for i in l2])
    l1 = int(l1) + int(l2)
    l1 = str(l1)
    l1 = [int(i) for i in l1]
    l1.reverse()
    return l1
print(addTwoNumbers2(l1, l2))