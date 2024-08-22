class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f'俺的名字是{self.name},体重是{self.weight}kg'

    def eat(self):
        self.weight += 2

    def run(self):
        self.weight -= 0.5

    def __del__(self):
        print(f'{self.name}死了')

    def __eq__(self, other):
        return self.weight == other.weight

    def __gt__(self, other):
        return self.weight > other.weight

xiaoming = Person('小明', 100)
print(xiaoming)


xiaoming.eat()
print(xiaoming)

xiaoming.run()
print(xiaoming)

xiaohuang = Person('小黄', 80)

if xiaoming > xiaohuang:
    print('小明比小黄胖')
else:
    print('小黄比小明胖')