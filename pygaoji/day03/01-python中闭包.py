def outer():
    """
    外部函数，用于封装一个内部函数，并返回该内部函数。

    返回:
        inner: 内部函数，被封装在外部函数中。
    """
    num = 100
    print(id(num))

    def inner():
        """
        内部函数，用于访问外部函数中的变量并打印其值。
        """
        print(num)
        print(id(num))

    return inner


# 创建一个函数对象，该对象关联到外部函数返回的内部函数。
func = outer()
# 调用内部函数，以展示其访问外部函数变量的能力。
func()
print(type(func))


x=100
print(id(x))
