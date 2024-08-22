
def logging(jiajian):
    def decorator(fn):
        def inner(a,b):
            if jiajian == '+':
                print('加法')
                return fn(a,b)
            elif jiajian == '-':
                print('减法')
                return fn(a,b)
        return inner
    return decorator
@logging('+')
def add(a,b):
    return a+b
@logging('-')
def jian(a,b):
    return a-b

if __name__ == '__main__':
    print(add(1,2))
    print(jian(1,2))

