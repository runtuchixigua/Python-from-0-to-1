from time import sleep,time
# print(time())
# sleep(10)
# print(type(time()))
import mymodule2
# from mymodule2 import my_sleep


start = time()
list1 = []

mymodule2.my_sleep()

for i in range(1000000):
    list1.append(i)
mymodule2.look_watch()
end = time()

print(end-start)