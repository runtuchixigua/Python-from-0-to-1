import threading
import time
import Utils

a = 0

lock = threading.Lock()


@Utils.use_time
def jiayi():
    global a
    lock.acquire()
    for i in range(10000):
        a += 1
        print(f'a子线程正在运行{a}')
    print(f'a子线程运行结束--------------------------------------{a}')
    lock.release()

@Utils.use_time
def jiayi2():
    global a
    lock.acquire()
    for i in range(10000):
        a += 1
        print(f'b子线程正在运行{a}')
    print(f'b子线程运行结束-------------------------------------{a}')
    lock.release()

if __name__ == '__main__':
    thread1 = threading.Thread(target=jiayi)
    thread2 = threading.Thread(target=jiayi2)
    thread1.start()
    thread2.start()
