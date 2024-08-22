def yonghuming(fn):
    def inner():
        print("yonghuming1")
        fn()
        print("yonghuming2")
    return inner

def mima(fn):
    def inner():
        print("mima1")
        fn()
        print("mima2")
    return inner

@yonghuming
@mima
def login():
    print("yes")

login()
