'''
 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

给对象添加属性

* 明星姓名= “周星驰”
* 明星的电影 = “功夫”

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性

定义方法playing()，打印“xxx出演了yyy，非常好看”


定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性

print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"

xxx为明星姓名，yyy是电影的名字



定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性

删除创建的对象，打印“我不喜欢xxx了”
'''


class Star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def playing(self):
        print(self.name + "出演了" + self.movie + "，非常好看")

    def __del__(self):
        print("我不喜欢" + self.name + "了")



    pass


star_list = []
for i in range(5):
    name = input("请输入明星姓名：")
    movie = input("请输入明星电影：")
    star = Star(name, movie)
    star_list.append(star)

for i in range(len(star_list)):
    star_list[i].playing()


