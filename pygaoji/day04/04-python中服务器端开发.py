import socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('', 8000))
socket_server.listen(128)
conn_socket, addr = socket_server.accept()
recv_data = conn_socket.recv(1024).decode('utf-8')
print(f'{addr}发的：{recv_data}')
content = input('请输入要发送的内容：')
conn_socket.send(content.encode('utf-8'))
conn_socket.close()
socket_server.close()
