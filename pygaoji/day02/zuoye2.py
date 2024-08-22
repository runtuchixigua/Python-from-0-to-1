class Parent:
    x = 1


class Child(Parent):
    pass


class Child2(Parent):
    pass


Child.x = 2
Parent.x = 3


# print(Child.x)
# print(Child2.x)
# print(Parent.x)


class Student(object):
    count = 0

    def __init__(self):
        Student.count += 1


student1 = Student()
student2 = Student()
# print(Student.count)


class B(object):
    def handle(self):
        print("B")
class A(B):
    def handle(self):
        print("A")
        super().handle()

a = A()
# a.handle()


class Mybase(object):
    def __init__(self):
        print("Mybase")



