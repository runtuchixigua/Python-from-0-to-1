# 定义一个函数
def func(mynames):
    mynames.append('赵六')


# 定义一个全局变量
names = ['张三', '李四', '王五']
# 调用函数
func(names)

print(names)  # 最终答案：[张三, 李四, 王五, 赵六]