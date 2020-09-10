#!/usr/bin/env python3
import json

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

from pwn import *

def result():
    response = r.recv(1024)
    response = json.loads(response)
    if not response["success"]:
        print(f"{test['mode']} {test['operation']} failed")
        exit(1)

r = remote("127.0.0.1", 3000)

# ECB encrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
pt = test["data"]

aes = AES.new(key, AES.MODE_ECB)
ct = aes.encrypt(pt.encode())

print(f"ECB encrypt answer: {ct.hex()}")
r.send(ct.hex())
result()

# ECB decrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
ct = bytes.fromhex(test["data"])

aes = AES.new(key, AES.MODE_ECB)
pt = aes.decrypt(ct)

print(f"ECB decrypt answer: {pt.decode()}")
r.send(pt)
result()

# CBC encrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
iv = bytes.fromhex(test["iv_or_counter"])
pt = test["data"]

aes = AES.new(key, AES.MODE_CBC, iv)
ct = aes.encrypt(pt.encode())

print(f"CBC encrypt answer: {ct.hex()}")
r.send(ct.hex())
result()

# CBC decrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
iv = bytes.fromhex(test["iv_or_counter"])
ct = bytes.fromhex(test["data"])

aes = AES.new(key, AES.MODE_CBC, iv)
pt = aes.decrypt(ct)

print(f"CBC decrypt answer: {pt.decode()}")
r.send(pt)
result()

# CTR encrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
counter = test["iv_or_counter"]
pt = test["data"]

aes = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=int(counter, 16)))
ct = aes.encrypt(pt.encode())

print(f"CTR encrypt answer: {ct.hex()}")
r.send(ct.hex())
result()

# CTR decrypt
test = json.loads(r.recv(1024))
key = bytes.fromhex(test["key"])
counter = test["iv_or_counter"]
ct = bytes.fromhex(test["data"])

aes = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=int(counter, 16)))
pt = aes.decrypt(ct)

print(f"CTR decrypt answer: {pt.decode()}")
r.send(pt)
result()

flag = json.loads(r.recv(1024))
print(flag["flag"])
