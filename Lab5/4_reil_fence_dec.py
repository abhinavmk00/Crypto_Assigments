#!/usr/bin/python3

import string

cipher=input("cipher : ")
plain = ""

cipher=cipher.upper()
output=""
for ele in cipher:
    if ele not in string.whitespace:
        output=output+ele

cipher=output

if(len(cipher)%2!=0):
    cipher=cipher+" "

half=int(len(cipher)/2)

for ele in range(half):
    plain=plain+cipher[ele]
    plain=plain+cipher[ele+half]
    

print(plain)
