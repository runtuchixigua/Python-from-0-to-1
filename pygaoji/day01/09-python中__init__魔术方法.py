class Car(object):
    def __init__(self, color: str, wheels: int):
        self.color = color
        self.wheels = wheels

    def show(self):
        print(f'color: {self.color}, wheels: {self.wheels}')


benz = Car('red', 4)
benz.show()
