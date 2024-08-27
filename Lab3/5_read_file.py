#!/usr/bin/python

file_path = 'text.txt'

with open(file_path, 'r') as file:
    contents = file.read()

print(contents)
