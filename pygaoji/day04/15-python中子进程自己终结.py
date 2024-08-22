import multiprocessing
import time
def task():
    print("子进程开始执行任务")
    for i in range(10):
        print(f"子进程正在执行任务{i}")
        time.sleep(0.2)
    print("子进程执行任务结束")

if __name__ == '__main__':
    print("主进程开始执行任务")
    task_process = multiprocessing.Process(target=task)

    task_process.start()

    time.sleep(2)
    task_process.terminate()
    print("主进程执行任务结束")
