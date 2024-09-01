'''
1.手动在当前项目根目录下创建singer.txt文件，内容如下： 沉默是金，张国荣 少女的祈祷，杨千嬅 暗里着迷，刘德华 难念的经，周华健
2、定义一个singer类(歌手类)，包含初始化init方法： 成员属性: 歌曲名 歌手名字 成员方法：fans()：打印“XXX歌手的YYY歌曲持续打榜，
粉丝为喜欢的歌手打call” XXX为对象的歌手名字，YYY为对象的歌曲名。

3、在歌手类外面完成以下功能： 1）通过程序逐行读取singer.txt文件内容，根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。
2）遍历列表，获取元素并调用对象的fans方法
'''


class singer(object):
    def __init__(self, name, music):
        self.name = name
        self.music = music

    def fans(self):
        print(f'{self.name}歌手的{self.music}歌曲持续打榜，粉丝为喜欢的歌手打call')




if __name__ == '__main__':
    singer_list = []
    fr = open('singer.txt', 'r', encoding='utf-8')
    for line in fr:
        line = line.strip().split('，')
        singer1 = singer(line[0], line[1])
        singer_list.append(singer1)
    for singer in singer_list:
        singer.fans()
    fr.close()
