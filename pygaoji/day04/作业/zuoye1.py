'''
实现一个 TCP客户端， 连接的服务器是 `47.93.187.37` 端口是`8081`,
请向他发送一个helloworld 然后将接收到的数据打印出来。

##### 考察知识点：
'''
import socket
if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(('192.168.108.62', 8082))
    socket_client.send('helloworld'.encode('utf-8'))
    recv_data = socket_client.recv(1024).decode('utf-8')
    print(recv_data)
    socket_client.close()