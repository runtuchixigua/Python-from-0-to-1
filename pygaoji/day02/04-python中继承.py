class Animal(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def drink(self):
        print("喝")


class Dog(Animal):
    def goujiao(self):
        print("狗叫")

    pass


dog = Dog("旺财", 3)
dog.eat()
dog.goujiao()
