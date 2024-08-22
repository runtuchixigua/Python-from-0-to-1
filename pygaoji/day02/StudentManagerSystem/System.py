from Student import Student


class System(object):
    def __init__(self):
        self.students = []



    @staticmethod
    def menu():
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生")
        print("4.查询学生")
        print("5.显示所有学生")
        print("6.保存学生信息到文件")
        print("7.退出系统")
        print("----------------------------")

    def add_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        mobile = input("请输入学生手机号：")
        student = Student(name, age, mobile)
        self.students.append(student)
        print("添加学生成功")

    def del_student(self):
        name = input("请输入学生姓名：")
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                print("删除学生成功")
                break
            else:
                print("没有该学生")

    def modify_student(self):
        name = input("请输入学生姓名：")
        for i in self.students:
            if i.name == name:
                i.name = input("请输入学生姓名：")
                i.age = int(input("请输入学生年龄："))
                i.mobile = input("请输入学生手机号：")
                print("修改学生成功")
                break
            else:
                print("没有该学生")

    def find_student(self):
        name = input("请输入学生姓名：")
        for i in self.students:
            if i.name == name:
                print(i)
                break
            else:
                print("没有该学生")

    def show_all_student(self):
        for student in self.students:
            print(student)

    def save_student(self):
        # with open("students.txt", "w", encoding='utf8') as f:
        #     for student in self.students:
        #         str1 = student.name + "," + str(student.age) + "," + student.mobile
        #         f.write(str1)
        #         f.write("\n")
        f = open("students.txt", "w", encoding='utf8')
        student_list = [stu.__dict__ for stu in self.students]
        f.write(str(student_list))
        f.close()
        print("保存学生信息到文件成功")


    def load_student(self):
        try:
            f = open("students.txt", "r", encoding='utf8')
        except:
            f = open("students.txt", "w", encoding='utf8')
            f.write('[]')
        else:
            students = eval(f.read())
            self.students = [Student(**stu) for stu in students]
            print("加载学生信息成功")
        finally:
            f.close()


    def run(self):
        self.load_student()
        while True:
            self.menu()
            choice = input("请输入您的选择：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.del_student()
            elif choice == "3":
                self.modify_student()
            elif choice == "4":
                self.find_student()
            elif choice == "5":
                self.show_all_student()
            elif choice == "6":
                self.save_student()
            elif choice == "7":
                break
            else:
                print("输入错误，请重新输入")
