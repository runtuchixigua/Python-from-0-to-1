# scale = 10.0
# print(f'{scale:.2f}%')
#
#
# a = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
# print(sum(a))


# int1 = 10
# int2 = 1
# int3 = 0
# int4 = -10
# bool1 = True
# bool2 = False
# print(int1 > bool1)
# print(int1 > bool2)
# print('*************')
# print(int2 > bool1)
# print(int2 > bool2)
# print('*************')
# print(int3 > bool1)
# print(int3 >= bool2)
# print('*************')
# print(int4 > bool1)
# print(int4 > bool2)
# print('*************')
# print(bool(int1), bool(int2), bool(int3), bool(int4))
#
# print(int(bool1), int(bool2))


# a = 2
# b = 1
# print(id(a), id(b))
# # a, b = b, a
# a = a + b
# b = a - b
# a = a - b
# print(a, b)
# print(id(a), id(b))


# a = [1]
# b = a
#
# print(a, b)
# print(id(a), id(b))


# print(15%12//5+4**2)
# list1 = [1, 2, 3, 1, 1, 2]
# print(len(list1))
# list2 = ' '.join(list1)
# print(list2)
# list1 = 'name', 'age'
# print(list1)

c1 = 'abc'
c2 = 'def'
c1, c2 = c2.upper(), c1.upper()
print(c1, c2)

x = lambda x, y: x + y
print(x(1, 2))

list1 = [1, 2, 3]
set1 = {'a': 1, 'b': 2, 'c': 3}
y = lambda *a, **b: print(a, b)
y(list1, set1)
