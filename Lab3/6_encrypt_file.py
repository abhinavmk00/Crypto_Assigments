#!/usr/bin/python

import string

file_path = 'text.txt'

with open(file_path, 'r') as file:
    contents = file.read()

key = int(input("Enter key : ")) 
cipher = ""

for element in contents:
    if element in string.ascii_letters:
        temp = ord(element)+key
        if(temp > ord('z')):
            temp = temp - 26
        cipher=cipher+chr(temp)
    else:
        cipher=cipher+element

print(cipher)