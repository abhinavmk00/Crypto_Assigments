#!/usr/bin/python

text=input("enter cipher text:")
key = 3
out=""
text=text.lower()

for ele in text:
    if(ord(ele)<=ord("c")):
        ele=chr(ord(ele)+26)

    out=out+chr(ord(ele)-key)

print(out)