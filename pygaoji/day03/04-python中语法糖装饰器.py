from test1 import use_time


@use_time
def func1():
    for i in range(10000000):
        pass


func1()
