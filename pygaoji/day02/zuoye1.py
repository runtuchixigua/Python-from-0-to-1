class Parent:
    def __init__(self):
        print("父类初始化")


class Child(Parent):

    def child_method(self):
        print("子类方法")


child = Child()
child.child_method()


class A(object):
    def __init__(self):
        print("A类初始化")

    def a_method(self):
        print("A类方法")


class B(object):
    def __init__(self):
        print("B类初始化")
    def b_method(self):
        print("B类方法")


class C(A, B):
    def c_method(self):
        print("C类方法")


c = C()
c.c_method()
