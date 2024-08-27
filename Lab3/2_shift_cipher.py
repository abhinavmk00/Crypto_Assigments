#!/usr/bin/python

import string

print("Shift Cipher")

plain = input("Enter plain text : ")
key = int(input("Enter key : ")) 
cipher = ""

for element in plain:
    if element in string.ascii_letters:
        temp = ord(element)+key
        if(temp > ord('z')):
            temp = temp - 26
        cipher=cipher+chr(temp)
    else:
        cipher=cipher+element

print(cipher)


