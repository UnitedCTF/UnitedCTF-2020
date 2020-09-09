#!/usr/bin/env python3
from pwn import *

r = remote("127.0.0.1", 3000)

name = r.recvline()
print(name.decode().strip())

r.send(name)
print(r.recvall().decode())
