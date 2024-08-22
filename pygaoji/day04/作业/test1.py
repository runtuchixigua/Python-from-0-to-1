import socket

if __name__ == '__main__':
    # 1 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2 连接服务器
    tcp_socket.connect(('47.93.187.37', 8081))
    # 3.1 发送数据
    tcp_socket.send('hello'.encode())
    # 3.2 接收数据
    recv_data = tcp_socket.recv(4096)
    if recv_data:
        print("接收到对方回复 %s" % recv_data.decode())
    else:
        print("对方连接关闭了")
    # 4 关闭连接
    tcp_socket.close()