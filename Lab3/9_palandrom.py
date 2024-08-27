#!/usr/bin/python

text=input("enter string : ")

flag=True

for i in range (0,int(len(text)/2)):
    if text[i] != text[len(text)-i-1] :
        flag = False
        break

if(flag):
    print("plandrom")
else:
    print("not palandrom")