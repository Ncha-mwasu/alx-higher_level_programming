#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_len1 == 0:
        a1 = 0
        b1 = 0
    elif tuple_len1 == 1:
        a1 = tuple_a[0]
        b1 = 0
    else:
        a1 = tuple_a[0]
        b1 = tuple_a[1]

    if tuple_len2 == 0:
        a2 = 0
        b2 = 0
    elif tuple_len2 == 1:
        a2 = tuple_b[0]
        b2 = 0
    else:
        a2 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + a2, b1 + b2)
    return (new_tuple)
