def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    new_list = []
    while i < x:
        try:
            new_list.append(str(my_list[i]))
            i += 1
            count += 1
            num = int("".join(new_list))

        except IndexError:
            break
    print("{}".format(num))
    return count
