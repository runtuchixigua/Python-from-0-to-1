import socket
from utilsp import get_response
from langchain.memory import ConversationBufferMemory

api_key = 'sk-188e803b54354551bdae6b708daa20da'

# 初始化socket连接
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 尝试连接服务器
    socket_client.connect(('192.168.108.62', 8080))
    socket_client.send('你好,我是彭湘达，你是谁？'.encode('utf-8'))

    memory = ConversationBufferMemory(return_messages=True)

    while True:
        try:
            # 接收数据
            recv_data = socket_client.recv(2048).decode('utf-8')
            # 处理数据
            response = get_response(recv_data, api_key, memory)
            # 发送响应
            socket_client.send(response.encode('utf-8'))
            print(response)
        except Exception as e:
            print(f"Error occurred: {e}")
            break

except Exception as e:
    print(f"Failed to connect or send data: {e}")

finally:
    # 关闭socket连接
    socket_client.close()
