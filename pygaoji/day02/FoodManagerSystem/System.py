class System(object):
    def __init__(self):
        self.food_list = []

    def menu(self):
        while True:
            print('1.添加食物')
            print('2.删除食物')
            print('3.修改食物')
            print('4.查找食物')
            print('5.显示所有食物')
            print('6.保存食物')
            print('7.退出')
            print('--------------------------')

    def add_food(self):
        name = input('请输入食物名称：')
        price = input('请输入食物价格：')
        food = {'name': name, 'price': price}
        self.food_list.append(food)

    def del_food(self):
        name = input('请输入食物名称：')
        for i in range(len(self.food_list)):
            if self.food_list[i]['name'] == name:
                del self.food_list[i]
                break
            else:
                print('没有找到该食物')

    def modify_food(self):
        name = input('请输入食物名称：')
        for i in range(len(self.food_list)):
            if self.food_list[i]['name'] == name:
                self.food_list[i]['name'] = input('请输入新的食物名称：')
                self.food_list[i]['price'] = input('请输入新的食物价格：')
                break
            else:
                print('没有找到该食物')

