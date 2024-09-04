#!/usr/bin/python

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1

text = input("plain text : ").upper()
k1 = int(input("input key 1 : "))
k2 = int(input("input key 2 : "))


cipher = ""
for ele in text:
    if ele.isalpha():
        x = ord(ele) - ord('A')
        y = (k1 * x + k2) % 26
        cipher += chr(y + ord('A'))
    else:
        cipher += ele

print("cipher text : " + cipher)

k1_inv = mod_inverse(k1, 26)

out = ""
for ele in cipher:
    if ele.isalpha():
        shift = ord('A')
        char = (k1_inv * ((ord(ele) - shift) - k2)) % 26
        out += chr(char + shift)
    else:
        out += ele

print("plain text : " + out)
