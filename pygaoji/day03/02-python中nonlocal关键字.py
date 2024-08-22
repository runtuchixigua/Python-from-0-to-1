def outer():
    num = 100

    def inner():
        nonlocal num
        num += 1
        print(num)

        def inner1():
            nonlocal num
            num += 1
            print(num)

        inner1()

    inner()
    print(num)


outer()
