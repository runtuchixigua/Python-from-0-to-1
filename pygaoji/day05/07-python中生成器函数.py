def my_generator(n):
    for i in range(n):
        print("正在执行第%d次start" % i)
        yield i
        print("正在执行第%d次end" % i)

gen = my_generator(3)
print(next(gen))
print(next(gen))


