import socket
import threading


def handle(conn, addr):
    while True:
        data = conn.recv(1024).decode('utf-8')
        print(f'{addr}说了：{data}')
        content = input('请输入内容:')
        conn.send(content.encode('utf-8'))
        if data == 'exit':
            conn.close()
            break


if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(('', 8080))
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.listen(128)
    while True:
        conn, addr = socket_server.accept()
        sub_thread = threading.Thread(target=handle, args=(conn, addr))
        sub_thread.start()
