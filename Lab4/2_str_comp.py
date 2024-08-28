#!/usr/bin/python

text = input("input :")
out=""
count = 1

for ele in range(len(text)-1):
    
    temp = text[ele]
    if text[ele] == text[ele+1]:
        count+=1
    else:
        out=out+text[ele]+str(count)
        count=1

out=out+text[-1]+str(count)
print(out)