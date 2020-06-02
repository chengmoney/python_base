import socket
import time
file = 'socket_client_udp.py'

sk = socket.socket()
host = '127.0.0.1'
port = 8888
sk.connect((host, port))
msg = sk.recv(1024).decode()
print(msg)

# 记住打开文件要以二进制模式打开
with open(file, 'rb') as f:
    for line in f:
        sk.send(line)
        time.sleep(2)

