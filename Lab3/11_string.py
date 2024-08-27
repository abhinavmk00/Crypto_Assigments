#!/usr/bin/python

import string

plain = input("Enter plain text : ")

output=""

print("lowercase characters")

for ele in plain:
    if ele in string.ascii_lowercase:
        output=output+ele

print(output)
print("\n")
output=""

print("uppercase characters")

for ele in plain:
    if ele in string.ascii_uppercase:
        output=output+ele

print(output)
print("\n")
output=""

print("lowercase and uppercase characters")

for ele in plain:
    if ele in string.ascii_letters:
        output=output+ele

print(output)
print("\n")
output=""

print("digits")

for ele in plain:
    if ele in string.digits:
        output=output+ele

print(output)
print("\n")
output=""

print("punctuation symbols")
for ele in plain:
    if ele in string.punctuation:
        output=output+ele

print(output)
print("\n")
count=0


print("number of punctuation symbols")
for ele in plain:
    if ele in string.punctuation:
        count+=1

print(count)