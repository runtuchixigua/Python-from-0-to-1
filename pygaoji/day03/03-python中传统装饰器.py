def check(fn):
    def inner():
        print("xxx")
        fn()

    return inner


# def comment():
#     print("yyy")

# @check
def comment():
    print("zzz")

c = check(comment)
c()

# comment()
