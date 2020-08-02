#!/usr/bin/env python3

import struct
import sys

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import flag


def remove_newline(string):
    if string[-2 : ] == "\r\n":
        return string[: -2]
    elif string[-1] in ["\r", "\n"]:
        return string[: -1]
    else:
        return string


if __name__ == '__main__':
    key = Random.get_random_bytes(16)
    aes = AES.new(key, AES.MODE_ECB)

    while True:
        print("""ECB Crypto Menu
1. Encrypt data
2. Get flag
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
            name = input("> Enter your name: ").replace("&", "").replace("=", "")
            name = remove_newline(name)

            cookie = f"name={name}&flag=False"
            ciphertext = aes.encrypt(pad(cookie.encode(), 16))

            print(f"Cookie: {cookie}")
            print(f"Ciphertext: {ciphertext.hex()}")
        elif choice == "2":
            cookie = input("> Enter your cookie: ")
            cookie = bytes.fromhex(cookie)

            plaintext = unpad(aes.decrypt(cookie), 16).decode()

            for entry in plaintext.split("&"):
                key, value = entry.split("=")

                if key == "flag" and value == "True":
                    print(flag.flag)
