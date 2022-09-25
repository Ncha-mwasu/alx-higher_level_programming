#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    if string_len == 0:
        str_tuple = (string_len, None)
        return str_tuple

    else:
        first_char = sentence[0]
        str_tuple = (string_len, first_char)
        return str_tuple
