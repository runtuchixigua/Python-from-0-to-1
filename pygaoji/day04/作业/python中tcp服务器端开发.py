import socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('192.168.108.62', 8080))
socket_server.listen(128)
while True:
    try:
        conn, addr = socket_server.accept()
        try:
            recv_data = conn.recv(1024).decode('utf-8')
            print(f'{addr}说了：{recv_data}')
            content = input('请输入要发送的内容：')
            conn.send(content.encode('utf-8'))
        except ConnectionResetError:
            print('客户端异常')
            break

    except:
        print('服务器异常')
        break

socket_server.close()

