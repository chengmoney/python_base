import socket

sk = socket.socket()
# 在两台电脑上运行的时候host用空字符串的意思是，监听连接到服务器的所有ip
host = '127.0.0.1'
port = 8888
sk.bind((host, port))
sk.listen(5)
file = 'fasong2'
while True:
    client, adr = sk.accept()
    msg = 'welcome to {}'.format(host).encode()
    client.send(msg)
    while True:  # 保持连接，直到传输完成后再断开连接
        with open(file, 'ab') as f:
            data = client.recv(1024)
            if data:
                f.write(data)
            else:
                break
    print('文件接收完成')
