import threading
import time


def get_info():
    print('子线程开启')
    for i in range(10):
        print(f'子线程正在运行{i}')
        time.sleep(0.2)
    print('子线程结束')


if __name__ == '__main__':
    thread = threading.Thread(target=get_info, daemon=True)
    thread.start()
    time.sleep(1)
    print('主线程结束')
