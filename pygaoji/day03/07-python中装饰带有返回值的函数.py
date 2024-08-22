def logging(fn):
    def inner():
        print("开始执行")
        return fn()

    return inner


@logging
def add():
    print("执行add")
    return 100


print(add())
