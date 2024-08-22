import socket

if __name__ == '__main__':
    tcp_client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(tcp_client_server)