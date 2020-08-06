#!/usr/bin/env python3

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import flag


if __name__ == '__main__':
    key = Random.get_random_bytes(16)
    aes = AES.new(key, AES.MODE_ECB)

    while True:
        print("""ECB Crypto Menu
1. Encrypt flag
2. Exit
""")
        choice = input("> Your choice: ").strip()

        if choice not in "12" or choice == "":
            print("Invalid choice.")
            continue

        if choice == "2":
            print("Goodbye!")
            break
        
        name = input("> Please enter your name: ")
        data = f"{name}{flag.flag}"
        print(f"Result: {aes.encrypt(pad(data.encode(), 16)).hex()}")
