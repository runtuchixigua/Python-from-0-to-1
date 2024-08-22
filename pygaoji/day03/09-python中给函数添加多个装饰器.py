def check_user(fn):
    def inner():
        print("检查用户")
        fn()

    return inner


def check_pwd(fn):
    def inner():
        print("检查密码")
        fn()

    return inner


@check_user
@check_pwd
def login():
    print("登录成功")


login()
