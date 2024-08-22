import threading
import time

def get_info():
    time.sleep(0.5)
    current_thread = threading.current_thread()
    print(current_thread.name)

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=get_info)
        t.start()
