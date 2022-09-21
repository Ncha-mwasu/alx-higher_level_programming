#!/usr/bin/python3
for letters in range(122, 96, -1):
    if letters % 2 != 0:
        char = (letters - 32)
    else:
        char = letters
    print("{}".format(chr(char)), end="")
