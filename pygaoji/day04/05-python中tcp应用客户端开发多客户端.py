import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.bind(('', 8000))
socket_client.listen(5)
while True:
    conn_client, addr = socket_client.accept()
    recv_data = conn_client.recv(1024).decode('utf-8')
    print(recv_data)
    content = input('请输入要发送的内容：')
    conn_client.send(content.encode('utf-8'))
    conn_client.close()
