#!/usr/bin/env python3
# hash-breaker challenge
import socket
import socketserver
import time
import random
import base64
import io
from PIL import Image, ImageDraw, ImageFont

flag = "flag-63bbf01698840ce256abc6954e51c420eb281352"

sequence = []
for i in range(48, 123):
	if i >= 48 and i <= 57 or i >= 65 and i <= 90 or i >= 97 and i <= 122:
		sequence.append(chr(i))

# ceux qui portes à confusion sont enlevés (dépend trop de la qualité d'OCR de chaque joueur)
sequence.remove('l')
sequence.remove('1')
sequence.remove('i')
sequence.remove('I')
sequence.remove('o')
sequence.remove('O')
sequence.remove('0')
sequence.remove('U')

class TaskHandler(socketserver.BaseRequestHandler):
	def main(self, client):
		tries = 10
		for i in range(1, tries + 1):
			# generate random string
			rndstring = ""
			for n in range(random.randint(9, 11)):
				rndstring += random.choice(sequence)

			# create image
			img = Image.open("random.png")
			fnt = ImageFont.truetype('Roboto-Regular.ttf', 54)
			x = random.randint(70, 200)
			y = random.randint(40, 160)
			d = ImageDraw.Draw(img)
			d.text((x, y), rndstring, font = fnt, fill = (255, 69, 0))

			# save file (as PNG) to memory buffer
			in_mem_file = io.BytesIO()
			img.save(in_mem_file, format = "PNG")
			in_mem_file.seek(0)
			img_bytes = in_mem_file.read()

			# convert to Base64
			newimg = base64.b64encode(img_bytes)

			print(str(newimg[:32]) + " ... " + str(newimg[-32:]))

			# start timer and send challenge
			start_time = time.time()
			# send size, then base64-encoded image
			client.sendall(str(len(newimg)).encode('ascii') + b"\n")
			client.sendall(newimg + b"\n")
			# receive answer
			answer = client.recv(1024).decode().strip()
			end_time = time.time()

			print("iterations " + str(i) + " sur " + str(tries))

			if end_time - start_time >= 3.0:
				troplent = "Trop lent!"
				client.sendall(str(len(troplent)).encode() + b"\n")
				client.sendall(troplent.encode('utf-8') + b"\n")
				break
			elif answer == rndstring:
				if i == tries:
					client.sendall(str(len(flag)).encode() + b"\n")
					client.sendall(flag.encode() + b"\n")
					break
			else:
				mauvaise = "Mauvaise réponse"
				client.sendall(str(len(mauvaise)).encode() + b"\n")
				client.sendall(mauvaise.encode('utf-8') + b"\n")
				break

		print("Finished")

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
