from Student import Student
stu1 = Student('张三', 18, '12345678901')
# print(stu1.__dict__)

stu2 = Student('李四', 19, '12345678902')

def func1(**kwargs):
    print(kwargs)
#
#
# func1({'name':'张三', 'age':18, 'mobile':'12345678901'})
#
# func1(name='张三', age=18, mobile='12345678901')

try:
    f = open("students.txt", "r", encoding='utf8')
except:
    f = open("students.txt", "w", encoding='utf8')
    f.write('[]')
else:
    students1 = eval(f.read())
    students = [Student(**stu) for stu in students1]
    print(students)
    for stu in students1:
        print(stu)
        print(type(stu))
        func1(**stu)