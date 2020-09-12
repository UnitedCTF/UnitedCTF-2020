#!/usr/bin/env python3
import io
import base64
import requests
import time

from pwn import *

r = remote("127.0.0.1", 3000)

while True:
	math_problem = r.recv(1024).decode()

	if len(math_problem) == 0:
		print("[-] empty problem")
		break

	if math_problem.startswith("flag"):
		print("[+] flag: " + math_problem)
		break

	print("[+] new math problem: " + math_problem.strip())
	solution = str(eval(math_problem))
	print("[+] solution: " + str(solution))

	r.send(solution)

