import threading
import time

def dance(name):
    for i in range(5):
        print(f'{name} is dancing')
        time.sleep(0.2)

def music(name,timer):
    for i in range(5):
        print(f'{name} is playing music')
        time.sleep(timer)
        time.sleep(timer)


if __name__ == '__main__':
    dance_thread = threading.Thread(target=dance,args=('tom',))
    music_thread = threading.Thread(target=music,kwargs={'name':'jack','timer':0.2})
    dance_thread.start()
    music_thread.start()