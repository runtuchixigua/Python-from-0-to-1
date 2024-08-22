def logging(fn):
    def inner(*args, **kwargs):
        print('开始执行')
        return fn(*args, **kwargs)

    return inner


@logging
def add_num(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    for v in kwargs.values():
        sum += v
    return sum


print(add_num(1, 2, 3,  a=1, b=2, c=3))
