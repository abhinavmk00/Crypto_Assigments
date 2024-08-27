#!/usr/bin/python

a=input("first word : ")
b=input("second word : ")

fre_a = {}
fre_b = {}

for ele in a :
    if ele in fre_a:
        fre_a[ele]=fre_a[ele]+1
    else:
        fre_a[ele]=1

for ele in b :
    if ele in fre_b:
        fre_b[ele]=fre_b[ele]+1
    else:
        fre_b[ele]=1

if fre_a == fre_b :
    print ("anagram")
else :
    print ("not anagram")