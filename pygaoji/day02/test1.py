class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    @staticmethod
    def sleep():
        print("sleep")


class Girl(Person):
    pass


# person = Person("小明", 18)
girl = Girl("小红", 16)
print(girl.get_age())
girl.sleep()
