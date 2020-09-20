#!/usr/bin/env python3
import io
import base64
import requests
import json
from PIL import Image

from pwn import *

def decode_img(msg):
	msg = base64.b64decode(msg)
	buf = io.BytesIO(msg)
	img = Image.open(buf)
	return img

def recvall(sock):
	data = bytearray()
	length = 0
	while True:
		packet = sock.recv()
		# check for the length header
		if length == 0 and len(a := packet.split(b'\n')) == 2:
			# expected size of PNG is in this packet
			length = int(a[0])
			print("[+] found length header: " + str(length))
			data.extend(a[1])
		else:
			data.extend(packet)

		if len(data) >= length:
			print("[+] pieces all received")
			break
	return data

r = remote("127.0.0.1", 3000)

mybase64 = recvall(r).decode()

while True:
	img = decode_img(mybase64)
	pixels = img.load()

	for i in range(img.size[0]):             # for every col:
		for j in range(img.size[1]):         # For every row
			if pixels[i,j] != (255, 69, 0):  # if not orange
				pixels[i,j] = (0, 0, 0)      # set black

	# save file (as PNG) to memory buffer
	in_mem_file = io.BytesIO()
	img.save(in_mem_file, format = "PNG")
#	img.save("see.png")
	in_mem_file.seek(0)
	img_bytes = in_mem_file.read()

	# convert to Base64
	newimg = base64.b64encode(img_bytes)
	newimg = newimg.decode('ascii')

	x = requests.post("http://api.ocr.space/parse/image", {'apikey': 'f3fcac1ce988957', 'base64Image' : 'data:image/png;base64,' + newimg})

#	print(x.content.decode())

	if "Timed out waiting for results" in x.content.decode():
		print("[-] Timed out on API")

	myjson = json.loads(x.content.decode())
	mystring = myjson['ParsedResults'][0]['ParsedText']

	print("[+]: string found: " + mystring)

	if len(mystring) > 0:
		r.send(mystring)
		mybase64 = recvall(r).decode()

		print(mybase64[0:64])

		if mybase64.startswith("iVBOR"):
			print("[+] got new challenge")
		elif mybase64.startswith("flag"):
			print("[+] got flag: " + mybase64)
			break
		else:
			print("[-] error, got: " + mybase64)
			break

	else:
		print("[-] error: string not found")
