import socket
from utils import get_response
from langchain.memory import ConversationBufferMemory

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('192.168.108.62', 8080))
socket_server.listen(128)
while True:
    try:
        conn, addr = socket_server.accept()
        while True:
            try:
                recv_data = conn.recv(2048).decode('utf-8')
                print(f'客户端说了：{recv_data}')
                memory = ConversationBufferMemory(return_messages=True)
                api_key = 'sk-188e803b54354551bdae6b708daa20da'
                response = get_response(recv_data, api_key, memory)
                conn.send(response.encode('utf-8'))
                print(f'服务器端说：{response}')
            except ConnectionResetError:
                print('客户端异常')
                break
    except:
        print('服务器异常')
        break

socket_server.close()
