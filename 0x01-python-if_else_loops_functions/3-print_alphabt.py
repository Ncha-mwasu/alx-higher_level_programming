#!/usr/bin/python3
letters = 97
while letters < 123:
    if letters != 101 and letters != 113:
        print("{}".format(chr(letters)), end = "")
    letters += 1
