#!/usr/bin/python

text=input("plain text : ")
k1=input("input key 1 :")
k2=input("input key 2 :")

cipher=""
text=text.upper()

for ele in text:
    if ele.isalpha():
        x=ord(ele)-ord('A')
        y=(k1*x+k2)%26
        cipher=cipher+chr(y+ord('A'))

print("cipher text : "+cipher)

out=""

k1_inv=25

for ele in cipher:
    shift=ord('A')
    char=(k1_inv*((ord(ele)-shift)-k2))%26
    out+=chr(char+shift)

print ("plain text : "+out)
