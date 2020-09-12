import json
import names
import random
import socket
import socketserver

import flag


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        colors = ["red", "blue", "yellow", "orange", "purple", "pink"]

        child_name, parent_name, grandparent_name = [names.get_full_name() for _ in range(3)]
        child_age, parent_age, grandparent_age = [random.randint(1, 10), random.randint(25, 40), random.randint(60, 75)]
        color = random.choice(colors)

        child = {
            "name": child_name,
            "age": child_age,
            "favorite-color": color
        }

        parent = {
            "name": parent_name,
            "age": parent_age,
            "child": child
        }

        grandparent = {
            "name": grandparent_name,
            "age": grandparent_age,
            "child": parent
        }

        data = json.dumps(grandparent)

        client.sendall(data.encode())
        answer = json.loads(client.recv(1024).decode())
        child["grandparent"] = grandparent["name"]

        if answer == child:
            client.sendall(flag.flag.encode())
        else:
            client.sendall(b"Wrong answer!")
        
        client.shutdown(socket.SHUT_RDWR)
        client.close()

    def setup(self):
        # on veut pas que le TaskHandler attende recv pour toujours
        self.request.settimeout(30.0)

    def handle(self):
        self.main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()
