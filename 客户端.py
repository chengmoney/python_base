import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024).decode())
while True:
    msg = input('请输入消息...').encode()
    s.send(msg)
    if msg == b'exit':
        break
s.close()
