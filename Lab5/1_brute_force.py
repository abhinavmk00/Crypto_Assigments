#!/usr/bin/python

import string

print("brute force")

cipher = "dvvkzecfssprkkve"
plain = ""

for key in range(0,25):
    for ele in cipher:
        if ele in string.ascii_letters:
            temp = ord(ele)+key
            if(temp > ord('z')):
                temp = temp - 26
            plain=plain+chr(temp)
        else:
            plain=plain+ele

    print(str(key)+" : "+plain)
    plain=""
