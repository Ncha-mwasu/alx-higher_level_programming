#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    if idx < 0:
        list_copy = my_list
        return list_copy
    elif idx > list_len:
        list_copy = my_list
        return list_copy
    else:
        list_copy = my_list[:]
        list_copy[idx] = element
        return (list_copy)
