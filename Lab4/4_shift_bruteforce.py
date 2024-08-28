#!/usr/bin/python

text=input("enter cipher text:")
text=text.lower()

for key in range(26):
    out=""
    for ele in text:
        if(ord(ele)<=ord("c")):
            ele=chr(ord(ele)+26)

        out=out+chr(ord(ele)-key)

    print(str(key)+" : "+out)