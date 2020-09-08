#!/usr/bin/env python3
import json

from pwn import *

r = remote("127.0.0.1", 3000)

data = json.loads(r.recv(1024).decode())

child = data["child"]["child"]
child["grandparent"] = data["name"]

r.send(json.dumps(child))
print(r.recvall().decode())
