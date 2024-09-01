import re
str = '1111hello world22222hello ai'
result = re.finditer(r'hello (world|ai)', str)
for i in result:
    print(i.group())


