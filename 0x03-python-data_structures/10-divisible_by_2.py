#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_even = []
    for items in range(len(my_list)):
        if my_list[items] % 2 == 0:
            is_even.append(True)
        else:
            is_even.append(False)

    return(is_even)
