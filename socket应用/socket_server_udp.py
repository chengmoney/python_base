# 导入模块
import socket

# 进行实例化 UDP参数设置
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# IP地址和端口
port = ('127.0.0.1', 8888)
# 对port进行监听
sk.bind(port)

while True:
    print('正在接收信息.....')
    # Tcp 协议中不需要accept
    # client, address = sk.accept()
    # msg = 'welcome'
    # sk.sendto(msg.encode(), port)
    # sk.sendto(b'23', port)  这样写是错误的，这个是发给服务器
    data, port_from = sk.recvfrom(1024)
    # data = sk.recv(1024)
    if data == b'exit':
        # sk.sendto('Bye!', port_from)
        break
    print(data.decode())

sk.close()




