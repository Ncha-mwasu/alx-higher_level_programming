#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            num = my_list[i]
            i += 1
            print("{}".format(num), end="")

        except IndexError:
            break
    print()
    return i
