#!/usr/bin/python3
# remove_char_at - removes string at a certain index
# str: given string parameter
# n: index parameter

def remove_char_at(str, n):
    if n < 0:
        return str
    if n >= 0:
        return(str[:n] + str[n + 1:])
