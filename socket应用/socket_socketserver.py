import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        msg = 'welcome'
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())
            conn.send(data)
            num = b'200'
            conn.send(num)
            # conn.close()


if __name__ == '__main__':
    port = ('127.0.0.1', 8887)
    sk = socketserver.ThreadingTCPServer(port, MyServer)
    sk.serve_forever()
