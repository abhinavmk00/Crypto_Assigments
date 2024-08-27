#!/usr/bin/python

import string

text = input("Enter the text :")

text = text.lower()

fre={}

for i in text:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
        
print(fre)

for char, count in fre.items():
    print(f"{char}: {'*' * count}")