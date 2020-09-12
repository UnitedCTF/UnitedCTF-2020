#!/usr/bin/env python3
# solve-math challenge

import socket
import socketserver
import time
import random

flag = "flag-d91029876dd8d07f557d5ceac336cb048fde702e"

class TaskHandler(socketserver.BaseRequestHandler):
	def main(self, client):
		tries = 10
		for i in range(1, tries + 1):
			number1 = str(random.randint(1, 10000))
			number2 = str(random.randint(1, 10000))
			number3 = str(random.randint(1, 10000))
			operator1 = ('+', '-', '*')[random.randint(0, 2)]
			operator2 = ('+', '-', '*')[random.randint(0, 2)]
			problem = ' '.join((number1, operator1, number2, operator2, number3))
			value = str(eval(problem))
			start_time = time.time()

			client.sendall(problem.encode() + b"\n")
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
				client.sendall("Mauvaise réponse!".encode('utf-8'))
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
