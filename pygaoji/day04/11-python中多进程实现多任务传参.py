import multiprocessing
import time
def music(name):
    for i in range(5):
        print("正在听%s音乐"%name)
        time.sleep(1)
def dance(name, timer):
    for i in range(5):
        print(f"{name}正在跳舞")
        time.sleep(timer)


if __name__ == '__main__':
    music_process = multiprocessing.Process(target=music, args=("周杰伦",))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name":"王力宏", "timer":2})
    music_process.start()
    dance_process.start()