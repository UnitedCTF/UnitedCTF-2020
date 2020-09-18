#!/usr/bin/env python3
import json

from pwn import *

r = remote("challenges.unitedctf.ca", 3005)

data = json.loads(r.recv(1024).decode())

child = data["child"]["child"]
child["grandparent"] = data["name"]

r.send(json.dumps(child))
print(r.recvall().decode())
