class Person(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.count += 1


print(Person.count)
p = Person('张三', 18)
print(p.count)
