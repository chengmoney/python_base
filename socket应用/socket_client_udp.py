import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP地址和端口
port = ('127.0.0.1', 8888)

while True:
    msg = input('请输入要发送的消息： ')
    sk.sendto(msg.encode(), port)
    if msg == 'exit':
        break
sk.close()


