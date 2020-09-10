#!/usr/bin/env python3
import sys

from Crypto.Util.Padding import pad, unpad

from pwn import *


def local():
    return remote("localhost", 3003)

def server():
    raise Exception("Unimplemented")


r = local()

def encrypt(data):
    if isinstance(data, bytes):
        data = data.hex()
    else:
        data = data.encode().hex()

    r.recvuntil("choice:")
    r.sendline("2")
    r.recvuntil("format):")
    r.sendline(data)
    r.recvuntil("Result: ")

    encoded = r.recvline().decode()[: -1]
    return bytes.fromhex(encoded)

def find_fill_length(base_length):
    for fill_length in range(1, 17):
        result = encrypt("A" * fill_length)

        if len(result) > base_length:
            return fill_length

def get_flag(base_length, fill_length):
    print(f"Base length = {base_length}")
    print(f"Fill length = {fill_length}")
    print(f"Flag length = {base_length - fill_length}")

    flag_length = base_length - fill_length
    flag = ""

    for flag_index in range(flag_length):
        fill = "A" * (fill_length + flag_index + 1)
        ciphertext = encrypt(fill)
        attack_block = ciphertext[base_length : base_length + 16]

        found = False
        for test_char in "abcdefghijklmnopqrstuvwxyz1234567890-ABCDEFGHIKLMNOPQRSTUVWXYZ":
            test_block = pad((test_char + flag).encode(), 16)[: 16] + b"A" * fill_length
            encrypted_test = encrypt(test_block)[: 16]

            if encrypted_test == attack_block:
                flag = test_char + flag
                found = True
                break
        
        if not found:
            print("Catastrophic failure")
            sys.exit(1)

        print(flag)


base_length = len(encrypt(""))
fill_length = find_fill_length(base_length)

if fill_length == 16:
    fill_length = 0
    base_length -= 16

get_flag(base_length, fill_length)
