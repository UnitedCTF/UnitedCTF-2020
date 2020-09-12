#!/usr/bin/env python3
# hash-breaker challenge

import socket
import socketserver
import time
import hashlib
import random

flag = "flag-f832827eadad134a5450779048b3097050cac430"

class TaskHandler(socketserver.BaseRequestHandler):
	def main(self, client):
		tries = 10
		for i in range(1, tries + 1):
			value = str(random.randint(1, 65535))
			value_hash = hashlib.sha1(value.encode('ascii')).hexdigest()
			start_time = time.time()

			client.sendall(value_hash.encode() + b"\n")
			answer = client.recv(1024).decode().strip()
			end_time = time.time()

			if end_time - start_time >= 2.0:
				client.sendall("Trop lent!".encode('utf-8'))
				break
			elif answer == value:
				if i == tries:
					client.sendall(flag.encode())
					break
			else:
				client.sendall("Mauvaise réponse".encode('utf-8'))
				break
		
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
