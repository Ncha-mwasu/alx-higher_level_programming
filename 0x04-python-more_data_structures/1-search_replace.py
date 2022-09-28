#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for numbers in new_list:
        if numbers == search:
            search = replace
        return new_list
