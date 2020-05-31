import socket

s = socket.socket()
host = '127.0.0.1'
port = 8887
s.connect((host, port))
print(s.recv(1024).decode())
while True:
    msg = input('请输入你要输入的消息： ').encode()
    s.send(msg)
    print(s.recv(1024).decode())
    print(s.recv(1024).decode())

