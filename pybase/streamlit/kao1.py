'''
定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果
例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6） [上传文件题]
'''
list1 = [1, 2, 3]
dict1 = {'a': 4, 'b': 5, 'c': 6}


def fun(list1, dict1):
    sum1 = 0
    for i in list1:
        sum1 += i
    for v in dict1.values():
        sum1 += v
    print(sum1)


fun(list1, dict1)
