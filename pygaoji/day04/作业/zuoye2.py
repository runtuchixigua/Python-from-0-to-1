'''
编写TCP服务器接收客户端的消息, 并把客户端发送的信息原样返回给客户端。
'''
import socket
if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('192.168.108.62', 8082))
    socket_server.listen(128)
    conn_socket, addr = socket_server.accept()
    recv_data = conn_socket.recv(1024).decode('utf-8')
    print(recv_data)
    conn_socket.send(recv_data.encode('utf-8'))
    conn_socket.close()
    socket_server.close()