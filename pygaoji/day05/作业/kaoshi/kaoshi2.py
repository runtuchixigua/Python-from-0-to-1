'''
题目：使用套接字编程完成TCP客户端开发，连接服务器地址：192.168.108.88，端口号为8000，
客户端主动向服务器端发送文本"hello，itheima"，并接受服务器端返回结果。
'''
# import socket
# socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_client.connect(('192.168.108.88', 8000))
# socket_client.send(bytes('hello，itheima', 'utf-8'))
# result = socket_client.recv(1024).decode('utf-8')
# print(result)
# socket_client.close()


a = 1
b = 2
c = 3
c= a if a > b else b
print(c)