import multiprocessing
import os
def work():
    print("子进程的pid是%d"%os.getpid())
    print("父进程的pid是%d"%os.getppid())

if __name__ == '__main__':
    print(os.getpid())
    p = multiprocessing.Process(target=work)
    p.start()