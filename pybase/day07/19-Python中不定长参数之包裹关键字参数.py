'''
基本语法：
def func(**kwargs):  # kwargs是变量名，返回的数据类型为字典类型
    pass

func(关键字参数）  # 参数=参数值
'''
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# 使用关键字参数来传递参数值
func()
func(name='Tom')
func(name='Tom', age=23)
func(name='Tom', age=23, mobile='10086')

'''
小结：不定长参数
*args：包裹位置参数
**kwargs：包裹关键字参数
相同点：都可以用于接收不定长参数
不同点：返回类型不同，args（元组类型）、kwargs（字典类型）；传递方式不同 => args只能接收位置参数，kwargs只能接收关键字参数！
'''
