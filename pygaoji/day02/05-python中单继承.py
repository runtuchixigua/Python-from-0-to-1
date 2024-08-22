class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃饭")

    def sleep(self):
        print("睡觉")

    def speak(self):
        print("说话")

class Student(Person):
    pass

stu = Student("张三", 18)
stu.eat()
