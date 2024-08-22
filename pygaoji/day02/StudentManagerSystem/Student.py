class Student(object):
    def __init__(self, name: str, age: int, mobile: str):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，手机号：{self.mobile}'


