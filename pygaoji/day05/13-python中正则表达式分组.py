import re
str1 = 'abcd123def3443aaa6677'

result = re.finditer(r'([0-9])(\d)\2\1', str1)
for i in result:
    print(i.group())


result1 = re.finditer(r'([a-z])\1\1', str1)
for i in result1:
    print(i.group())


