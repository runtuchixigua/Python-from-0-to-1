class Person(object):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


xiaomei = Person('小美', 50)
print(xiaomei.name)
xiaomei.set_weight(60)
print(xiaomei.get_weight())
xiaomei.name = 100
print(xiaomei.name)
