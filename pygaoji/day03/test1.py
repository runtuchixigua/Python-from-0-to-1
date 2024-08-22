def fu1():
    number = 10

    def fu2():
        number = 100

        def fu3():
            nonlocal number
            number = 30

        fu3()
        print(number)
    fu2()
    print(number)

# fu1()

import time
def use_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print(end-start)
    return inner





