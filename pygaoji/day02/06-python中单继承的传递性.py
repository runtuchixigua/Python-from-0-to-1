class A(object):
    def func1(self):
        print("A.func1")

class B(A):
    def func2(self):
        print("B.func2")

class C(B):
    def func3(self):
        print("C.func3")


c = C()
c.func1()
c.func2()
c.func3()