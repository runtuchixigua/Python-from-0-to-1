import copy
tuple1 = (1,2,3,(4,5))
tuple2 = copy.deepcopy(tuple1)


print(tuple1)
print(tuple2)
print(id(tuple1[3]))
print(id(tuple2[3]))