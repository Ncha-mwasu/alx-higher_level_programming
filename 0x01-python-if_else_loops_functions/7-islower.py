#!/usr/bin/python3
# islower check if string's in lower case
# character: argument taken
# REturn: True

def islower(character):
    if ord(character) > 96 and ord(character) < 123:
        return True
    else:
        return False
