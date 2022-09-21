#!/usr/bin/python3
# uppercase - coverts to the upper case
# str: parameter description
# Return: no return

def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
