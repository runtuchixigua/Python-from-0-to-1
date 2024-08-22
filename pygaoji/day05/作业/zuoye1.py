from multiprocessing import Process
import time


def task(n):
    for i in range(n):
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    p = Process(target=task, args=(4,))
    p.start()