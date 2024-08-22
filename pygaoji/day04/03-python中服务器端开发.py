import socket

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.108.62', 8000))
    server.listen(128)
    conn, addr = server.accept()
    print(conn, addr)
    while True:
        data = conn.recv(1024).decode('utf-8')
        print(data)
        if data == b'exit':
            break
        conn.send('收到'.encode('utf-8'))
    server.close()