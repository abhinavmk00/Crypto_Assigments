#!/usr/bin/python

plain=input("plain : ")
cipher=input("cipher : ")

plain=plain.lower()
cipher=cipher.lower()

key=ord(cipher[0])-ord(plain[0])

print("key : "+str(key))