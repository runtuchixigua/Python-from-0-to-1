
class pp:
    name = "a"
    age = 22

ppp = pp;
print(pp.name)
'''
asdjflkajlkdf
'''
name1 = 'A'
name2 = "A"
name3 = """A"""
print(name2, name3, name1)
day = 6
p6 = "666"
msg1 = "第%s天大蟒蛇的学习笔记 %s" % (day, p6)
msg2 = "第%s天大蟒蛇的学习笔记" % day
print(msg1,type(day),type(p6))
print(msg2)
name = "j"
born_year = 2002
born_time = 17.30
print(f"我是{name} 我出生于{born_year} 我出生时间是{born_time}")
# a = input("你认真的？")
# print(a)
age = 18
if age > 18:
#缩进受if控制
    print("你已经是个老灯了")
    print("老年人")
elif age == 18:
    print("成年灯")
else:
    print("新灯")
i = 1
while i < 10:
    print("起飞", i)
    print(f"qifie{i}")
    i += 1

name = "abc"
for x in name:
    print(x)

def say_yes():
    print("yes")

say_yes()

stu_list1 = ['wang', 1, 'ji']
stu1 = stu_list1[1]
print(stu1)
stu_list2 = [['wu', 'hong'],['wang', 'li', 'ji']]
stu2 = stu_list2[1][0]
print(stu2)

t1 = (1, "hello", True)
t2 = (1)
print(t1)


