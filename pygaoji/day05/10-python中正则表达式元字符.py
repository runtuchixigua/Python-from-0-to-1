import re
#万能
str1 = ' abcdefg[;='
result1 = re.match('.',str1)
print(result1.group())

result2 = re.findall('[aeiou]',str1)
print(result2)

result3 = re.findall('[^aeiou]',str1)
print(result3)

print('--------')
result4 = re.match('\s',str1)
print(len(result4.group()))

result7 = re.findall('\S',str1)
print(result7)

result6 = re.findall('\W',str1)
print(result6)

print('--------')
result5 = re.findall('\w',str1)
print(result5)