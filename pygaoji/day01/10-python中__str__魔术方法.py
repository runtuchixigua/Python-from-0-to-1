class Car(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f'你滴车真帅，品牌是{self.brand}, 颜色是{self.color}'

    def __del__(self):
        print('车被销毁了')

benz = Car('Benz', 'black')
print(benz)
# del benz
