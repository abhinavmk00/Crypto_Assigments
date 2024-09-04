#!/usr/bin/python3

import string

plain=input("plain : ")
cipher = ""
key=2

plain=plain.upper()
output=""
for ele in plain:
    if ele not in string.whitespace:
        output=output+ele

plain=output

for i in range(key):
    for ele in range(i,len(plain),key):
        cipher = cipher + plain[ele]

print(cipher)
