def logging(flag):
    def decorator(fn):
        def inner(a, b):
            if flag == '+':
                print('执行加法运算')
            else:
                print('执行减法运算')
            return fn(a, b)

        return inner

    return decorator


@logging('+')
def add(a, b):
    return a + b


@logging('-')
def sub(a, b):
    return a - b


print(add(1, 2))
print(sub(1, 2))
