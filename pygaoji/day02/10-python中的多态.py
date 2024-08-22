class Fruit(object):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def make_juice(self):
        print('make果汁')

class Apple(Fruit):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    def make_juice(self):
        print('make苹果汁')

class Banana(Fruit):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    def make_juice(self):
        print('make香蕉汁')

class Orange(Fruit):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    def make_juice(self):
        print('make橙子汁')

def service(obj):
    obj.make_juice()

service(Apple('apple', 10))
service(Banana('banana', 20))
service(Orange('orange', 30))