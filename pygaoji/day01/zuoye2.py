'''
搬家具规则：

1. 家具分不同的类型，并占用不同的面积
2. 输出家具信息时，显示家具的类型和家具占用的面积
3. 房子有自己的地址和占用的面积
4. 房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
5. 输出房子信息时，可以显示房子的地址、占地面积、剩余面积

运行结果：
当前房间可用面积为:100
床的面积为:20
ok:已经存放到房间中
当前房间可用面积为:80 容纳的物品有: 床
床的面积为:30
ok:已经存放到房间中
当前房间可用面积为:50 容纳的物品有: 床, 席梦思
'''


class House(object):
    def __init__(self, furniture, area):
        self.__furniture = furniture
        self.__area = area

    def add_furniture(self, furniture, area):
        if self.__area > area:
            self.__furniture.append(furniture)
            self.__area -= area
            print('ok:已经存放到房间中')
        else:
            print('添加失败')

    def __str__(self):
        return '当前房间可用面积为:{0} 容纳的物品有: {1}'.format(self.__area, self.__furniture)


house = House([], 100)
house.add_furniture('床', 20)
print(house)
