#!/usr/bin/python3
def weight_average(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return 0
    else:
        numerator = 0
        denominator = 0

        for a_tuple in my_list:
            numerator += a_tuple[0] * a_tuple[1]
            denominator += a_tuple[1]
        return (numerator/denominator)

