class Girl(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 0 or age > 120:
            raise ValueError("年龄必须在0到120之间")
        self.__age = age
        return


girl = Girl("小红", 18)
girl.set_age(100)
print(girl.get_age())
