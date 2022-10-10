#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        i = 0
        new_list = []
        while i < x:
            new_list.append(str(my_list[i]))
            i += 1
            count += 1
        num = "".join(new_list)
        print(int(num))
        return count

    except IndexError:
        if x > 5:
            n = x - 5
            while i < (x - n):
                new_list.append(str(my_list[i]))
                i += 1
                count += 1
            num = "".join(new_list)
            print(int(num))
            return count
