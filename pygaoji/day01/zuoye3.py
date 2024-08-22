'''
1、定义一个电脑类,电脑有品牌,有价格,能放电影。分别创建2个对象"联想电脑" 和 "苹果电脑"。调用放电影的动作,联想电脑播放 电影"葫芦娃"，苹果电脑播放"黑猫警长"。
'''
class computer(object):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def play(self, movie):
        print(f'{self.brand}电脑正在播放{movie}')

lx = computer("联想", 5000)
lx.play("葫芦娃")
ip = computer("苹果", 10000)
ip.play("黑猫警长")


'''
2、定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加属性:颜色和价格:
'''
class Fruit(object):
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.color} {self.price}'

apple = Fruit("红色", 5)
orange = Fruit("橙色", 10)
watermelon = Fruit("绿色", 20)
print(apple, orange, watermelon)