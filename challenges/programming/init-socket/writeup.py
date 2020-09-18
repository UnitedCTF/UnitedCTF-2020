#!/usr/bin/env python3
from pwn import *

r = remote("challenges.unitedctf.ca", 3004)

name = r.recvline()
print(name.decode().strip())

r.send(name)
print(r.recvall().decode())
