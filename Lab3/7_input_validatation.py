#!/usr/bin/python

import string

plain = input("Enter plain text : ")

output=""

print("special charaters not allowed")

for ele in plain:
    if ele not in string.punctuation:
        output=output+ele

print(output)
print("\n")
output=""

print("numbers not allowed")

for ele in plain:
    if ele not in string.digits:
        output=output+ele

print(output)
print("\n")
output=""

print("empty values not allowed")

for ele in plain:
    if ele not in string.whitespace:
        output=output+ele

print(output)
print("\n")
output=""

print("uppercase not allowed if upper convert")
output = plain
print(output.lower())



