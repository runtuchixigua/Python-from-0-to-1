# 1. 导入模块
import socket

# 2. 创建套接字，使用UDP协议
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3. 定义目标服务器
server = ('192.168.108.42', 2425)
# 4. 使用sendto()方法发送数据，第一个参数内容，第二个参数目标机器
content = '1:134871264:蔡徐坤:itheima:32:你好，陌生人！'
udp_client_socket.sendto(content.encode('gbk'), server)