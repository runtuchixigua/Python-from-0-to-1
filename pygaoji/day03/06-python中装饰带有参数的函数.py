def logging(fn):
    def inner(a, b):
        print("开始执行函数")
        fn(a, b)
        print("函数执行结束")

    return inner


@logging
def add(a, b):
    print(a + b)


add(1, 2)
