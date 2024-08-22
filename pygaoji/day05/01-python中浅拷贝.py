import copy

list1 = [1, 2, 3, [4, 5]]
list2 = copy.copy(list1)
print(list1)
print(list2)
print(id(list1[3]))
print(id(list2[3]))
list1[3][0] = 100
print(list1)
print(list2)
