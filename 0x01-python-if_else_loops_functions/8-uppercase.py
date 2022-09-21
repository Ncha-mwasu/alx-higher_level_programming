#!/usr/bin/python3
# uppercase - coverts to the upper case
# str: parameter description
# Return: no return

def uppercase(str):
    for i in str:
        ascii_val = ord(i)
        if ascii_val > 96 and ascii_val < 123:
            ascii_char = chr(ascii_val - 32)
        else:
            ascii_char = chr(ascii_val)
        print("{:s}".format(ascii_char), end="")
    print()
