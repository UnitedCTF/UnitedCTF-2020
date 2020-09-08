import json
import names
import socket
import socketserver
import time

import flag


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        name = names.get_full_name()
        client.sendall(name.encode() + b"\n")
        answer = client.recv(1024).decode().strip()

        if answer == name:
            client.sendall(flag.flag.encode())
        else:
            client.sendall(b"Wrong answer! You must send back the text that was sent to you.")
        
        client.shutdown(socket.SHUT_RDWR)
        client.close()

    def handle(self):
        self.main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()