import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
s.send('you are a sb'.encode())
print(s.recv(1024).decode())
