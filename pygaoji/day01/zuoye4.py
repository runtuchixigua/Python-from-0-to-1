'''
4、定义一个汽车类，并在类中定义一个move方法，
然后分别创建BMW_X9、AUDI_A9对象，并添加颜色、马力、型号等属性，然后分别打印出属性值、调用move方法（使用__init__方法完成属性赋值）。
'''
class Car(object):
    def __init__(self, name, color, horsepower, model):
        self.name = name
        self.color = color
        self.horsepower = horsepower
        self.model = model
    def move(self):
        print('%s正在行驶' % self.name)

    def __str__(self):
        return 'name:%s, color:%s, horsepower:%s, model:%s' % (self.name, self.color, self.horsepower, self.model)

BMW_X9 = Car('BMW_X9', 'white', 300, 'X9')
BMW_X9.a = 1
AUDI_A9 = Car('AUDI_A9', 'black', 400, 'A9')

print(BMW_X9.a)
BMW_X9.move()
AUDI_A9.move()
print(BMW_X9)
print(AUDI_A9)