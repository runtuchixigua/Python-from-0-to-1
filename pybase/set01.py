set1 = set()
print(set1)
print(type(set1))

set2 = {1, 2, 3, 4, 5}
print(set2)

set4 = {1, 22, 11, 2, 3, 44, 55, 6}
print(set4)

for i in set4:
    print(i)

list1 = [1, 2, 22, 21, 33, 44, 22, 3, 4, 5]
new_list = list()
for i in list1:
    if i not in new_list:
        new_list.append(i)
    i += 1
print(new_list)

print('--------------------------------')
set1.add(1)
set1.add(2)
set1.add(3)

set1.remove(2)

for i in set1:
   print(i)

if 1 in set1:
    print('exists')
else:
    print('not exists')
