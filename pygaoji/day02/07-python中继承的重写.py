class Animal(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def drink(self):
        print("喝水")

    def eat(self):
        print("睡觉")

    def sleep(self):
        print("吃东西")

    def call(self):
        print("叫")


class Dog(Animal):
    def call(self):
        print("汪汪叫")


class Cat(Animal):
    def call(self):
        print("喵喵叫")


dog = Dog("小黑", 3)
dog.call()
