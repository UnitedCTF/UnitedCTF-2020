#!/usr/bin/env python3
import io
import base64
import requests
import hashlib

from pwn import *

NUMBER_OF_TESTS = 1000000

r = remote("127.0.0.1", 3000)

while True:
	problem = r.recv(1024).decode().strip()

	if len(problem) == 0:
		print("[-] empty problem")
		break

	if problem.startswith("flag"):
		print("[+] flag: " + problem)
		break

	print("[+] new hash to crack: " + problem)

	# on a cracké un hash sur https://crackstation.net/ donc on a une idée du format
	possible_solution = 0
	while possible_solution < NUMBER_OF_TESTS:
		newhash = hashlib.sha1(str(possible_solution).encode('ascii')).hexdigest()

		if newhash == problem:
			break
		else:
			possible_solution += 1

	if possible_solution == NUMBER_OF_TESTS:
		print("[-] solution not found")
		break

	# found solution
	possible_solution = str(possible_solution)
	print("[+] cracked password: " + possible_solution)

	r.send(possible_solution)

