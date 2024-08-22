import time
def use_time(fn):
    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print("函数执行时间：", end_time - start_time)
    return inner
@use_time
def fu1():
    time.sleep(2)
    print("fu1函数执行了")

fu1()