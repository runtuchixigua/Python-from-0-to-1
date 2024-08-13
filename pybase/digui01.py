def func(n):
    if n == 1:
        return 1
    return func(n - 1) + n


# print(func(100))

fuc2 = lambda n: fuc2(n - 1) + n if n > 1 else 1


# print(fuc(100))


def fuc1(n):
    if n == 1:
        return 1
    return fuc1(n - 1) * n


# print(fuc2(3))

fuc3 = lambda n: fuc3(n - 1) * n if n > 1 else 1


# print(fuc3(4))


def fuc4(n):
    if n == 1 or n == 2:
        return 1
    return fuc4(n - 1) + fuc4(n - 2)


# print(fuc4(10))

result = 1


def peach(n):
    global result
    result = (result + 1) * 2
    if n == 2:
        return result
    return peach(n - 1)


# print(peach(10))


def eat_peach(n):
    if n == 1:
        return 1
    else:
        return (eat_peach(n - 1) + 1) * 2


# print(eat_peach(10))

eatpeach = lambda n: (eatpeach(n - 1) + 1) * 2 if n != 1 else 1
print(eatpeach(10))


str = 'asa'
print(str*3)