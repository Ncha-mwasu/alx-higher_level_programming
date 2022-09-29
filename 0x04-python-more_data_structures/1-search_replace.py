#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    list_len = len(new_list)
    for item in range(list_len - 1):
        if new_list[item] == search:
            new_list[item] = replace
    return new_list
