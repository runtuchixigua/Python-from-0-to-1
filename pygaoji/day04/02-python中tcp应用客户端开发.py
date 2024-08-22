import socket
if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.106.1", 8080))
    tcp_client_socket.send('hello'.encode('utf-8'))
    recv_data = tcp_client_socket.recv(1024).decode('utf-8')
    print(recv_data)
    tcp_client_socket.close()