class StudentManager(object):
    def __init__(self):
        self.students = []

    @staticmethod
    def menu():
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生")
        print("4.查询学生")
        print("5.显示所有学生")
        print("6.退出")
        print('---------------------------------')


StudentManager.menu()
stu_manager = StudentManager()
stu_manager.menu()
