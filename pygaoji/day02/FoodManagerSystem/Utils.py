import time

def use_time(fn):
    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print("函数执行时间：%s" % (end_time - start_time))
    return inner


