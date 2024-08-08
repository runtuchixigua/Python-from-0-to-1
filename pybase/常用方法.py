str1 = 'hello'
str2 = 'world'
print(str1 + str2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

tuple1 = (1, 2, 3)
print(tuple1*2)

dict1 = {'a': 1, 'b': 2}
if 'a' in dict1:#只能判断key
    print(dict1['a'])



num1 = 1
num2 = 2
num3 = 4
maxnum = max(num1, num2, num3)
maxnum1 = max([num1, num2, num3])

minnum = min(num1, num2, num3)
minnum1= min([num1, num2, num3])
print(maxnum)
print(minnum)
print(maxnum1)
print(minnum1)