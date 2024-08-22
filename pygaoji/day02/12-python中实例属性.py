class Phone(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color



mi = Phone("小米", "黑色")
print(mi.brand)
print(mi.color)
huawei = Phone("华为", "蓝色")
print(huawei.brand)
print(huawei.color)

