import re

str1 = '2itniuma'
result = re.match('^\d.*', str1)
if result:
    print(result.group())
else:
    print('匹配失败')

str2 = '2itniuma22'
result1 = re.match('^\d.*\d$', str2)
if result1:
    print(result1.group())
else:
    print('匹配失败')

str3 = '2itniuma22'
result2 = re.match('.*[^4]$', str3)
if result2:
    print(result2.group())
else:
    print('匹配失败')

str4 = 'itn222iuma'
result3 = re.search(r'\d(\d)(\d)', str4)
print(result3.group())
print(result3.group(1))
print(result3.group(2))
