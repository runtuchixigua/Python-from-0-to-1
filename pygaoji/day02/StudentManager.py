class Student_Manager(object):
    def __init__(self):
        self.students = []

    @staticmethod
    def show_menu():
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生")
        print("4.查询学生")
        print("5.显示所有学生")
        print("6.退出系统")
        print('-----------------------------')
        choice = input("请输入您的选择：")
        return choice

    def add_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        sex = input("请输入学生性别：")
        student = {"name": name, "age": age, "sex": sex}
        self.students.append(student)
        print(self.students)
        print("添加学生成功")

    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for i in range(len(self.students)):
            if self.students[i]["name"] == name:
                del self.students[i]
                print("删除学生成功")
                return
        print("删除学生失败")

    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for i in range(len(self.students)):
            if self.students[i]["name"] == name:
                self.students[i]["age"] = int(input("请输入学生年龄："))
                self.students[i]["sex"] = input("请输入学生性别：")
                print("修改学生成功")
                return
        print("修改学生失败")

    def search_student(self):
        name = input("请输入要查询的学生姓名：")
        for i in range(len(self.students)):
            if self.students[i]["name"] == name:
                print("查询学生成功")
                print(self.students[i])
                return
        print("查询学生失败")

    def show_all_student(self):
        print("所有学生信息如下：")
        for i in range(len(self.students)):
            print(self.students[i])

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                self.show_all_student()
            elif choice == "6":
                break
            else:
                print("输入错误，请重新输入")


