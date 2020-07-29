#!/usr/bin/env python3

import struct
import sys

from Crypto import Random
from Crypto.Cipher import AES

import flag


def counter(nonce):
    count = 0

    while True:
        count_bytes = struct.pack('>Q', count)
        count += 1
        yield nonce + count_bytes


if __name__ == '__main__':
    key = Random.get_random_bytes(16)
    nonce = Random.get_random_bytes(8)

    while True:
        print("""CTR Crypto Menu
1. Encrypt flag
2. Encrypt data
3. Exit
""")
        choice = input("> Your choice: ").strip()

        if choice not in "123" or choice == "":
            print("Invalid choice.")
            continue

        if choice == "3":
            print("Goodbye!")
            break
        
        if choice == "1":
            aes = AES.new(key, AES.MODE_CTR, nonce = nonce, initial_value = 0)
            data = flag.flag
        elif choice == "2":
            aes = AES.new(key, AES.MODE_CTR, nonce = nonce, initial_value = 0)
            data = input("> Data to encrypt: ")

        print(f"Result: {aes.encrypt(data.encode()).hex()}")