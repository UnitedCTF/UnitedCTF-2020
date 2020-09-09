import json
import names
import socket
import socketserver
import time

import flag


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        name = names.get_full_name()
        start_time = time.time()

        client.sendall(name.encode() + b"\n")
        answer = client.recv(1024).decode().strip()
        end_time = time.time()

        if end_time - start_time >= 1.0:
            client.sendall(b"Too slow! You have 1 second to send back the text that was sent to you.")
        elif answer == name:
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