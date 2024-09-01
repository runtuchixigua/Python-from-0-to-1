import re
str1 = 'ab cde 123fgh3456'
result1 = re.match('.*', str1)
print(result1.group())

str2 = '115277@qq.com'
result2 = re.match('\w+@qq.com', str2)
print(result2.group())

str3= 'g,go,goo'
result3 = re.findall('go?', str3)
print(result3)

result4 = re.findall('\d{3}',str1)
print(result4)

result5 = re.findall('\d{3,4}',str1)
print(result5)

result6 = re.findall('g+o',str3)
print(result6)