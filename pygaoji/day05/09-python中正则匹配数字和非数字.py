import re
str1 = 'a1b2c3d4e5f6g'
result = re.findall(r'\D',str1)
if result:
    print(result)