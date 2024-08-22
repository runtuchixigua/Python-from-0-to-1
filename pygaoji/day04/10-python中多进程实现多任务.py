import multiprocessing
import time

def music():
    for i in range(5):
        print('正在听音乐...',flush=True)
        time.sleep(1)

def dance():
    for i in range(5):
        print('正在跳舞...',flush=True)
        time.sleep(1)

if __name__ == '__main__':
    music_process = multiprocessing.Process(target=music)
    dance_process = multiprocessing.Process(target=dance)
    music_process.start()
    dance_process.start()