import multiprocessing
import os
my_list = [1]
def writh_to_list():
    global my_list
    for i in range(3):
        my_list.append(i)
    print(my_list)

def read_from_list():
    global my_list
    print(my_list)


if __name__ == '__main__':
    write_process = multiprocessing.Process(target=writh_to_list)
    read_process = multiprocessing.Process(target=read_from_list)
    write_process.start()
    read_process.start()