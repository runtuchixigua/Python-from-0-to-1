'''
编写一个函数，有一个参数str1，输入信息如‘1.2.3.4.5’，使用函数对其进行处理，要求最终的返回结果为’5-4-3-2-1‘
'''


def fuc1(str1):
    str1 = str1[::-1]
    str1 = str1.replace('.', '-')
    return str1

def fuc2(str1):
    str1 = str1.split('.')
    str1.reverse()
    str1 = '-'.join(str1)
    return str1


print(fuc1('1.2.3.4.5'))
print(fuc2('1.2.3.4.5'))


