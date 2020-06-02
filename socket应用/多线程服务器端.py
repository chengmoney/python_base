from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer


class Handle(BaseRequestHandler):
    def handle(self):
        conn = self.request
        msg = 'Welcome!'.encode()
        conn.send(msg)
        file = 'new_file'
        while True:
            with open(file, 'ab') as f:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        conn.close()


if __name__ == '__main__':
    host = ''
    port = 8888
    with ThreadingTCPServer((host, port), Handle) as myserver:
        myserver.serve_forever()






